import rospy
import time
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from math import sqrt

current_pose = None

def pose_callback(msg):
    global current_pose
    current_pose = msg.pose.pose

def publish_goal(pub, x, y, z):
    goal = PoseStamped()
    goal.header.frame_id = ""
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = z
    goal.pose.orientation.w = 0.0  # No rotation

    pub.publish(goal)

# def send_goals(pub):
#     while True:
#         goal_x = float(input("Enter x-coordinate (or 'q' to quit): "))
#         if goal_x == 'q':
#             break

#         goal_y = float(input("Enter y-coordinate: "))
#         goal_z = float(input("Enter z-coordinate: "))

#         rospy.loginfo(f"Goal: x={goal_x}, y={goal_y}, z={goal_z}")
#         publish_goal(pub, goal_x, goal_y, goal_z)

#         while True:
#             if reached_goal(goal_x, goal_y, tolerance=0.1):
#                 rospy.loginfo("Reached the goal!")
#                 break
#             rospy.sleep(1)
def send_goals_from_file(pub, filename):
    with open(filename, 'r') as file:
        for line in file:
            goal_x, goal_y, goal_z = map(float, line.strip().split(','))  # Split by commas
            
            rospy.loginfo(f"Goal: x={goal_x}, y={goal_y}, z={goal_z}")
            publish_goal(pub, goal_x, goal_y, goal_z)

            while True:
                if reached_goal(goal_x, goal_y, tolerance=0.3):
                    rospy.loginfo("Reached the goal!")
                    break
                rospy.sleep(1)
            rospy.sleep(4)

def reached_goal(goal_x, goal_y, tolerance=0.3):
    global current_pose
    if current_pose is None:
        return False
    current_x = current_pose.position.x
    current_y = current_pose.position.y
    distance = sqrt((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2)
    return distance < tolerance

def main():
    rospy.init_node('simple_goal_publisher')

    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.Subscriber('/mavros/local_position/odom', Odometry, pose_callback)

    rospy.sleep(1)  # Wait for publisher and subscriber to connect

    try:
        goal_file = "goal.txt"  # Modify this to the path of your goal file
        send_goals_from_file(pub, goal_file)
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()


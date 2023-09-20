def print_pattern():
    for z in range(1, 13):
        # Moving right along the x-axis
        for x in range(7):
            print(f"{x}.0, 0.0, {z}.0")
        
        # Moving down along the y-axis
        for y in range(-1, 0, -1):
            print(f"6.0, {y}.0, {z}.0")
        
        # Moving left along the x-axis
        for x in range(6, -1, -1):
            print(f"{x}.0, -1.0, {z}.0")
        
        # Moving up along the y-axis
        for y in range(0, 1):
            print(f"0.0, {y}.0, {z}.0")

print_pattern()

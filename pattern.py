def generate_pattern(max_z):
    pattern = []
    for x in range(int(max_z) + 1):
        if x % 2 == 0:
            for y in range(7):
                pattern.append((float(y), 0.0, float(x) + 1.0))  # Start from 1.0 meter
        else:
            for y in range(6, -1, -1):
                pattern.append((float(y), 0.0, float(x) + 1.0))  # Start from 1.0 meter
    return pattern

def main():
    max_z = float(input("Enter the maximum Z-coordinate: "))
    result = generate_pattern(max_z)
    for point in result:
        print(f"{point[0]}, {point[1]}, {point[2]}")

if __name__ == "__main__":
    main()

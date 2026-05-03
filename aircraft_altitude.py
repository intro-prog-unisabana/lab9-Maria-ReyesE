from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n").strip()
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()

        if command == "X":
            break

        parts = command.strip().split()

        if len(parts) < 2:
            continue

        action = parts[0].strip()
        feet_str = parts[1].strip()

        if not feet_str.lstrip('-').isdigit():
            continue

        feet = int(feet_str)

        if action == "A":
            aircraft.ascend(feet)
        elif action == "D":
            aircraft.descend(feet)

    print(f"Final altitude: {aircraft.altitude} feet")

if __name__ == "__main__":
    main() 
    
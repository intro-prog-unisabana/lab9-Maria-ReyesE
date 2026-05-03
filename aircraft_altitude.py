from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n")
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()

        if command == "X":
            break

        parts = command.split()

        # 🔥 Validar que tenga 2 partes
        if len(parts) != 2:
            continue

        action, feet = parts[0], int(parts[1])

        if action == "A":
            aircraft.ascend(feet)
        elif action == "D":
            aircraft.descend(feet)

    print(f"Final altitude: {aircraft.altitude} feet")

if __name__ == "__main__":
    main()
    
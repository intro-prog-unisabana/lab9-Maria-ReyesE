from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n")
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()

        if command == "X":
            break

        parts = command.split()
        action = parts[0]
        feet = int(parts[1])

        if action == "A":
            aircraft.climb(feet)   # 🔥 aquí está el fix
        elif action == "D":
            aircraft.descend(feet)

    print(f"Final altitude: {aircraft.altitude} feet")

if __name__ == "__main__":
    main()
    
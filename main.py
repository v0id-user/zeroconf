from sys import argv
import announce
import discovery

def main():
    if len(argv) < 2:
        print("Usage: python main.py [announce|discover]")
        print("Options:")
        print("  announce    Register and broadcast this device's presence on the network")
        print("  discover    Search for and show other announced devices on the network")
        return

    if argv[1] == "announce":
        announce.register_service()
    elif argv[1] == "discover":
        discovery.discover_service()
    else:
        print(f"Unknown command: {argv[1]}")
        print("Available options: announce, discover")


if __name__ == "__main__":
    main()

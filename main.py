from sys import argv
import announce
import discovery

def main():
    if argv[1] == "announce":
        announce.register_service()
    elif argv[1] == "discover":
        discovery.discover_service()


if __name__ == "__main__":
    main()

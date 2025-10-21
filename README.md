# ZeroConf Discovery

An experiment with ZeroConf/Bonjour service discovery using Python.

![ZeroConf Discovery Demo](./demo.gif)

## What is ZeroConf Discovery?

ZeroConf (Zero Configuration Networking) is a collection of technologies that enable devices on a local network to discover and communicate with each other without manual setup or a central directory server. It underpins Apple's Bonjour protocol, and is widely used for things like printer or service discovery.

## How does it work?

- **Announcing a Service:** Devices broadcast their presence on the network by registering a service (e.g., an HTTP server) with ZeroConf. 
- **Discovering Services:** Other devices listen for these announcements and can find services dynamically without knowing them ahead of time.

## How to use

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Announce your service:**
   In one terminal, register your device/service on the network:
   ```bash
   python main.py announce
   ```

3. **Discover available services:**
   In another terminal (can be on another machine on the same local network):
   ```bash
   python main.py discover
   ```

## Notes

- You can run the announce and discover scripts each from completely different machines, but both devices *must* be on the same local network.
- This project uses the [zeroconf](https://pypi.org/project/zeroconf/) Python library.
- The announce script must remain running for the service to stay visible to others.

Feel free to experiment further by changing the service details or port!

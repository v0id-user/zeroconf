# ZeroConf Discovery

My experiment with ZeroConf Discovery.

![ZeroConf Discovery](./demo.gif)

# What is ZeroConf Discovery?

ZeroConf Discovery is a protocol that allows devices to discover each other on the network without the need for a central server. It is a part of the Bonjour/Zeroconf family of protocols.

# How does it work?

Devices register themselves with a Zeroconf server, and other devices can discover them by querying the Zeroconf server.

# How can I use/test it?

```bash
pip install -r requirements.txt

# Run the announce script to register your device with the Zeroconf server
python main.py announce

# Run the discover script to discover other devices on the network from a different terminal
python main.py discover
```


# Notes
- You can run this from a completely different machine, but they must be on the same network.

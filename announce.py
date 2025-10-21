from zeroconf import ServiceInfo, Zeroconf
from utils import get_local_ip
import socket

local_ip = get_local_ip()

info = ServiceInfo(
    "_http._tcp.local.",
    "v0id-user._http._tcp.local.",
    addresses=[socket.inet_aton(local_ip)],
    port=8080,
    properties={"path": "/"},
    server="v0id.local.",
)

def register_service():
    zeroconf = Zeroconf()
    print("📡 Registering service...")
    zeroconf.register_service(info)

    input("Press Enter to unregister...")
    zeroconf.unregister_service(info)
    zeroconf.close()
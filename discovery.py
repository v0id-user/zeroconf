from zeroconf import ServiceBrowser, Zeroconf, ServiceStateChange

def on_service_state_change(zeroconf: Zeroconf, service_type: str, name: str, state_change: ServiceStateChange):
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            host = ".".join(map(str, info.addresses[0])) if info.addresses else "Unknown"
            port = info.port
            print(f"Found service: {name} at {host}:{port}")

def discover_service(timeout=5, service_type="_http._tcp.local."):
    zeroconf = Zeroconf()
    try:
        ServiceBrowser(zeroconf, service_type, handlers=[on_service_state_change])
        print(f"Discovering services of type '{service_type}' for {timeout} seconds...")
        from time import sleep
        sleep(timeout)
    finally:
        zeroconf.close()

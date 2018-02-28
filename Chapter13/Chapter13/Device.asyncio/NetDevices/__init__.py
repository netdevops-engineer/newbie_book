def DeviceHandler(device):
    os_type = device.get("OS_type", "JUNOS")
    try:
        device_module = __import__("NetDevices.%s" %os_type)
    except ImportError:
        pass

    device_module = getattr(device_module, os_type)
    device_class = getattr(device_module, os_type)
    return device_class(device)

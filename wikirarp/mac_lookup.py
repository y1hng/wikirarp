from mac_vendor_lookup import MacLookup

_mac_lookup = MacLookup()

def get_device_vendor(mac_address):
    try:
        return _mac_lookup.lookup(mac_address)
    except Exception:
        return "Unknown"

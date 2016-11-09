#!/usr/bin/env python


from net_system.models import NetworkDevice
import django

def main():

    django.setup()

    test_rtr1 = NetworkDevice(
        device_name="test-rtr1",
        device_type="cisco_ios",
        ip_address="192.168.0.1",
        port=5022
    )
    test_rtr1.save()

    test_rtr2 = NetworkDevice.objects.get_or_create(
        device_name="test-rtr2",
        device_type="cisco_ios",
        ip_address="192.168.0.2",
        port=5122
    )

    print
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device
    print

if __name__ == "__main__":
    main()

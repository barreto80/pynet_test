#!/usr/bin/env python

from net_system.models import NetworkDevice
import django

def main():


    django.setup()
    try:
        test_rtr1 = NetworkDevice.objects.get(device_name='test-rtr1')
        test_rtr1.delete()
        test_rtr2 = NetworkDevice.objects.get(device_name='test-rtr2')
        test_rtr2.delete()
    except NetworkDevice.DoesNotExist:
        pass

    # Verify devices that currently exist
    print
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device
    print

if __name__ == "__main__":
    main()

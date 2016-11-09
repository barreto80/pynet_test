#!/usr/bin/env python

import django
from pprint import pprint as pp
from net_system.models import NetworkDevice, Credentials

def main():

    django.setup()
    net_devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()

    std_creds = creds[0]
    arista_creds = creds[1]

    for i in net_devices:
        if 'arista' in i.device_type:
            i.credentials = arista_creds
        else:
            i.credentials = std_creds
        i.save()

    for i in net_devices:
        print i, i.credentials

#    pp (net_devices)
#    pp (net_devices[0].__dict__)

if __name__ == "__main__":
  main()

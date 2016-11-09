#!/usr/bin/env python

import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pynxos.device import Device
from pprint import pprint


# Disable untrusted CERT warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def check_nxapi_errors(results, verbose=False):
    """Return True if all commands are None"""
    for entry in results:
        if entry is not None:
            if verbose:
                print entry
            return False
    return True




nexus_ip = "nxos3.twb-tech.com"
nxs = Device(host=nexus_ip, username="pyclass", password="88newclass", transport='https', port=8443)

#nxs_facts = nxs.facts
#pprint (nxs_facts)


def main():
    """Configure BGP using NX-API."""
    # Nexus switches
    # switch_ip = raw_input("Enter switch IP: ")
    # username = 'pyclass'
    # password = getpass()
    eth_intf = "Ethernet 2/2"
    intf_ip = '10.1.4.5/30'
    peer_ip = '10.1.4.6'
    as_number = '10'

    config_eth = [
        'interface ' + eth_intf,
        'ip address ' + intf_ip
    ]

    config_bgp = [
        'router bgp ' + as_number,
        'neighbor {} remote-as {}'.format(peer_ip, as_number),
        'address-family ipv4 unicast',
    ]


    print "\nCurrent Ethernet config: "
    cmd = 'show run int {}'.format(eth_intf)
    print nxs.show(cmd, raw_text=True)

    print "\nConfig Eth Interface:"
    results = nxs.config_list(config_eth)
    if check_nxapi_errors(results):
        print "...interface configured successfully."

    print "\nCurrent Ethernet config: "
    cmd = 'show run int {}'.format(eth_intf)
    print nxs.show(cmd, raw_text=True)

####### Try to ping the other side using netmiko ######

    print
    print "-" * 50
    print "BGP Config"
    print "-" * 50

    cmd = 'show run bgp'
    print nxs.show(cmd, raw_text=True)

    print "\nConfigure BGP"
    results = nxs.config_list(config_bgp)
    if check_nxapi_errors(results):
        print "...BGP configured successfully."

    cmd = 'show run bgp'
    print nxs.show(cmd, raw_text=True)

    print "\nVerify BGP (requires both peers)."
    print "Sleeping..."
    time.sleep(15)
    cmd = 'show bgp session'
    bgp_out = nxs.show(cmd)
    pprint(bgp_out)

    print "\nSaving config..."
    print nxs.save()

if __name__ == "__main__":
  main()

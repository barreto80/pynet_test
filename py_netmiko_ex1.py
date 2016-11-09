#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

def save_file(filename, content):
  with open(filename, "w") as f:
    f.write(content)

def main():
  rtr1_pass = getpass("Enter rtr1 password: ")
  sw1_pass = getpass("Enter sw1 password: ")

  pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': rtr1_pass,
  }

  pynet_sw1 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.72',
    'username': 'pyclass',
    'password': sw1_pass,
  }

  for devices in (pynet_rtr1, pynet_sw1):
    device_con = ConnectHandler(**devices)
    print "Current Prompt: " + device_con.find_prompt()
    sh_ver = device_con.send_command("show version")
    sh_run = device_con.send_command("show run")
    filename = device_con.base_prompt + ".txt"
    print
    print "*" *50
    print sh_ver
    print "*" *50
    print
    print "Saving \"show run\" to file: {}".format(filename)
    print
    save_file(filename, sh_run)

if __name__ == "__main__":
  main()

#!/usr/bin/env python

import subprocess
import os
from datetime import datetime

GIT = '/usr/bin/git'
CFGS_DIR = '/home/bbarret7/pynet_test/CFGS'

def subprocess_handler(cmd_list):
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (std_out, std_err) = proc.communicate()
    if std_err:
        print std_err
    return std_out

def main():
    os.chdir(CFGS_DIR)
    git_add = [GIT, 'add', '*.cfg']
    std_out = subprocess_handler(git_add)
    commit_str = "Add configs for the subprocess exercise at ({})".format(datetime.now())
    git_commit = [GIT, 'commit', '-m', commit_str]
    std_out = subprocess_handler(git_commit)

if __name__ == "__main__":
    main()

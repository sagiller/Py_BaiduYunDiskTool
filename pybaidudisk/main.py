#!/usr/bin/python

from disk import NetDisk

disk = NetDisk("sagiller", "P8hBQJc9LXBx")
if disk.check_login():
    files = disk.list()
    disk.upload("/Users/hujiazhao/Documents/Codes/Python/pybaidudisk-master/hellotest")
a = 1
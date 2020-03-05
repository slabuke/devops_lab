#!/usr/bin/env python
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-path", help="Input path", required=True)
parser.add_argument("-par", action="store_true", help="output files only from the parent directory")
parser.add_argument("-rec", action="store_true", help="list files recursively")
parser.add_argument("-ext", help="filter by file extension")
parser.add_argument("-sname", action="store_true", help="order output by filename")
parser.add_argument("-stime", action="store_true", help="order output by date of creation")
parser.add_argument('-v', action='version', version='version 1.0')

args = parser.parse_args()

# output files only from the parent directory
if args.par:
    for entry in os.listdir(args.path):
        if os.path.isfile(os.path.join(args.path, entry)):
            print(entry)

# list files recursively
if args.rec:
    for root, folders, files in os.walk(args.path):
        for filename in files:
            print(root, filename)

# filter by file extension
if args.ext:
    for root, dirs, files in os.walk(args.path):
        for file in files:
            if file.endswith(args.ext):
                print(os.path.join(root, file))

# order output by filename
if args.sname:
    s = sorted(os.listdir(args.path))
    for i in range(len(s)):
        print(s[i])

# order output by date of creation
if args.stime:
    file_list = os.listdir(args.path)
    full_list = [os.path.join(args.path, i) for i in file_list]
    time_sorted_list = sorted(full_list, key=os.path.getmtime)
    for i in time_sorted_list:
        print(i)

#!/usr/bin/env python

import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-path", nargs='?', action="store", default="./", help="Input path")
parser.add_argument("-par", action="store_true", help="output files only from the parent directory")
parser.add_argument('-ext', nargs='?', default=False, action="store", dest='ext', help='extention filter')
parser.add_argument("-sname", action="store_true", help="order output by filename")
parser.add_argument("-stime", action="store_true", help="order output by date of creation")

args = parser.parse_args()


def par():
    list = []
    timelist = []
    for files in os.listdir(args.path):
        if os.path.isfile(os.path.join(args.path, files)):
            list.append(files)
        timelist.append(os.path.getctime(os.path.join(args.path, files)))
    return list, timelist


def rec():
    list = []
    timelist = []
    for root, folders, files in os.walk(args.path):
        for filename in files:
            list.append(filename)
            timelist.append(os.path.getctime(os.path.join(root, filename)))
    return list, timelist


def time_sort(time, list):
    listout = [x for _, x in sorted(zip(time, list))]
    return listout


if args.par:
    nlist, tlist = par()
    if args.sname:
        nlist.sort()
    elif args.stime:
        nlist = time_sort(tlist, nlist)

    if args.ext:
        for name in nlist:
            if name.endswith("." + args.ext):
                print(name)
    else:
        for name in nlist:
            print(name)

else:
    nlist, tlist = rec()
    if args.sname:
        nlist.sort()
    elif args.stime:
        nlist = time_sort(tlist, nlist)

    if args.ext:
        for name in nlist:
            if name.endswith("." + args.ext):
                print(name)
    else:
        for name in nlist:
            print(name)

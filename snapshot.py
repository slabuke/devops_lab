#!/usr/bin/env python

import psutil
import json
import argparse
import time
from time import gmtime, strftime

parser = argparse.ArgumentParser(description='Simple server system monitoring script.')
parser.add_argument('interval', type=int, nargs='?', const=1, default=300, help='Time interval.')
parser.add_argument('data_type', type=str, nargs='?', const=1, default='txt', help='f-format.')
args = parser.parse_args()


class CompInfo:

    def __init__(self):
        self.mb = 1024 * 1024
        self.cpu = psutil.cpu_percent()
        self.mem = psutil.disk_usage('/').used
        self.vmem = psutil.virtual_memory().active
        self.iodiskr = psutil.disk_io_counters().read_bytes
        self.iodiskw = psutil.disk_io_counters().write_bytes
        self.ionets = psutil.net_io_counters().packets_sent
        self.ionetr = psutil.net_io_counters().packets_recv

    def cpuload(self):
        return self.cpu

    def memus(self):
        return self.mem // self.mb

    def vmemus(self):
        return self.vmem // self.mb

    def iodiskbytes(self):
        return str(self.iodiskr // self.mb), str(self.iodiskw // self.mb)

    def ionetpack(self):
        return self.ionets, self.ionetr


def WriteToJson(file, interval):
    i = 0
    # data = {}
    while True:
        cinfo = CompInfo()
        data1 = {
            'SNAPSHOTS': str(i + 1),
            'TIME': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
            'Cpu Load': str(cinfo.cpuload()),
            'Memory usage': str(cinfo.memus()),
            'Virtual Memory Usage': str(cinfo.vmemus()),
            'I/O disk': str("Read: " + "mb/Write: ".join(cinfo.iodiskbytes())),
            'I/O network, packets': str("Sent: " + "/Received: ".join(cinfo.iodiskbytes()))
               }
        
        with open(file, 'a+') as outfile:
            outfile1 = json.dumps(data1, indent=4)
            outfile.write(outfile1)
            i += 1
            time.sleep(interval)


def WriteToFile(file, interval):

    fileTxt = open(file, "w+")
    i = 0
    while True:
        fileTxt = open(file, "a+")
        cinfo = CompInfo()
        fileTxt.write('SNAPSHOTS ' + str(i + 1) + '\r\n'),
        fileTxt.write('Time ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '\r\n')
        fileTxt.write("\t\t\t Cpu Load: %s\r\n" % str(cinfo.cpuload()))
        fileTxt.write("\t\t\t Memory usage: %s mb\r\n " % str(cinfo.memus()))
        fileTxt.write("\t\t\t Virtual memory usage: %s mb\r\n" % str(cinfo.vmemus()))
        fileTxt.write("\t\t\t I/O disk. Read: %s mb Write: %s mb\r\n" % cinfo.iodiskbytes())
        fileTxt.write("\t\t\t I/O network, packets. Read %s Write: %s\r\n" % cinfo.iodiskbytes())
        fileTxt.close()
        i += 1
        time.sleep(interval)


if args.data_type == 'json':
    WriteToJson('data.json', args.interval)

elif args.data_type == 'txt':
    WriteToFile('data.txt', args.interval)

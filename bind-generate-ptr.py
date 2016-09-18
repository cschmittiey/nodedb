#!/usr/bin/python

import sys
# https://raw.githubusercontent.com/google/ipaddr-py/master/ipaddr.py
import ipaddr
import time

# Point this to the "nodes" file from nodedb

with open("nodes") as fd:
    content = fd.readlines()

print "$TTL 3600"
print "$ORIGIN c.f.ip6.arpa."
print ""

print "@\tIN SOA\th.ns.net. hostmaster.h.ns.net. (\n" + \
          "\t\t" + str(int(time.time())) + "    ; serial\n" + \
          "\t\t1h               ; slave refresh interval\n" + \
          "\t\t15m              ; slave retry interval\n" + \
          "\t\t1w               ; slave copy expire time\n" + \
          "\t\t1h               ; NXDOMAIN cache time\n" + \
          "\t)"
print "\tIN NS\th.ns.net"
print "h.ns.net\tIN AAAA\t::1"
for line in content:
    tokens = line.strip().split(" ")
    if not tokens[0] == '' and not tokens[1] == '':
        ip = ipaddr.IPv6Network(tokens[0]).exploded.split("/")[0]
        print ".".join(ip[2:][::-1].replace(":", "")) + "\tIN\tPTR\t" + tokens[1].split("/")[0] + "."

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import re
import sys

single_matcher = re.compile("(?P<bytes>\d+) bytes from (?P<IP>\d+.\d+.\d+.\d+): icmp_seq=(?P<sequence>\d+) ttl=(?P<ttl>\d+) time=(?P<time>\d+(.\d+)?) ms")
# should match lines like this:
# 64 bytes from 192.168.178.45: icmp_seq=2 ttl=64 time=103 ms
end_matcher = re.compile("rtt min/avg/max/mdev = (?P<min>\d+.\d+)/(?P<avg>\d+.\d+)/(?P<max>\d+.\d+)/(?P<mdev>\d+.\d+)")
# should match lines like this:
# rtt min/avg/max/mdev = 0.234/0.234/0.234/0.000 ms
# alternative matcher for a different ping utility:
#end_matcher = re.compile("round-trip min/avg/max/stddev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Ping a host and create histogram.')
    parser.add_argument('host', help='The host to ping')
    parser.add_argument('--count', '-c', type=int, default=4, help='Number of times the host should be pinged')
    parser.add_argument('--interval', '-i', type=float, default=1.0, help='Interval between individual pings.')
    parser.add_argument('--debug', '-d', action='store_true', help='Enable debug output for this script')
    args = parser.parse_args()

    ping = subprocess.Popen(
        ["ping", "-c", str(args.count), "-i", str(args.interval), args.host],
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT
    )

    try:
        times = []
        sentinel = b"" if sys.version_info[0] >= 3 else ""
        for line in iter(ping.stdout.readline, sentinel):
            line = line.decode('ascii').strip()
            if not line: continue
            if args.debug: print("Analyzing this line: " + line)
            match = single_matcher.match(line)
            if match:
                if args.debug: print("Matches found: {}".format(match.groups()))
                time = float(match.group('time'))
                times.append(time)
                print(time)
                continue
            match = end_matcher.match(line)
            if match:
                if args.debug: print("Matches found: {}".format(match.groups()))
                continue
            if args.debug: print("Didn't understand this line: " + line)
    except KeyboardInterrupt:
        sys.exit()

    if args.debug: print("Exit Code of the ping command: " + str(ping.returncode))
    sys.exit(ping.returncode)

if __name__ == "__main__":
    main()


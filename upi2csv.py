#!/usr/bin/env python3
#
# Simple Python script to export POIs into a CSV file from a
# proprietary UPI POI file used by old Sygic GPS navigation
# systems.
#
# https://github.com/lrswss/upi2csv
#
# Copyright (c) 2024 Lars Wessels <software@bytebox.org>
# This script comes with no warranties, use at your own risk!
#
# Published as OSS under the MIT license.
# https://opensource.org/license/mit
#

import sys

if (len(sys.argv) != 3):
    print("Usage: %s <upi-file> <2-letter-countrycode>" % sys.argv[0])
    sys.exit(1)

upi_file = sys.argv[1]
nullbytecountry_code = sys.argv[2]
exportcount = 0

with open(upi_file, "rb") as f:
    nullbytecount = 0
    nibble = 0
    while nibble != "":
        # simple POI record starts with 0x0 0x3 header
        nibble = int.from_bytes(f.read(1))
        if (nibble == 0):
            nibble = int.from_bytes(f.read(1))
            if (nibble == 3):
                nullbytecount = 0
                size = int.from_bytes(f.read(4), byteorder='little') - 17
                # skip POI entry (invalid size)
                if (size > 512):
                    continue
                lon = int.from_bytes(f.read(4), byteorder='little')
                lat = int.from_bytes(f.read(4), byteorder='little')
                print("%.4f,%.4f,%s-" % (lon/100000, lat/100000, nullbytecountry_code.upper()), end="")
                exportcount += 1
                lastByte = 0
                commaFound = False
                while (size >= 0):
                    byte = int.from_bytes(f.read(2), byteorder='little')
                    size -= 2
                    # skip strange country code header if present
                    if (byte == 65535):
                        f.read(12)
                        size -= 12
                        continue
                    if (byte > 31) and (byte != 34):
                        # remove duplicate spaces
                        if (byte == 32 and lastByte == 32):
                            continue
                        # omit all commas except for the first one
                        # after the location field to ensure csv format
                        if (byte == 44):
                            if (commaFound):
                                continue
                            else:
                                commaFound = True 
                        print("%s" % chr(byte), end="")
                        lastByte = byte
                print()
            else:
                # triggers exit at end of file
                nullbytecount += 1
                if (nullbytecount > 256):
                    print(">>> %d POIs found in file '%s'" % (exportcount, upi_file), file=sys.stderr) 
                    break

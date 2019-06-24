#!/bin/python
 
  # # # # # # # # # # # # # # # # # # # #
  #   K3PNW       ____     _            #
  #   _________ _/ / /____(_)___ _____  #
  #  / ___/ __ `/ / / ___/ / __ `/ __ \ #
  # / /__/ /_/ / / (__  ) / /_/ / / / / #
  # \___/\__,_/_/_/____/_/\__, /_/ /_/  #
  #                      /____/         #
  #  Michael Peters                     #
  #  2019
  # # # # # # # # # # # # # # # # # # # #

import argparse
import requests
import json
import sys

#argument handlers
if (len(sys.argv) > 1):
    parser = argparse.ArgumentParser(prog="callsign")

    parser.add_argument('callsign')
    parser.add_argument('--status', action='store_true', help="show status of license")
    parser.add_argument('--type', action='store_true', help="show type of license")
    parser.add_argument('--call', action='store_true', help="show callsign")
    parser.add_argument('--opclass', action='store_true', help="show class of license")

    parser.add_argument('--name', action='store_true', help="show name of licensee")
    parser.add_argument('--address', action='store_true', help="show address of licensee")

    parser.add_argument('--latlong', action='store_true', help="show coordinates of licensee")
    parser.add_argument('--grid', action='store_true', help="show grid square of licensee")

    parser.add_argument('--expiry', action='store_true', help="show expire date of license")
    parser.add_argument('--url', action='store_true', help="show FCC url of license")

    parser.add_argument('--raw', action='store_true', help="no formatting on output")

    args = parser.parse_args()

    r = requests.get('https://callook.info/{}/json'.format(args.callsign))
    result = json.loads(r.text)

    #parsing
    status = result["status"]
    if(status == "INVALID"):
        print(status)

    else:
        licenseType = result["type"]
        call = result["current"]["callsign"]
        opClass = result["current"]["operClass"]
        name = result["name"]
        add1 = result["address"]["line1"]
        add2 = result["address"]["line2"]
        attn = result["address"]["attn"]
        lat = result["location"]["latitude"]
        long = result["location"]["longitude"]
        gridSquare = result["location"]["gridsquare"]
        grantDate = result["otherInfo"]["grantDate"]
        expiryDate = result["otherInfo"]["expiryDate"]
        url = result["otherInfo"]["ulsUrl"]

        if (len(sys.argv) == 2):
            print("call:       ", call)
            print("name:       ", name)
            print("address:    ", add1, add2)
            print(" ")
        
        if (len(sys.argv) == 3 and args.raw):
            print(call)
            print(name)
            print(add1, add2)

        else:
            if args.raw:
                if args.status:
                    print(status)
                if args.type:
                    print(licenseType)
                if args.call:
                    print(call)
                if args.opclass:
                    print(opClass)    
                if args.name:
                    print(name)    
                if args.address:
                    print(add1, add2)
                if args.latlong:
                    print(lat + ",", long)
                if args.grid:
                    print(gridSquare)
                if args.expiry:
                    print(expiryDate)
                if args.url:
                    print(url)
            else:
                if args.status:
                    print("status:     ", status)
                if args.type:
                    print("type:       ", licenseType)
                if args.call:
                    print("call:       ", call)
                if args.opclass:
                    print("class:      ", opClass)    
                if args.name:
                    print("name:       ", name)    
                if args.address:
                    print("address:    ", add1, add2)
                if args.latlong:
                    print("coordinates:", lat + ",", long)
                if args.grid:
                    print("grid:       ", gridSquare)
                if args.expiry:
                    print("expiry:     ", expiryDate)
                if args.url:
                    print(url)

else:
    
    call = input("Enter a callsign:")

    r = requests.get('https://callook.info/{}/json'.format(call))
    result = json.loads(r.text)

    #parsing
    status = result["status"]
    if(status == "INVALID"):
        print(status)

    else:
        licenseType = result["type"]
        call = result["current"]["callsign"]
        name = result["name"]
        add1 = result["address"]["line1"]
        add2 = result["address"]["line2"]

        print("call:    ", call)
        print("name:    ", name)
        print("address: ", add1, add2)
        print(" ")
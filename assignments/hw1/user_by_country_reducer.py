#!/usr/bin/env python

import sys
import csv

def init():
    with open('IP2LOCATION-LITE-DB1.CSV', 'rb') as f:
        reader = csv.reader(f)
        return list(reader)


def search_country(ipstr, ipdb):
    parts = ipstr.split('.')
    ip_int = (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    for item in ipdb:
        if int(item[0])<=ip_int and int(item[1])>=ip_int:
            return item
    return None

def main():
    (current_key) = (None)
    
    ipdb = init()
    users_by_country = dict()

    for line in sys.stdin:
        line = line.strip()
        try:
            key, value = line.split('\t', 1)
        except ValueError:
            (key, value) = (line, 1)
        
        if current_key != key:
            current_key=key
            country = search_country(current_key, ipdb)
            if country:
                if country[3] in users_by_country:
                    users_by_country[country[3]]=users_by_country[country[3]]+1
                else:
                    users_by_country[country[3]]=1

    for key, value in users_by_country.iteritems() :
        print "%s\t%d" % (key, value)            
        
        
if __name__ == '__main__':
    main()
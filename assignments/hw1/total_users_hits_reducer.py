#!/usr/bin/env python


import sys

# key = user
# value = time and also hit

def main():
    (current_key, count_uniq_users, count_hits) = (None,0,0)
    for line in sys.stdin:
        line = line.strip()
        try:
            key, value = line.split('\t', 1)
        except ValueError:
            (key, value) = (line, 1)
        if current_key != key:
            count_uniq_users+=1
            current_key = key
        count_hits +=1
    print "%d\t%d" % (count_uniq_users, count_hits)
if __name__ == '__main__':
    main()
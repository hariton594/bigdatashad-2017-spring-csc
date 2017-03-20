#!/usr/bin/env python
# подсчет сессий и хитов

import sys

def main():
    (current_key, hits, sessions, last_time) = (None,0,0,0)

    for line in sys.stdin:
        line = line.strip()
        try:
            key, time = line.split('\t', 1)
            time = int(time)
        except ValueError:
            (key, time) = line, 1

        if current_key != key:
            if current_key:
                print "%s\t%d\t%d" % (current_key, hits, sessions)
            hits = 0
            sessions=0
            last_time=0
            current_key = key
        hits += 1
        if (time>last_time+30*60)
            sessions+=1
        last_time=time

    if current_key:
        print "%s\t%d\t%d" % (current_key, hits, sessions)


if __name__ == '__main__':
    main()
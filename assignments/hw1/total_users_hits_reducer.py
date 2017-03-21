#!/usr/bin/env python
from __future__ import division

import sys

# key = user
# value = time and also hit

def main():
    (current_key, count_uniq_users, count_hits, total_sessions_time, total_sessions_count, total_skelets_count, total_sessions_size) = (None,0,0,0,0,0,0)
    last_time = 0
    issession = False
    for line in sys.stdin:
        line = line.strip()
        try:
            key, value = line.split('\t', 1)
        except ValueError:
            (key, value) = (line, 1)
        time = int(value)
        if current_key != key:
            if not issession and current_key:
                total_skelets_count+=1
            issession=False
            last_time=time 
            count_uniq_users+=1
            current_key = key
        else:
            if time<last_time+30*60: #in session
                if not issession:
                    issession=True
                    total_sessions_count+=1
                    total_sessions_size+=1 #adding previous hit
                total_sessions_size+=1
                total_sessions_time+=time-last_time
        
            else:
                if not issession and last_time>0:
                    total_skelets_count+=1
                issession=False
            last_time=time
            
        count_hits +=1
    
    print "%d\t%d\t%d\t%d\t%d\t%d" % (count_uniq_users, count_hits, total_sessions_count, total_sessions_time, total_sessions_size, total_skelets_count)
if __name__ == '__main__':
    main()

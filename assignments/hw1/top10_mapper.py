import sys
import re

# get urls
def main():
    current_key = None
    record_re = re.compile('([\d\.:]+) - - \[(\S+ [^"]+)\] "(\w+) ([^"]+) (HTTP/[\d\.]+)" (\d+) \d+ "([^"]+)" "([^"]+)"')
    for line in sys.stdin:
        match = record_re.match(line)
        if not match:
            continue
        if match.group(6) != "200":
            continue
        print match.group(6)


if __name__ == '__main__':
    main()
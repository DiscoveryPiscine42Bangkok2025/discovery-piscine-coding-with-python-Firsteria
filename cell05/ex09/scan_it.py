import sys
import re

if len(sys.argv) < 2:
    print("none")
else:
    key = sys.argv[1]
    x = re.findall(key, sys.argv[2])
    ans = len(x)
    print(ans)
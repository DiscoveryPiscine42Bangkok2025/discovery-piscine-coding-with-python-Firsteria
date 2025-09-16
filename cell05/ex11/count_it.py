import sys
args = sys.argv[1:]
print(f"parameters: {len(args)}")
for arg in args:
    print(f"{arg} : {len(arg)}")
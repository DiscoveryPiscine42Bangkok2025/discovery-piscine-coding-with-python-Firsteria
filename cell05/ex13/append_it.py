import sys

args = sys.argv[1:]

if len(sys.argv) < 2:
    print("none")
else:
    for word in args:
        if not word.endswith("ism"):
            print(word + "ism")
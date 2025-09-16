import sys

input_sys = sys.argv[1]

count = input_sys.count('z')

if count == 0:
    print('none')
elif len(sys.argv) != 2:
    print('none')
else:
    print('z' * count)
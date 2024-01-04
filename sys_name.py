import sys

'''
try:
    print("Hello, my name is", sys.argv[1])  #at [0] is the script name eg: name.py and [1] is command-line argument
except IndexError:
    print("script name:", sys.argv[0])
'''

#----------------------------------------------

'''
# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# print name tags
print("Hello, my name is", sys.argv[1])
'''

#-----------------------------------------------

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, My name is", arg)

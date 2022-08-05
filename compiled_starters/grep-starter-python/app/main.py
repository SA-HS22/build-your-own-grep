import sys
import os

from dataclasses import dataclass

# import pyparsing - available if you need it!
# import lark - available if you need it!

if sys.argv[1] != "-E":
    print("Expected first argument to be '-E'")
    os.exit(1)

pattern = sys.argv[2]
input = sys.stdin.read()

# You can use print statements as follows for debugging, they'll be visible when running tests.
print("Logs from your program will appear here!")

if len(pattern) == 1:
    # Uncomment this block to pass the first stage
    # if input.count(pattern) > 0:
    #     os.exit(0)
    # else:
    #     os.exit(1)
else:
    print(f"Unhandled pattern: {pattern}")

import math
import sys
from os import rename

import requests

# name = input("Your Name?")
# print("Hello,", name)


print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("world"))
print(greet("corey"))


r = requests.get("http://coreyms.com")
print(r.status_code)

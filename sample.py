# python file
import math
import os
import sys

import requests

# input can only be used with terminal only
# name = input("Kimi No Nawa? ")
# print("Hello,", name)

print(sys.version)

print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)

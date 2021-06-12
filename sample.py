import requests

# input can only be used with terminal only
# name = input("Kimi No Nawa? ")
# print("Hello,", name)

# print(sys.version)

# print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)


# try to pull one last time, deleted previous 2 lines, added 1 line
# create new branch
# this is the changes i made in new branch 2
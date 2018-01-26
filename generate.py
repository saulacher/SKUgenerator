import string, random
import sys


def pick(num):
    for j in range(num):
        print("".join([random.choice(string.digits) for i in range(3)])+"-"+"".join([random.choice(string.ascii_uppercase) for i in range(3)])+"-"+"".join([random.choice(string.digits) for i in range(3)]))

num1 = int(sys.argv[1])

pick(num1)

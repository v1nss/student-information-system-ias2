import random

header = "TUPM-21-"
randnum = str(random.randint(1000,9999))

studentID = ("".join([header, randnum]))

print(studentID)
import random
from datetime import datetime

startTime = datetime.now()


my_list = []

x = 0
while x < 1_000_000_000:
    my_list.append(random.randint(0,9))
    x += 1

print(datetime.now() - startTime)

# Det tok 0:27:21.314278 
import os
import random
import time
import eyed3


path = 'C:\\Users\\shubh\\Music\\'
items = os.listdir(path)
length = len(items)
checker = 0

i = 0
while i < len(items):
    try:
        if os.path.isfile(os.path.join(path, items[i])):
            checker += 1
            i += 1
        else:
            del items[i]
    except Exception as e:
        pass

length2 = len(items)
# for _ in range(0, length2-1):
#
#     if '.mp3' in items[_]:
#         pass
#     else:
#         del (items[_])
#
#
# random.shuffle(items)
# random.shuffle(items)
# random.shuffle(items)
# shuffles = random.randrange(10)
# for shuffles in range(0, shuffles):
#     random.shuffle(items)
#
#
# for length2 in range(0, length2):
#     file = eyed3.load(path + items[length2])
#     stop = int(file.info.time_secs + 1)
#     os.startfile(path + items[length2])
#     time.sleep(stop)


data = eyed3.load(path+items[0])
print(data)
time = data.path.__add__()



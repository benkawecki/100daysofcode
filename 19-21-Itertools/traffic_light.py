from itertools import cycle, product, permutations, combinations
import sys
import time

traffic_light = cycle(['Green','Yellow','Red'])

while True:
    current_light = next(traffic_light)
    sys.stdout.write('\r {}        '.format(current_light))
    sys.stdout.flush()
    time.sleep(1)

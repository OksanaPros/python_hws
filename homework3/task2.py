import hashlib
import random
import struct
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


if __name__ == "__main__":
    import time

    start_time = time.time()
    with Pool(25) as p:
        print(sum(p.imap_unordered(slow_calculate, range(501), chunksize=20)))
    print("--- %s seconds ---" % (time.time() - start_time))

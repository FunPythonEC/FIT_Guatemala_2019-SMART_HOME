import MMA8452
import time
def word(l, h):
    """
    Given a low and high bit, converts the number back into a word.
    """
    return (h << 8) + l

acc=MMA8452.MMA8452()
while True:
    dato=acc.get_x()
    print(str(type(dato)) + " " + str(dato))
    print(word(dato[0],dato[1]))
    time.sleep(0.1)
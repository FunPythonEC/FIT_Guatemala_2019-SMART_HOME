import MMA8452
import time

acc=MMA8452.MMA8452()
while True:
    dato=acc.get_acc()
    print('X: ', dato[0],' | ','Y: ', dato[1],' | ','Z: ', dato[2])
    #print(str(type(dato)) + " " + str(dato))
    #print(word(dato[0],dato[1]))
    time.sleep(0.08)

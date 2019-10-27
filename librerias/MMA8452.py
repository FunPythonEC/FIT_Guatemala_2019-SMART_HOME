import machine
import time

# listas de registros
STATUS_MMA8452Q = 0x00
OUT_X_MSB = 0x01
OUT_X_LSB = 0x02
OUT_Y_MSB = 0x03
OUT_Y_LSB = 0x04
OUT_Z_MSB = 0x05
OUT_Z_LSB = 0x06
SYSMOD = 0x0B
INT_SOURCE = 0x0C
WHO_AM_I = 0x0D
XYZ_DATA_CFG = 0x0E
HP_FILTER_CUTOFF = 0x0F
PL_STATUS = 0x10
PL_CFG = 0x11
PL_COUNT = 0x12
PL_BF_ZCOMP = 0x13
P_L_THS_REG = 0x14
FF_MT_CFG = 0x15
FF_MT_SRC = 0x16
FF_MT_THS = 0x17
FF_MT_COUNT = 0x18
TRANSIENT_CFG = 0x1D
TRANSIENT_SRC = 0x1E
TRANSIENT_THS = 0x1F
TRANSIENT_COUNT = 0x20
PULSE_CFG = 0x21
PULSE_SRC = 0x22
PULSE_THSX = 0x23
PULSE_THSY = 0x24
PULSE_THSZ = 0x25
PULSE_TMLT = 0x26
PULSE_LTCY = 0x27
PULSE_WIND = 0x28
ASLP_COUNT = 0x29
CTRL_REG1 = 0x2A
CTRL_REG2 = 0x2B
CTRL_REG3 = 0x2C
CTRL_REG4 = 0x2D
CTRL_REG5 = 0x2E
OFF_X = 0x2F
OFF_Y = 0x30
OFF_Z = 0x31

# objeto definido
# hace falta todavia ciertos metodos
class MMA8452(object):

    # scl y sda por default para esp32
    def __init__(self, scl=22, sda=23):
        self.scl=scl
        self.sda=sda
        self.i2c=machine.I2C(scl=machine.Pin(scl), sda=machine.Pin(sda), freq=400000)
        self.address=None
        
        addrs = self.i2c.scan()
        if addrs[0]==0x1D:
            self.address=addrs[0]
        else:
            raise Exception('Address not right, should be 29 or 0x1d. It is ',addrs[0])
        self.active(1)


    # metodos para cada eje
    def get_x(self):
        ret=self.i2c.readfrom_mem(self.address,OUT_X_MSB,2)
        time.sleep_ms(10)
        return list(ret)

    def get_y(self):
        ret=self.i2c.readfrom_mem(self.address,OUT_Y_MSB,2)
        time.sleep_ms(10)
        return list(ret)

    def get_z(self):
        ret=self.i2c.readfrom_mem(self.address,OUT_Z_MSB,2)
        time.sleep_ms(10)
        return list(ret)

    # estado activo de acelerometro
    def active(self, status):
        time.sleep_ms(100)
        if status==1:
    		self.i2c.writeto_mem(self.address,CTRL_REG1,b'\x01')
    	else:
    		self.i2c.writeto_mem(self.address,CTRL_REG1,b'\x00')
		time.sleep_ms(100)




    
        




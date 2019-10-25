from machine import Pin, PWM

pwm = PWM(Pin(14))
# duty de 0-1000
# cambiar la frecuencia freq de 0-1000
pwm.freq(500)
pwm.duty(100)

    

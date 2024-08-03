import time
import board
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

Skit = ServoKit(channels=16)


# =====================================================
    
def led_R0():
        Skit.servo[3].angle = None
        
        
def led_R1():
        Skit.servo[3].angle = 50
        
#=====================================================    
        
def led_G0():
        Skit.servo[4].angle = None
        
        
def led_G1():
        Skit.servo[4].angle = 50
        
#===================================================== 
        
def led_B0():
        Skit.servo[5].angle = None
        
        
def led_B1():
        Skit.servo[5].angle = 50
        
#=====================================================

def led_W0():
        Skit.servo[7].angle = None
        
        
def led_W1():
        Skit.servo[7].angle = 90

#=====================================================

def led_Y0():
        Skit.servo[8].angle = None
        
        
def led_Y1():
        Skit.servo[8].angle = 80
        
#=====================================================

def led_O0():
        Skit.servo[6].angle = None
        
        
def led_O1():
        Skit.servo[6].angle = 50
        
#=====================================================

def leds_an():
        led_W1()
        led_R1()
        led_B1()
        led_G1()
        led_Y1()
        led_O1()
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++
        
def leds_aus():
        led_W0()
        led_R0()
        led_B0()
        led_G0()
        led_Y0()
        led_O0()
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++
        
def led_start():
        led_W0()
        led_R0()
        led_B0()
        led_G0()
        led_Y0()
        led_O0()
        
        led_R1()
        time.sleep(0.1)
        led_R0()
        led_G1()
        time.sleep(0.1)
        led_G0()
        led_B1()
        time.sleep(0.1)
        led_B0()
        led_O1()
        time.sleep(0.1)
        led_O0()
        led_W1()
        time.sleep(0.1)
        led_W0()
        led_Y1()
        time.sleep(0.1)
        led_Y0()
        led_W1()
        time.sleep(0.1)
        led_W0()
        led_O1()
        time.sleep(0.1)
        led_O0()
        led_B1()
        time.sleep(0.1)
        led_B0()
        led_G1()
        time.sleep(0.1)
        led_G0()
        led_R1()
        time.sleep(0.1)
        led_R0()
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++

def led_blink():
        leds_aus()
        time.sleep(0.2)
        leds_an()
        time.sleep(0.2)
        leds_aus()
        time.sleep(0.2)
        leds_an()
        time.sleep(0.2)
        leds_aus()
        time.sleep(0.2)
        leds_an()
        time.sleep(0.2)
        leds_aus()
        time.sleep(0.2)
        leds_an()
        time.sleep(0.2)
        leds_aus()
        time.sleep(0.2)
        leds_an()
        time.sleep(0.2)
        leds_aus()
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++

def led_flow():
        led_R1()
        time.sleep(0.1)
        led_G1()
        led_R0()
        time.sleep(0.1)
        led_B1()
        led_G0()
        time.sleep(0.1)
        led_O1()
        led_B0()
        time.sleep(0.1)
        led_W1()
        led_O0()
        time.sleep(0.1)
        led_Y1()
        led_W0()
        time.sleep(0.1)
        led_Y0()
        time.sleep(0.3)
        led_R1()
        time.sleep(0.1)
        led_G1()
        led_R0()
        time.sleep(0.1)
        led_B1()
        led_G0()
        time.sleep(0.1)
        led_O1()
        led_B0()
        time.sleep(0.1)
        led_W1()
        led_O0()
        time.sleep(0.1)
        led_Y1()
        led_W0()
        time.sleep(0.1)
        led_Y0()
        time.sleep(0.3)
        led_R1()
        time.sleep(0.1)
        led_G1()
        led_R0()
        time.sleep(0.1)
        led_B1()
        led_G0()
        time.sleep(0.1)
        led_O1()
        led_B0()
        time.sleep(0.1)
        led_W1()
        led_O0()
        time.sleep(0.1)
        led_Y1()
        led_W0()
        time.sleep(0.1)
        led_Y0()
        time.sleep(0.3)
        led_R1()
        time.sleep(0.1)
        led_G1()
        led_R0()
        time.sleep(0.1)
        led_B1()
        led_G0()
        time.sleep(0.1)
        led_O1()
        led_B0()
        time.sleep(0.1)
        led_W1()
        led_O0()
        time.sleep(0.1)
        led_Y1()
        led_W0()
        time.sleep(0.1)
        led_Y0()
        time.sleep(0.3)
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++ 

def led_startup():
        led_flow()
        time.sleep(0.2)
        led_blink()

#++++++++++++++++++++++++++++++++++++++++++++++++++++ 

def led_ende():
        leds_an()
        time.sleep(0.5)
        leds_aus()
        time.sleep(0.5)
        leds_an()
        time.sleep(0.5)
        leds_aus()

#++++++++++++++++++++++++++++++++++++++++++++++++++++ 

#Reihenfolge der Led's: RGBOWY


if __name__ == '__main__':
        try:
            leds_aus()
            
                        
                 
        except KeyboardInterrupt:
                print("Messung vom User gestoppt")
                GPIO.cleanup()
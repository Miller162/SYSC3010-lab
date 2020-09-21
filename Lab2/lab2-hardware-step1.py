from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def m_logo(): 
  R = red
  O = nothing
  
  logo = [
    O, O, O, O, O, O, O, O,
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, R, R, O, 
    O, R, O, R, R, O, R, O, 
    O, R, O, R, R, O, R, O, 
    O, R, O, O, O, O, R, O, 
    O, R, O, O, O, O, R, O,
    O, O, O, O, O, O, O, O]
  return logo
  
def t_logo(): 
  R = red
  O = nothing
  
  logo = [
    O, O, O, O, O, O, O, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O, 
    O, O, O, R, R, O, O, O, 
    O, O, O, R, R, O, O, O, 
    O, O, O, R, R, O, O, O, 
    O, O, O, R, R, O, O, O,
    O, O, O, O, O, O, O, O]
  return logo
  
images = [m_logo, t_logo]
count = 0

#note, keyboard input required additional library that I could not figure out how to install for this emulator.
while True: 
  s.set_pixels(images[count % len(images)]())
  time.sleep(.75)
  count += 1
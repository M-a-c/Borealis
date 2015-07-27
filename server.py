#Mac Carter UIC 
#In "main" comments partain to the 'todo list' in the code.

DEBUG = True
#REMOVE

#!/usr/bin/env python
# """A simple/readable example of driving a Shiftbrite / Octobar / Allegro A6281 
# via  hardware SPI on the Raspberry Pi.
 
# You must have /dev/spidev* devices / bcm2708_spi driver for this to work.
# """
 
# import fcntl, array, RPi.GPIO as GPIO
#
#	^    ENABLE THE SCRIPT ABOVE    ^
#


#-------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------CREDIT for some snipits go to----------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------#
#																																	  #
# 						    http://docs.macetech.com/doku.php/raspberry_pi_with_octobrite_shiftbrite								  #
#																																      #
#			   	Basic code was used from this webite to help facilitate the use of the rasberri pi's SPI busself. 					  #
#																																	  #
#-------------------------------------------------------------------------------------------------------------------------------------# 
#-------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------#
#																																	  #
#                                https://github.com/backupbrain/tornado-websocket-echo-server										  #
#																																	  #
#                  Basic example code was used form backupbrain's github in order to create this programself.        				  #
#				       His code was a very basic 'echo' websockets example using the tornado librarry								  #
#																																	  #
#																																	  #
#																																	  #
#-------------------------------------------------------------------------------------------------------------------------------------# 

#import the web and socket infromation form tornado packages
import tornado.web
import tornado.websocket
import tornado.ioloop

import time #import time, sleep #time libraries 


 
### /Configuration ###
## Diagram by Mac Carter
## Here is your pi interface
# with the pins layed out on the board
# =======================================
# |								o  5v	|
# |								o  o 	|
# |			---------			o  gnd 	|
# |								o  o	|
# |								o  o	|
# |								o  o 	|
# |								o  o 	|
# |								o  o 	|
# |								o  o 	|
# |								Di o 	|
# |								o  o	|
# |								Ci Ei 	|
# |								o  Li 	|
# |								      	|
# |										|
# |										|
# |										|
# |										|
# |										|
# |										|
# |										|
# |	 __________							|
# |	 |		  |							|
# |	 |ETHERNET|							|
# |	 |		  | 						|
# ===|--------|====|---------|===========
# 			       |===USB===|

### /Configuration ###
 
# set to the number of modules you are controlling.  If this is  a shiftbrite,
#it would be 1, if it's an octobar, 8, etc
 
NUM_LEDS =15
 
#In addition to the hardware SPI pins, we require two general GPIO pins for 
#the enable and latch pins.  It doesn't matter what pins you use
 

ENABLE_PIN = 8
LATCH_PIN  = 7


def printDebug(r,g,b):
	print("r"+str(r))
    print("g"+str(g))
    print("b"+str(b))
    print("\n")
	pass

def unpack_color(v):
    print v
    red = (v[1] & 0b00001111)<<6
    red = (v[2] & 0b11111100)>>2 | red
    print "red: "+str(red)
    green = (v[2] & 0b00000011)<<8
    green = v[3] & 0b11111111 | green
    print "green: "+str(green)
    blue = (v[0] & 0b00111111)<<4
    blue = (v[1] & 0b11110000)>>4 | blue
    print "blue: "+str(blue)
    pass

def bootSequence():
	for x in xrange(0,NUM_LEDS):
        set_led(x, 0, 0, 0)

    update_leds(leds)

    for x in xrange(0,NUM_LEDS):
        set_led(x, 0, 0, 1023)   
	    update_leds(leds)
	    delay(150)


    delay(500)
    for x in xrange(0,NUM_LEDS):
        set_led(x, 1023, 1023, 1023)
    update_leds(leds)

    delay(300)
    for x in xrange(0,NUM_LEDS):
        set_led(x, 0, 0, 0)
    update_leds(leds)

	delay(200)
    for x in xrange(0,NUM_LEDS):
        set_led(x, 1023, 1023, 1023)
   
    update_leds(leds)

	pass

def delay(number):
	time.time()
	time.sleep(float(number)/1000.0)#convert seconds to miliseconds
	pass

def Static():
    if message[3]=="#":
	    r = "0x"+(message[4]+message[5])
	    g = "0x"+(message[6]+message[7])
	    b = "0x"+(message[8]+message[9])

	    r = (eval(r)<<2)
	    g = (eval(g)<<2)
	    b = (eval(b)<<2)

		# printDebug(r,g,b)

	    for x in xrange(0,NUM_LEDS):
	        set_led(x, r, g, b)

	    update_leds(leds)

	pass

def Blinking(message):
	if message[3]=="#":
	    r = "0x"+(message[4]+message[5])
	    g = "0x"+(message[6]+message[7])
	    b = "0x"+(message[8]+message[9])

	    r = (eval(r)<<2)
	    g = (eval(g)<<2)
	    b = (eval(b)<<2)

		# printDebug(r,g,b)

		while False:
		    for x in xrange(0,NUM_LEDS):
		        set_led(x, r, g, b)

		    update_leds(leds)
			delay (200)

		    for x in xrange(0,NUM_LEDS):
		        set_led(x, 0, 0, 0)    

		    update_leds(leds)
			delay (200)

	pass

def Music(message):
## Libarry still needs to be chosen
	pass

def Pulsing(message):#figure out how to maintain luminase intensity still.
	# if message[3]=="#":
	#     r = "0x"+(message[4]+message[5])
	#     g = "0x"+(message[6]+message[7])
	#     b = "0x"+(message[8]+message[9])
	

	# 	r = (eval(r)<<2)
	#     g = (eval(g)<<2)
	#     b = (eval(b)<<2)

	#     #temp vars
	#     rOld = r
	#     gOld = g
	#     bOld = b


	# 	# 100'ths of color subtracted each time.
	#     rMult = r/100
	#     gMult = g/100
	#     bMult = b/100

	# 	while False: # make this a thread that gets interpreted from a global var being set.

	# 	    for x in xrange(0,100):
	# 	    	time.sleep(100)#asuming miliseconds.
	# 	    	if ((r>0) && ((r-rMult)>0)):
	# 	    		r-=rMult
	# 	    	if ((g>0) && ((g-gMult)>0)):
	# 	    		g-=gMult
	# 	    	if ((b>0) && ((b-bMult)>0)):
	# 	    		b-=bMult

	# 	    	for x in xrange(0,NUM_LEDS):
	# 	        	set_led(x, rOld, gOld, bOld)

	# 	    for x in xrange(0,100):
	# 	    	time.sleep(100)#asuming miliseconds.
	# 	    	if (r<bOld && ((r+rMult)<1023):
	# 	    		r+=rMult
	# 	    	if (g<bOld && ((g+gMult)<1023)):
	# 	    		g+=gMult
	# 	    	if (b<bOld && ((b+bMult)<1023)):
	# 	    		b+=bMult

	# 		    for x in xrange(0,NUM_LEDS):
	# 		        set_led(x, r, g, b)

	# 	    update_leds(leds)
	pass

def Strobe(message):#msg format COMMAND(400),COLOR(#XXXXXX) ,INTERVAL_FLASH (2),(3),(4)readDigits  (10,100,1000) 
					#example 400#EF1616240
					#broken up 400-#EF1616-2-40
	if message[3]=="#":
	    r = "0x"+(message[4]+message[5])
	    g = "0x"+(message[6]+message[7])
	    b = "0x"+(message[8]+message[9])

	delayTime = 300# default delayTime

    if message[10]=="2":
    	delayTime = message[11]+message[12]

    if message[10]=="3":
    	delayTime = message[11]+message[12]+message[13]
    
    if message[10]=="4":
    	delayTime = message[11]+message[12]+message[13]+message[14]

    
    delayTime = int(delayTime)

    r = (eval(r)<<2)
    g = (eval(g)<<2)
    b = (eval(b)<<2)

	while False:#still need to figure out threading.
	    for x in xrange(0,NUM_LEDS):
			set_led(x, r, g, b)
	    
	    delay(delayTime/4)#should cause a nice strobe effect.
	    update_leds(leds)

	    for x in xrange(0,NUM_LEDS):
	    	set_led(x, 0, 0, 0)

	    delay(delayTime/2)
	    update_leds(leds)

	pass
    

def PartyMode(message):
	##need to experiment more with what function/sets of repeting color combos might work.
	pass

def Sky(message):
	## how does a sky behave? going to figure out delta map
	colorlist
	ColorList = ["FFCC33","E3A857","FD5E53"]## the three colors.

	# ["FFCC33"]#sunglow yellow
	# ["E3A857"]#deeper orange
	# ["FD5E53"]#sunset orange

	pass

def Wave(message):
	## color switch of temp colors down the line pre defined.
	ColorList = ["FF0000","FF4000","FF8000","FFBF00","FFFF00","BFFF00","80FF00","40FF00","00FF00","00FF40","00FF80","00FFBF","00FFFF","00BFFF","0080FF","0040FF","0000FF","4000FF","8000FF","BF00FF","FF00FF","FF00BF","FF0080","FF0040"]
	for n in xrange(0,1000):
		for i in xrange(0,NUM_LEDS):
			i=i+n
			Hex=ColorList[i%24]
		    r = "0x"+(Hex[0]+Hex[1])
		    g = "0x"+(Hex[2]+Hex[3])
		    b = "0x"+(Hex[4]+Hex[5])

		    r = (eval(r)<<2)
		    g = (eval(g)<<2)
		    b = (eval(b)<<2)

			set_led(i, r, g, b)

		delay(150);
		update_leds(leds)

	pass

def Weather(message):
	##need a weather api 
	pass

def DNDDice(message):
	#come up with encoding scheme, d2 d3 d4 d5 d6
	pass

def Random(message):
	##
	for x in xrange(0,NUM_LEDS):
		r = randint(0, 1023)
		g = randint(0, 1023)
		b = randint(0, 1023)
		for x in xrange(0,NUM_LEDS):
			set_led(x, r, g, b)

	update_leds(leds)
	pass

def Clock(message):

	tOld=0

	t = time.time()
	t = int(t)
	tOld=t

	while False:#add threading
		if tOld!=t:
			t = time.time()
			t = int(t)
			tOld=t

			t = "{0:b}".format(t)

			for x in xrange(0,NUM_LEDS):
				if t[x]=="1":
					set_led(x, 1024, 1024, 1024)
				else:
					set_led(x, 0, 0, 0)

			update_leds(leds)
	pass

def GradentSwitch(message):
	#calculate deltas and switch.
	pass

def DayTime(message):
	##implement time changing elements form red to full bright, maybe transition to sky() and then back to red.
	pass

def Twitter(message):
	#E00 - String (MESSAGE) - INITIAL(COLOR) - Fade (COLOR)
	#still ned to find an API for this.
	pass

def BarLights(message):
	#FOO bar, basically just dim lighting
    for x in xrange(0,NUM_LEDS):
        set_led(x, 700, 500, 500)

    update_leds(leds)
    pass

def telemetry(lightIn,X1,X2,Y1,Y2,time):
	X2-X1
	Y2-Y1
	LightIn

def FlashAllRedPattern():
  #   counter = 3

  #   while counter!=0:
	 #    for x in xrange(0,NUM_LEDS):
	 #        set_led(x, 0, 0, 0)

	 #    update_leds(leds)

		# delay(130)

	 #    for x in xrange(0,NUM_LEDS):
	 #        set_led(x, 1023, 0, 0)

	 #    update_leds(leds)

		# delay(70)

		# counter--
	DEBUG
	pass

def off():
	for x in xrange(0,NUM_LEDS):#turns off the lights. 
		set_led(x, 0, 0, 0)

	update_leds(leds)

	pass

def pack_color(red, green, blue):
    # """Takes 10 bits of each color (0-1023) and packs it into the four bytes
    # needed by the LED controller
 
    # Ported from: http://docs.macetech.com/doku.php/shiftbrite#code_example
    # """
    rv = bytearray(4)
 
    #2bit control, 6bit blue
    rv[0] = (0b00 << 6) & 0b11111111 | blue >> 4
 
    #4bit blue, 4 bit red
    rv[1] = (blue << 4) & 0b11111111 | red >> 6
 
    #6bit red, 2 bit green
    rv[2] = (red  << 2) & 0b11111111 | green >> 8
 
    #8bits green
    rv[3] = green & 0b11111111
 
    return rv
 
def update_leds(bytes):
	# if (!DEBUG):
	#     # """Just write the byte array out to the SPI device and toggle the latch"""
	#     #write the shit out over SPI
	#     spidev.write(bytes)
	#     spidev.flush()
	 
	#     #latch, #rpi is slow enough we don't need a delay here
	#     GPIO.output(LATCH_PIN, 1)
	#     GPIO.output(LATCH_PIN, 0)
	pass
 
 
def set_led(num, red, green, blue):

    # """helper function to quickly set an LED color
 
    # Don't use this in production code, global is bad mmmkay?
    # """
 
    global leds
 
    leds[num*4:(num*4)+4] = pack_color(red, green, blue)
 


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        i=0
        # print "connection opened"
        # self.write_message("connection opened")

    def on_close(self):
        i=0
        print "connection closed"

    def on_message(self,message):
        print "message received: {}".format(message)

		messageHeader = message[0]+message[1]+message[2]

		if messageHeader == "000":#done
			Static(message)
		if messageHeader == "100":#Enable threading
			Blinking(message)
		if messageHeader == "200":#Still searching for a library
			Music(message)
		if messageHeader == "300":#Enable threading
			Pulsing(message)
		if messageHeader == "400":#Enable threading
			Strobe(message)
		if messageHeader == "500":#Search for a good distribution of light colors
			PartyMode(message)
		if messageHeader == "600":#search for a good distibution of random in and out clouds.
			Sky(message)
		if messageHeader == "700":#done add threading
			Wave(message)
		if messageHeader == "800":#need a weather api 
			Weather(message)
		if messageHeader == "900":#come up with encoding scheme, d2 d3 d4 d5 d6
			DNDDice(message)
		if messageHeader == "A00":#done add threading
			Random(message)
		if messageHeader == "B00":#add threading
			Clock(message)
		if messageHeader == "C00":#calculate deltas and switch.
			GradentSwitch(message)
		if messageHeader == "D00":#implement time changing elements form red to full bright, maybe transition to sky() and then back to red.
			DayTime(message)
		if messageHeader == "E00":#still ned to find an API for this.
			Twitter(message)
		if messageHeader == "F00":#BAR get it? bar lighting, just a dim lighting thats all. also done.
			BarLights(message)
		if messageHeader == "0FF":#done
			Off()
			
		else:
			FlashAllRedPattern();#incorrect command.

        # if message[0]=="#":
        #     r = "0x"+(message[0]+message[1])
        #     g = "0x"+(message[2]+message[3])
        #     b = "0x"+(message[4]+message[5])

        #     r = (eval(r)<<2)
        #     g = (eval(g)<<2)
        #     b = (eval(b)<<2)

        #     print("r"+str(r))
        #     print("g"+str(g))
        #     print("b"+str(b))
        #     print("\n")

        #     for x in xrange(0,8):
        #         set_led(x, r, g, b)

        # #Format &RRGGBB,light no;
        # if message[0]=="&":
        #     r = "0x"+(message[1]+message[2])
        #     g = "0x"+(message[3]+message[4])
        #     b = "0x"+(message[5]+message[6])

        #     x=0
        #     if(len(message)>7):
	       #  	x=int(message[6]+message[7])
	       #  elif (len(message)>6):
        #         x=int(message[6])
        #     else:
        #         x = 0
            
        #     r = (eval(r)<<2)
        #     g = (eval(g)<<2)
        #     b = (eval(b)<<2)

        #     print("r"+str(r))
        #     print("g"+str(g))
        #     print("b"+str(b))
        #     print("\n")

        #     set_led(x, r, g, b)



        #write the data to the strip    
        update_leds(leds)

        # self.write_message("message received")

application = tornado.web.Application([
    (r"/", WebSocketHandler),
])

if __name__ == "__main__":
    #open the SPI device for writing
	if(not DEBUG):
	    spidev = file("/dev/spidev0.0", "wb")

	    #set the speed of the SPI bus, 5000000 == 5mhz    
	    #Magic number below is from spidev.h SPI_IOC_WR_MAX_SPEED_HZ
	    #TODO: can I reference this as a constant from termios?
	    fcntl.ioctl(spidev, 0x40046b04, array.array('L', [6000000]))

	    #setup our GPIO
	    GPIO.setwarnings(False)
	    GPIO.setmode(GPIO.BCM)
	    GPIO.setup(ENABLE_PIN, GPIO.OUT)
	    GPIO.setup(LATCH_PIN, GPIO.OUT)

	    #both pins low to start
	    GPIO.output(LATCH_PIN, 0)
	    GPIO.output(ENABLE_PIN, 0)

    #setup the initial LED state as a byte array of 4 bytes per module
    leds = bytearray(4 * NUM_LEDS)


#on sequence 
	bootSequence()
#end on sequence

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
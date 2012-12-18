#BeagleBone class, inspired from mrBBIO

import time


class BeagleBone(object):
    """Class to wrap beaglebone features"""

    def __init__(self):
        self.pinList = [] # needed for unexport()
        self.HIGH = "HIGH"
        self.LOW = "LOW"
        self.OUTPUT = "OUTPUT"
        self.INPUT = "INPUT"
        self.digitalPinDef = {
                    "P8.3":     38,
                    "P8.4":     39,
                    "P8.5":     34,
                    "P8.6":     35,
                    "P8.7":     66,
                    "P8.8":     67,
                    "P8.9":     69,
                    "P8.10":    68,
                    "P8.11":    45,
                    "P8.12":    44,
                    "P8.13":    23,
                    "P8.14":    26,
                    "P8.15":    47,
                    "P8.16":    46,
                    "P8.17":    27,
                    "P8.18":    65,
                    "P8.19":    22,
                    "P8.20":    63,
                    "P8.21":    62,
                    "P8.22":    37,
                    "P8.23":    36,
                    "P8.24":    33,
                    "P8.25":    32,
                    "P8.26":    61,
                    "P8.27":    86,
                    "P8.28":    88,
                    "P8.29":    87,
                    "P8.30":    89,
                    "P8.31":    10,
                    "P8.32":    11,
                    "P8.33":    9,
                    "P8.34":    81,
                    "P8.35":    8,
                    "P8.36":    80,
                    "P8.37":    78,
                    "P8.38":    79,
                    "P8.39":    76,
                    "P8.40":    77,
                    "P8.41":    74,
                    "P8.42":    75,
                    "P8.43":    72,
                    "P8.44":    73,
                    "P8.45":    70,
                    "P8.46":    71,
                    "P9.11":    30,
                    "P9.12":    60,
                    "P9.13":    31,
                    "P9.14":    50,
                    "P9.15":    48,
                    "P9.16":    51,
                    "P9.17":    5,
                    "P9.18":    4,
                    "P9.19":    13,
                    "P9.20":    12,
                    "P9.21":    3,
                    "P9.22":    2,
                    "P9.23":    49,
                    "P9.24":    15,
                    "P9.25":    117,
                    "P9.26":    14,
                    "P9.27":    115,
                    "P9.28":    113,
                    "P9.29":    111,
                    "P9.30":    112,
                    "P9.31":    110,
                    "P9.41":    20,
                    "P9.42":    7}

        self.pinMuxDef = {
                    "P8.3":     "gpmc_ad6",
                    "P8.4":     "gpmc_ad7",
                    "P8.5":     "gpmc_ad2",
                    "P8.6":     "gpmc_ad3",
                    "P8.7":     "gpmc_advn_ale",
                    "P8.8":     "gpmc_oen_ren",
                    "P8.9":     "gpmc_ben0_cle",
                    "P8.10":    "gpmc_wen",
                    "P8.11":    "gpmc_ad13",
                    "P8.12":    "gpmc_ad12",
                    "P8.13":    "gpmc_ad9",
                    "P8.14":    "gpmc_ad10",
                    "P8.15":    "gpmc_ad15",
                    "P8.16":    "gpmc_ad14",
                    "P8.17":    "gpmc_ad11",
                    "P8.18":    "gpmc_clk",
                    "P8.19":    "gpmc_ad8",
                    "P8.20":    "gpmc_csn2",
                    "P8.21":    "gpmc_csn1",
                    "P8.22":    "gpmc_ad5",
                    "P8.23":    "gpmc_ad4",
                    "P8.24":    "gpmc_ad1",
                    "P8.25":    "gpmc_ad0",
                    "P8.26":    "gpmc_csn0",
                    "P8.27":    "lcd_vsync",
                    "P8.28":    "lcd_pclk",
                    "P8.29":    "lcd_hsync",
                    "P8.30":    "lcd_ac_bias_en",
                    "P8.31":    "lcd_data14",
                    "P8.32":    "lcd_data15",
                    "P8.33":    "lcd_data13",
                    "P8.34":    "lcd_data11",
                    "P8.35":    "lcd_data12",
                    "P8.36":    "lcd_data10",
                    "P8.37":    "lcd_data8",
                    "P8.38":    "lcd_data9",
                    "P8.39":    "lcd_data6",
                    "P8.40":    "lcd_data7",
                    "P8.41":    "lcd_data4",
                    "P8.42":    "lcd_data5",
                    "P8.43":    "lcd_data2",
                    "P8.44":    "lcd_data3",
                    "P8.45":    "lcd_data0",
                    "P8.46":    "lcd_data1",
                    "P9.11":    "gpmc_wait0",
                    "P9.12":    "gpmc_ben1",
                    "P9.13":    "gpmc_wpn",
                    "P9.14":    "gpmc_a2",
                    "P9.15":    "gpmc_a0",
                    "P9.16":    "gpmc_a3",
                    "P9.17":    "spi0_cs0",
                    "P9.18":    "spi0_d1",
                    "P9.19":    "uart1_rtsn",
                    "P9.20":    "uart1_ctsn",
                    "P9.21":    "spi0_d0",
                    "P9.22":    "spi0_sclk",
                    "P9.23":    "gpmc_a1",
                    "P9.24":    "uart1_txd",
                    "P9.25":    "mcasp0_ahclkx",
                    "P9.26":    "uart1_rxd",
                    "P9.27":    "mcasp0_fsr",
                    "P9.28":    "mcasp0_ahclkr",
                    "P9.29":    "mcasp0_fsx",
                    "P9.30":    "mcasp0_axr0",
                    "P9.31":    "mcasp0_ahclkx",
                    "P9.41":    "xdma_event_intr0",
                    "P9.42":    "ecap0_in_pwm0_out"}

        self.analogPinDef = {
                    "P9.33":    "ain5",
                    "P9.35":    "ain7",
                    "P9.36":    "ain6",
                    "P9.37":    "ain3",
                    "P9.38":    "ain4",
                    "P9.39":    "ain1",
                    "P9.40":    "ain2"}

    def __del__(self):
        self.cleanup()
        pass
        
        
    def pinMode(self, pin, direction):
        """pinMode(pin, direction) opens (exports) a pin for use, sets the pinmux, and sets the direction"""
        if pin in self.digitalPinDef: # if we know how to refer to the pin:
            fw = file("/sys/class/gpio/export", "w")
            fw.write("%d" % (self.digitalPinDef[pin])) # write the pin to export to userspace
            fw.close()
            fileName = "/sys/class/gpio/gpio%d/direction" % (self.digitalPinDef[pin]) 
            fw = file(fileName, "w")
            if direction == self.INPUT: 
                fw.write("in") # write the diretion
                muxfile = file("/sys/kernel/debug/omap_mux/" + self.pinMuxDef[pin], "w") # open its mux file
                muxfile.write("2F") # put it into mode 7 input, no pulldown
                muxfile.close
            else:
                fw.write("out") # write the diretion
                muxfile = file("/sys/kernel/debug/omap_mux/" + self.pinMuxDef[pin], "w") # open its mux file
                muxfile.write("7") # put it into mode 7 output)
                muxfile.close
            fw.close()
            self.pinList.append(self.digitalPinDef[pin]) # Keep a list of exported pins so that we can unexport them.
        else: #if we don't know how to refer to a pin:
            print "pinMode error: Pin " + pin + " is not defined as a digital I/O pin in the pin definition."


    def digitalWrite(self, pin, status):
        """digitalWrite(pin, status) sets a pin HIGH or LOW"""
        if self.digitalPinDef[pin] in self.pinList: # check if we exported the pin in pinMode
            fileName = "/sys/class/gpio/gpio%d/value" % (self.digitalPinDef[pin])
            fw = file(fileName, "w") # open the pin's value file for writing
            if status == self.HIGH:
                fw.write("1") # Set the pin HIGH by writing 1 to its value file
            elif status == self.LOW:
                fw.write("0") # Set the pin LOW by writing 0 to its value file
            else:
                print "status unknown : possible in (" +self.HIGH+","+self.LOW+")"
            fw.close()
        else: # if we haven't exported the pin, print an error:
            print "digitalWrite error: Pin mode for " + pin + " has not been set. Use pinMode(pin, INPUT) first."
    
    def digitalRead(self, pin):
        """digitalRead(pin) returns HIGH or LOW for a given pin."""
        if self.digitalPinDef[pin] in self.pinList: # check if we exported the pin in pinMode
            
            fileName = "/sys/class/gpio/gpio%d/value" % (self.digitalPinDef[pin])
            fw = file(fileName, "r") # open the pin's value file for reading
            inData = fw.read()
            fw.close()
            if inData == "0\n": # a 0 means it's low
                return self.LOW
            if inData == "1\n": # a 1 means it's high
                return self.HIGH
            else:
                print "digitalRead error : expected value in {" + self.LOW +","+ self.HIGH +"} but unfortunately : " + str(inData) +" was found."
                return -1
        else: # if we haven't exported the pin, print an error (not working for some reason):
            print "digitalRead error: Pin mode for " + pin + " has not been set. Use pinMode(pin, OUTPUT) first."
            return -1;

    def analogRead(self, pin): #under construction!
        """analogRead(pin) returns analog value for a given pin."""
        if pin in self.analogPinDef:
            fileName = "/sys/devices/platform/omap/tsc/" + (self.analogPinDef[pin])
            fw = file(fileName, "r")
            data = fw.read()
            fw.close()
            return data
        else:
            print "analogRead error: Pin " + pin + " is not defined as an analog in pin in the pin definition."
            return -1;
    
    def pinUnexport(self, pin): # helper function for cleanup()
        """pinUnexport(pin) closes a pin in sysfs. This is usually 
        called by cleanup() when a script is exiting."""
        fw = file("/sys/class/gpio/unexport", "w")
        fw.write("%d" % (pin))
        fw.close()

    def cleanup(self):
        """    takes care of stepping through pins that were set with
        pinMode and unExports them. Prints result"""
        def find_key(dic, val):
            return [k for k, v in dic.iteritems() if v == val][0] # helper function for getting friendly name of pin
        print ""
        print "Cleaning up. Unexporting the following pins:",
        for pin in self.pinList: # for each pin we exported... 
            self.pinUnexport(pin) # ...unexport it...
            print find_key(self.digitalPinDef, pin), #...and print the friendly name of the pin


    def forceCleanup(self):
        """" try to unexport all pin in all lists"""
        #TODO
        pass
    

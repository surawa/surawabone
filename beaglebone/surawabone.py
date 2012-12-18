import beaglebone



class SurawaBone(beaglebone.BeagleBone):
    def __init__(self):
        beaglebone.BeagleBone.__init__(self)
        self.photoResistorPin="P9.39"

    
    def getPhotoresistorValue(self):
        return self.analogRead(self.photoResistorPin)
    pass

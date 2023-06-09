# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Define the TV class
class TV:
    # Attributes
    channel = 1
    volume = 1
    tv_on = False

    # Constructor
    def __init__(self, channel = 1, volume = 1):
        self.channel = channel
        self.volume = volume

    # Methods
    # Turn on the TV
    def turnOn(self):
        self.tv_on = True
    # Turn off the TV
    def turnOff(self):
        self.tv_on = False
    # Return the channel for the TV (1 to 120)
    def getChannel(self):
        return self.channel
    # Set a new channel for the TV
    def setChannel(self, channel):
        if self.tv_on and 1 <= channel <= 120:
            self.channel = channel
    # Get the volume level for the TV (1 to 7)
    def getVolume(self):
        return self.volume
    # Set a new volume level for the TV
    def setVolume(self, volume):
        if self.tv_on and 1 <= volume <= 7:
            self.volume = volume
    # Increase the channel number by 1
    def channelUp(self):
        if self.tv_on and self.channel < 120:
            self.channel += 1
    # Decrease the channel number by 1
    def channelDown(self):
        if self.tv_on and self.channel > 1:
            self.channel -= 1
    # Increase the volume level by 1
    def volumeUp(self):
        if self.tv_on and self.volume < 7:
            self.volume += 1
    # Decrease the volume level by 1
    def volumeDown(self):
        if self.tv_on and self.volume > 1:
            self.volume -= 1
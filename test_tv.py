# Import TV from tv_class.py
from tv_class import TV

# Define the TestTV function
def TestTV():

    # Create a TV object with channel 30 and volume level 3 (output)
    tv1 = TV(30, 3)
    # Turn on the TV1
    tv1.turnOn()
    # Print the current channel and volume level of the TV
    print("tv1's channel is", tv1.getChannel(), "and the volume level is", tv1.getVolume())

    # Create another TV object with channel 3 and volume level 2 (output)
    tv2 = TV(3, 2)
    # Turn on the TV2
    tv2.turnOn()
    # Print the current channel and volume level of the TV
    print("tv2's channel is", tv2.getChannel(), "and the volume level is", tv2.getVolume())

# Call the TestTV function to run the tests
TestTV()
# TV Class in Python
This Phyton program indicates a TV class that includes attributes like the __channel__, __volume__, and __power state__. Additionally, it describes how to operate various aspects of the TV, including turning it on and off, switching channels, and adjusting the volume. A __TestTV__ function is also defined to test the functionality of the TV class by creating two TV objects and executing different operations on them.
## Usage
Using Command Prompt:

- Open the Start menu and search for "Command Prompt".
- Click on "Command Prompt" to open the command prompt window.
- Use the cd command to navigate to the directory containing the script file. For example, if the script file is located in the "Documents" folder, type: cd Documents
- Type the command python script_name.py to run the script. Replace "script_name.py" with the actual name of the script file.
- Press Enter to run the script.
- The script will run and provides a basic TV class that allows for controlling a TV object's power, channel, and volume. 

Alternatively, you can also run the script using the Python IDLE environment:

- Open the Start menu and search for "Python".
- Click on "Python" to open the Python IDLE environment.
- Click on "File" at the top of the window and select "Open".
- Navigate to the directory containing the script file and select it.
- Click on "Run" at the top of the window and select "Run Module" or press the F5 key.
- The script will run and provides a basic TV class that allows for controlling a TV object's power, channel, and volume. 
## Code Explanation

<img width="500" alt="image" src="https://github.com/aieckxis/TV-Class-UML/assets/129574374/79525376-7ef8-48db-a3ca-9e8ba2db4d04">

The TV class has __three attributes__: __channel__, __volume__, and __tv_on__. The channel attribute, which is an integer and by default initialized to __1__, is used to identify the TV's current channel. The volume attribute, which is an integer that indicates the TV's current volume level, is also initially initialized to __1__. The __tv_on__ attribute, which has the boolean value of __False__ by default, indicates whether the TV is on or off. The class's methods provide access to and control over these attributes. The TV can be turned on and off, the channel can be changed, and the volume can be changed in the class using a variety of controls.

<img width="500" alt="image" src="https://github.com/aieckxis/TV-Class-UML/assets/129574374/517541b7-ac77-40a7-9ec6-bba47ac3611b">

The __constructor__ method initializes the TV object with a default channel number of __1__ and volume level of __1__. However, the user can override these default values by passing in new values when creating a TV object.

<img width="500" alt="image" src="https://github.com/aieckxis/TV-Class-UML/assets/129574374/fabc5ada-7e92-4261-8636-a3273ea97ff2">

The TV class has the following __methods__:

- __turnOn(self)__: a method that sets the __tv_on__ attribute to __True__, indicating that the TV is turned on.
- __turnOff(self)__: a method that sets the __tv_on__ attribute to __False__, indicating that the TV is turned off.
- __getChannel(self)__: a method that returns the current channel of the TV.
- __setChannel(self, channel)__: a method that sets the __channel__ attribute to the value passed as an argument, if the TV is turned on and the channel value is within the valid range of __1 to 120__.
- __getVolume(self)__: a method that returns the current volume level of the TV.

<img width="500" alt="image" src="https://github.com/aieckxis/TV-Class-UML/assets/129574374/29b17a05-37b3-4911-afcb-c2fd69ba0109">

- __setVolume(self, volume)__: a method that sets the __volume__ attribute to the value passed as an argument, if the TV is turned on and the volume level value is within the valid range of __1 to 7__.
- __channelUp(self)__: a method that increases the current channel number of the TV by __1__, if the TV is turned on and the channel is __less than 120__.
- __channelDown(self)__: a method that decreases the current channel number of the TV by __1__, if the TV is turned on and the channel is __greater than 1__.
- __volumeUp(self)__: a method that increases the current volume level of the TV by __1__, if the TV is turned on and the volume level is __less than 7__.
- __volumeDown(self)__: a method that decreases the current volume level of the TV by __1__, if the TV is turned on and the volume level is __greater than 1__.

<img width="500" alt="image" src="https://github.com/aieckxis/TV-Class-UML/assets/129574374/514363bf-518c-4daa-9672-a398cbe606f8">

Finally, the code defines a function called __TestTV__ that creates two instances of the TV class with different channel and volume levels, turns them on, and prints their current channel and volume level. The function is called to run the tests.

## Potential Improvements
- Add a mute method to mute/unmute the TV.
- Add error handling for when channel or volume level values are out of range.
- Add a method to set the TV to a specific channel number or volume level, rather than just increment/decrement them.
- Allow multiple TVs to be created and controlled independently.

## Conclusion
This Phyton program offers a simple implementation of a TV class and enables basic functionality to control a TV object, such as on/off, channel changing, and volume adjustment. To make the TV class more flexible and adaptable, additional functionality could be added

# PhilipsHueAPI
Python3 controller for the Philips Hue Smart Lightbulb

The attached Python file contains a TKINTER GUI that sends REST API requests to the Philips Hue Smart Light Bulb. You need to know the IP address of the smart ligth bulb and be on the same LAN as the light bulb. Please note that if you attempt to use the smart phone application and this software at the same time, the light bulb will become delayed and slow. 

Standards I found for the Philips Hue smart light bulb through wireshark: 
PORT: 38899
UTF-8 Encoded JSON request with the body of the packet containing one of two things:

1. {{"method":"setPilot","id":14,"params":{{"r":{VALUE},"g":{VALUE},"b":{VALUE},"c":{VALUE},"w":{VALUE},"orig":"ios"}}}} #all the value included here are between 1 and 255. 

2.  {{"params":{{"dimming":{VALUE},"orig":"ios"}},"id":36,"method":"setPilot"}} # the value of the brightness value here should be between 1 and 100. 

# Satellite Networking
Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?
# Challange
You download a [zip](https://github.com/sebastianbeck/ctf/blob/master/google2019/Challanges/Satellite%20Networking/768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf.zip) with one executable and a readme file.
I start the executable
```
Hello Operator. Ready to connect to a satellite?
Enter the name of the satellite to connect to or 'exit' to quit
```
and you need to enter the name of the satellite you want to connect to. in the description the satellite is called Osmium. So i enter that.
```
Establishing secure connection to osmium
 satellite...
Welcome. Enter (a) to display config data, (b) to erase all data or (c) to disconnect
```
If I type option a, i get this answer.
```
Username: brewtoot password: ********************	166.00 IS-19 2019/05/09 00:00:00	Swath 640km	Revisit capacity twice daily, anywhere Resolution panchromatic: 30cm multispectral: 1.2m	Daily acquisition capacity: 220,000km²	Remaining config data written to: https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
```
In the google doc file is a base64 encrypted strings which. I decrypt it and the plaintext is:
```
Logins for home and work computer:
Username: webortto
Password: totally-not-a-flag-keep-sniffing
```
I also tried to reserve the binary and found this, which led to nothing
```
CTF{\S{40}}GOTRACEBACKHOSTALIASESIdeographicInstCaptureInstRuneAnyLOCALDOMAINNew_Tai_LueOld_PersianPau_Cin_HauRES_OPTIONSSignWr
```
So I took a break and then the note in the password came to my mind. I started Wireshark and sniffed the traffic and under the asterisk hid the following text. I need to read the hints more conscious.
```
CTF{4efcc72090af28fd33a2118985541f92e793477f}
```

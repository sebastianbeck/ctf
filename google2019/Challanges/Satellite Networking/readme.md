# Satellite Networking
Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?
# Challange
You download a [zip](https://github.com/sebastianbeck/ctf/blob/master/google2019/Challanges/Satellite%20Networking/768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf.zip) with one executable and a readme file.

First we need to get the satellite name which is osmium
if you connect to the server you get 3 options
Enter (a) to display config data, (b) to erase all data or (c) to disconnect

a gives back this
Logins for home and work computer:
Username: webortto
Password: totally-not-a-flag-keep-sniffing

i found the following string in the connect to sta file

CTF{\S{40}}GOTRACEBACKHOSTALIASESIdeographicInstCaptureInstRuneAnyLOCALDOMAINNew_Tai_LueOld_PersianPau_Cin_HauRES_OPTIONSSignWr

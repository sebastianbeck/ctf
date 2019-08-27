## Beginners Quest
![Google CTF Overview](https://github.com/sebastianbeck/ctf/blob/master/google2019/src/img/googlectf.png?raw=true "Google CTF Overview")

Welcome to Beginners Quest! A few notes before your embark:
*There are multiple paths that lead through different challenges, to 4 different endings.
*Only after solving the most difficult challenges do you receive the "winning" ending.
*Save your flags in case you want to try different branches later, after reaching an ending.
*Three challenges have two flags, each taking you towards a different path.
*See the map for an overview of the challenges and paths.
*Problems vary in both difficulty and time to solve (ie. some might be easier but take more time to do the work for the flag.) You can go back to make different choices if you don't like what is ahead.
## Invitation
You are a simple life form, exiled from your home planet and in search of a new place to call home. The ruling came fast. Your taste in music was deemed to be far too "out-there-man" for anyone to possibly associate with you anymore. You were given 60 revolutions of Xenon around Fir to leave and never return. Gather whatever possessions and leave. You find your parents music collection, oddly in it is a golden disc labelled "Property of NASA, if lost please return to: EVNJAKL 1600 Ampitheatre Parkway Mountain View California." The music on the disc was uncovered a while back and was not very interesting. This weird language that said something about "Peace, love and rock and roll. Also we're having a really cool party tonight, so for whoever is out there, bring a friend and come along! Co-ordinates enclosed." On the back the words "Draft, do not distribute or load onto probe" written in big red letters. That could mean anything.

You'll go, since you have nowhere else to go. But you'll be careful. You well know to learn all you can about alien beings before making contact. They could be hostile, or listen to boring music. Time is slipping away fast, you race aboard the nearest ObarPool Spaceship. But you've never driven one... what next genius?

## Enter Space-Time Coordinates Misc
Ok well done. The console is on. It's asking for coordinates. Beating heavily on the console yields little results, but the only time anything changes on your display is when you put in numbers.. So what numbers are you going to go for?  You see the starship's logs, but is there a manual? Or should you just keep beating the console?

## Solution
You can download a [zip](https://github.com/sebastianbeck/ctf/blob/master/google2019/src/challenges/00c2a73eec8abb4afb9c3ef3a161b64b451446910535bfc0cc81c2b04aa132ed.zip). In the zip are two files, one log file and one executable. The URL to the challange contains *reversing-rand2*. This suggests that we have to do some reverse engineering. I openend the file in EDB and found the flag by scrolling through it. 
```
Flag: CTF{welcome_to_googlectf}
```
## Arrival & Reconnaissance
Having successfully figured out this "coordinate" problem. The ship lurches forward violently into space. This is one of the moments when you realize that some kind of thought or plan would have been good, but typically for you and how you found yourself in this situation, you didn't think too much before acting. Only the stars themselves know where you'll end up.

After what seems like an eternity, or at least one full season of "Xenon's Next Top Galactic Overlord" you arrive in a system of 9 planetary bodies, though one of them is exceptionally small. You nostalgically remember playing explodatoid with your friends and hunting down planets like this. But this small planet registers a hive of noise and activity on your ships automated scanners. There's things there! Billions upon trillions of things, moving around, flying, swimming, sliding, falling.

Of particular interest may be the insect-like creatures flying around this planet, uniformly. One has the words "Osmium Satellites" written on it. Maybe this is a starting point to get to know what's ahead of you
## Satellite Networking
Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?
## Solution
You download a [zip](https://github.com/sebastianbeck/ctf/blob/master/google2019/src/challenges/00c2a73eec8abb4afb9c3ef3a161b64b451446910535bfc0cc81c2b04aa132ed.zip) with one executable and a readme file.
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
So I took a break and then the note in the password came to my mind. I started Wireshark and sniffed the traffic and under the asterisk when you chose the option (a) hid the following text. I need to read the hints more conscious.
```
CTF{4efcc72090af28fd33a2118985541f92e793477f}
```

## Your Choice!
Having found the information you were looking for, while detailed, it presents you with an interesting dilemma. There is a network of "computers" not completely dissimilar to your computrator-machine on your ship. You find yourself in possession of the credentials of an individual on the planet named "SarahH." Great, with these you can get right into the secret world of an earthling without them knowing you're there. You access "SarahH home network," to find two computers: "work" and "home." Not knowing what either of these are, you have to make a decision.

## Home Computer forensics
Blunderbussing your way through the decision making process, you figure that one is as good as the other and that further research into the importance of Work Life balance is of little interest to you. You're the decider after all. You confidently use the credentials to access the "Home Computer."

Something called "desktop" presents itself, displaying a fascinating round and bumpy creature (much like yourself) labeled  "cauliflower 4 work - GAN post."  Your 40 hearts skip a beat.  It looks somewhat like your neighbors on XiXaX3.   ..Ah XiXaX3... You'd spend summers there at the beach, an awkward kid from ObarPool on a family vacation, yearning, but without nerve, to talk to those cool sophisticated locals.

So are these "Cauliflowers" earthlings? Not at all the unrelatable bipeds you imagined them to be.  Will they be at the party?  Hopefully SarahH has left some other work data on her home computer for you to learn more.

## Solution
For the third thime I download a zip file. I can't upload it here because it's to big. It contains a .ntfs file.
I have to mount the ntfs partition.
```
mkdir /mnt/ntfs1
mount -t ntfs /path-to-file/family.ntfs /mnt/ntfs1

```
I search through the partition and under /mnt/ntfs1/Users/Family/Documents I find a document called credentials.txt which cotains.
```
I keep pictures of my credentials in extended attributes.
```
Therefore I need to search for extenend attributes. I stumbled on this blog https://medium.com/@stdout_/accessing-ntfs-extended-attributes-from-linux-f79552947981 
I downloaded the script which was mentioned in the blog from https://github.com/siftgrab/siftgrab/blob/master/ermount.sh 
and mounted the file. 
Afterwards I run the following command in the path /mnt/ntfs1/Users/Family and found out that the crednetials.txt file had an alternate datastream. I knew them from testing how to bypass AppLocker.
```
getfattr -Rn ntfs.streams.list .
```
Now I had to extract the file to a jpg or png file.
```
cat Documents/credentials.txt:FILE0 > cred.png
```
In the picture was the flag
```
CTF{congratsyoufoundmycreds}
``` 

## Government Agriculture Network web (Path Home Network)
Well it seems someone can't keep their work life and their home life separate. You vaguely recall on your home planet, posters put up everywhere that said "Loose Zips sink large commercial properties with a responsibility to the shareholders." You wonder if there is a similar concept here.

Using the credentials to access this so-called Agricultural network, you realize that SarahH was just hired as a vendor or contract worker and given access that was equivalent. You can only assume that Vendor/Contractor is the highest possible rank bestowed upon only the most revered and well regarded individuals of the land and expect information and access to flow like the Xenovian acid streams you used to bathe in as a child.

The portal picture displays that small very attractive individual whom you instantly form a bond with, despite not knowing. You must meet this entity! Converse and convince them you're meant to be! After a brief amount of time the picture shifts into a biped presumably ingesting this creature! HOW DARE THEY. You have to save them, you have to stop this from happening. Get more information about this Gubberment thing and stop this atrocity.

You need to get in closer to save them - you beat on the window, but you need access to the cauliflower's host to rescue it.
https://govagriculture.web.ctfcompetition.com/ 

## Solution 
Here you get an URL to a website: https://govagriculture.web.ctfcompetition.com/

I didn't really try this one cause I don't have a lot of expierence with web based challanges. 
I found this write up.https://github.com/AidanFray/CTF_Writeups/tree/master/2019/GoogleCTF/BeginnerQuests/GovernmentAgricultureNetwork
I need to learn alot about Webbased Challanges.

## STOP GAN bof (Path Home Network)
Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two separate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.
## Solution normal flag
After I had to look up the solution for the other challenge, I hope to solve this without help. 
I have never tried a bufferoverflow challenge before so let's see what I can learn.

I can download a [zip](https://github.com/sebastianbeck/ctf/blob/master/google2019/src/challenges/4a8becb637ed2b45e247d482ea9df123eb01115fc33583c2fa0e4a69b760af4a.zip) file which contains a ELF32 bit executable and a .c file with source code.
You can also connect to the host buffer-overflow.ctfcompetition.com 1337. 
First I take a look at the source code where I can see that the input is limited to 256.
The first input needs to be run, and afterwards it waits for another input which we may be able to overflow?.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/**
 * 6e: bufferflow triggering segfault  - binary, compile with:
 * gcc /tmp/console.c -o /tmp/console -static -s
 *
 * Console allows the player to get info on the binary.
 * Crashing bof will trigger the 1st flag.
 * Controlling the buffer overflow in bof will trigger the 2nd flag.
 */

int main() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
  char inputs[256];
  printf("Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.\n Bonus flag for controlling the crash.\n");
  while(1) {
    printf("\nConsole commands: \nrun\nquit\n>>");
    if (fgets(inputs, 256, stdin) == NULL) {
      exit(0);
    }
    printf("Inputs: %s", inputs);
    if ( strncmp(inputs, "run\n\0", 256) == 0 ) {
      int result = system("/usr/bin/qemu-mipsel-static ./bof");
      continue;
    } else if ( strncmp(inputs, "quit\n\0", 256) == 0 ) {
      exit(0);
    } else {
      puts("Unable to determine action from your input");
      exit(0);
    }
  }
  return 0;
}
```
Before I start to overthink again I will try the easy thing.
First I connect to the host and create a string which is larger then 256
```
python -c "print 'x' * 300"
nc buffer-overflow.ctfcompetition.com 1337
```
Afterwards i type run and copy the 300 x into the input and the flag appears
```
Flag: CTF{Why_does_cauliflower_threaten_us}
````
## Solution Bonus Flag 

## Work Computer sandbox 
With the confidence of conviction and decision making skills that made you a contender for Xenon's Universal takeover council, now disbanded, you forge ahead to the work computer.   This machine announces itself to you, surprisingly with a detailed description of all its hardware and peripherals. Your first thought is "Why does the display stand need to announce its price? And exactly how much does 999 dollars convert to in Xenonivian Bucklets?" You always were one for the trivialities of things.

Also presented is an image of a fascinating round and bumpy creature, labeled "Cauliflower for cWo" - are "Cauliflowers" earthlings?  Your 40 hearts skip a beat - these are not the strange unrelatable bipeds you imagined earthings to be.. this looks like your neighbors back home. Such curdley lobes. Will it be at the party?

SarahH, who appears to be  a programmer with several clients, has left open a terminal.  Oops.  Sorry clients!  Aliens will be poking around attempting to access your networks.. looking for Cauliflower.   That is, *if* they can learn to navigate such things.

## Solution normal flag
We need to connect to readme.ctfcompetition.com 1337 via telnet.
The box is restricted as  uname -a returned something with Linux Jail. I thought I need to break out of the chroot which was not the case. I couldn't find the solution by myself so i found this write up. 
https://github.com/AidanFray/CTF_Writeups/tree/master/2019/GoogleCTF/BeginnerQuests/WorkComputer

I learned about https://gtfobins.github.io which will be very helpful in the future. 
Another way to solve it would have been with to use of tar -c README.flag

```
FLAG: CTF{4ll_D474_5h4ll_B3_Fr33}
```
## Solution bonus flag
There is a a solution to the bonus flag in the link above.

## FriendSpaceBookPlusAllAccessRedPremium.com reversing
Having snooped around like the expert spy you were never trained to be, you found something that takes your interest: "Cookie/www.FriendSpaceBookPlusAllAccessRedPremium.com"  But unbeknownst to you, it was only the  700nm Wavelength herring rather than a delicious cookie that you could have found.   It looks exactly like a credential for another system.  You find yourself in search of a friendly book to read.

Having already spent some time trying to find a way to gain more intelligence... and learn about those fluffy creatures, you (several)-momentarily divert your attention here.  It's a place of all the individuals in the world sharing large amounts of data with one another. Strangely enough, all of the inhabitants seem to speak using this weird pictorial language. And there is hot disagreement over what the meaning of an eggplant is.

But not much Cauliflower here.  They must be very private creatures.  SarahH has left open some proprietary tools, surely running this will take you to them.  Decipher this language and move forth!

## Solution 
I need to download a [zip](https://github.com/sebastianbeck/ctf/blob/master/google2019/src/challenges/775e97ff94e7dfe79293b62abed7e1ad17cdc6ebc82c4873cdca201c40569624.zip) file which containts a python and a executable file.
http://www.bleleet.kr/2019-googlectf-friendspacebookplusallaccessredpremiumcom.html 



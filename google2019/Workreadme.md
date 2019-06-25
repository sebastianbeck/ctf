# Work Computer Sandbox
With the confidence of conviction and decision making skills that made you a contender for Xenon's Universal takeover council, now disbanded, you forge ahead to the work computer.   This machine announces itself to you, surprisingly with a detailed description of all its hardware and peripherals. Your first thought is "Why does the display stand need to announce its price? And exactly how much does 999 dollars convert to in Xenonivian Bucklets?" You always were one for the trivialities of things.

Also presented is an image of a fascinating round and bumpy creature, labeled "Cauliflower for cWo" - are "Cauliflowers" earthlings?  Your 40 hearts skip a beat - these are not the strange unrelatable bipeds you imagined earthings to be.. this looks like your neighbors back home. Such curdley lobes. Will it be at the party?

SarahH, who appears to be  a programmer with several clients, has left open a terminal.  Oops.  Sorry clients!  Aliens will be poking around attempting to access your networks.. looking for Cauliflower.   That is, *if* they can learn to navigate such things.

# Challange
We need to connect to readme.ctfcompetition.com 1337 via telnet.
The box is restricted as  uname -a returned something with Linux Jail. I thought I need to break out of the chroot which was not the case. I couldn't find the solution by myself so i found this write up. 
https://github.com/AidanFray/CTF_Writeups/tree/master/2019/GoogleCTF/BeginnerQuests/WorkComputer

I learned about https://gtfobins.github.io which will be very helpful in the future. 
I another way would have been to use tar -c README.flag
>Main Flag
>
>The challenge starts by providing us with a command prompt. However, is immediately apparent that commands are missing and you're unable to cat out files.
>
>Listing out /usr/bin or /bin (where system binaries are stored) allows us to view what we can execute.
>Using this information alongside the beautiful website gtfobins. I am able to search for binaries that allow us to read a file.
>After a little trial and error I come across the command fold that is used to wrap text to fit a specified width.
>This, however, allows us to read local files! Taking the code snippet from gtfobins
>
>LFILE=file_to_read
>
>fold -w99999999 "$LFILE"
>
>We're able to print the READEME.flag to get the first flag (-w is just to specify the character width)
>
>fold -w 1000 README.flag
>
>FLAG:
>
>CTF{4ll_D474_5h4ll_B3_Fr33}
>

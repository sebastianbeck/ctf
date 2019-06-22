# Home Computer forensics
Blunderbussing your way through the decision making process, you figure that one is as good as the other and that further research into the importance of Work Life balance is of little interest to you. You're the decider after all. You confidently use the credentials to access the "Home Computer."

Something called "desktop" presents itself, displaying a fascinating round and bumpy creature (much like yourself) labeled  "cauliflower 4 work - GAN post."  Your 40 hearts skip a beat.  It looks somewhat like your neighbors on XiXaX3.   ..Ah XiXaX3... You'd spend summers there at the beach, an awkward kid from ObarPool on a family vacation, yearning, but without nerve, to talk to those cool sophisticated locals.

So are these "Cauliflowers" earthlings? Not at all the unrelatable bipeds you imagined them to be.  Will they be at the party?  Hopefully SarahH has left some other work data on her home computer for you to learn more.
# Challange
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

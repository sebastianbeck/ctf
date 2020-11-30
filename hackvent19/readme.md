
# Hackvent 2019

## Day 1

### Challenge

I got this little image, but it looks like the best part got censored on the way. Even the tiny preview icon looks clearer than this! Maybe they missed something that would let you restore the original content?

![Flag1](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag1/1.jpg)


### Solution

As the text suggests we got to extract the thumbnail picture. Exiftool is capable of doing so. Run this command. 

```bash
exiftool -b -ThumbnailImage my_image.jpg > my_thumbnail.jpg
```

Open the file and scan the QR Code. The Flag is:

```bash
HV19{just-4-PREview!}

```

## Day 2

### Challenge

Today we give away decorations for your Christmas tree. But be careful and do not break it.

### Solution

First, I download the file and unzip it. It is an stl(3D Image) file which I open in a web viewer. It is a Christmas bulb. I play around with the different views and see there is a QR code inside the bulb. The web viewer is very limited, so I downloaded the FreeCAD Software and again play around with different view settings and got to this picture.

![Flag2_1](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag2/Flag2_1.png)

I make a screenshot and use gimp to edit the screenshot. After some work I get a functional QR Code.

![Flag2_2](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag2/Flag2_2.png)

The Flag is:
```
HV19{Cr4ck_Th3_B411!}
```

## Day 3

### Challenge

```
$HODOR: hhodor. Hodor. Hodor!?  = `hodor?!? HODOR!? hodor? Hodor oHodor. hodor? , HODOR!?! ohodor!?  dhodor? hodor odhodor? d HodorHodor  Hodor!? HODOR HODOR? hodor! hodor!? HODOR hodor! hodor? ! 

hodor?!? Hodor  Hodor Hodor? Hodor  HODOR  rhodor? HODOR Hodor!?  h4Hodor?!? Hodor?!? 0r hhodor?  Hodor!? oHodor?! hodor? Hodor  Hodor! HODOR Hodor hodor? 64 HODOR Hodor  HODOR!? hodor? Hodor!? Hodor!? .

HODOR?!? hodor- hodorHoOodoOor Hodor?!? OHoOodoOorHooodorrHODOR hodor. oHODOR... Dhodor- hodor?! HooodorrHODOR HoOodoOorHooodorrHODOR RoHODOR... HODOR!?! 1hodor?! HODOR... DHODOR- HODOR!?! HooodorrHODOR Hodor- HODORHoOodoOor HODOR!?! HODOR... DHODORHoOodoOor hodor. Hodor! HoOodoOorHodor HODORHoOodoOor 0Hooodorrhodor HoOodoOorHooodorrHODOR 0=`;
hodor.hod(hhodor. Hodor. Hodor!? );
```

### Solution
I found the site http://www.hodor-lang.org/, which was made before S8.
I installed the required software.
```
sudo apt-get install nodejs
sudo apt-get install npm
npm install -g hodor-lang 
```
Afterwards I  copied the hodor code into a file and executed it.
```
hodor flag3.hd 
HODOR: \-> flag3.hd
Awesome, you decoded Hodors language! 

As sis a real h4xx0r he loves base64 as well.

SFYxOXtoMDFkLXRoMy1kMDByLTQyMDQtbGQ0WX0=

```
Just encrypt the bas64 string and the flag is:
```
HV19{h01d-th3-d00r-4204-ld4Y}
``` 

## Day 4

### Challenge

Santa released a new password policy (more than 40 characters, upper, lower, digit, special).
The elves can't remember such long passwords, so they found a way to continue to use their old (bad) password:

```
merry Christmas geeks
```

### Solution

I get a zip file which contains an ahk file. ahk is an automation scripting language, therefore I download the compiler and compile it.
I enter the string *merry christmas geeks* (Don't type too fast) and you get the flag.

```
HV19{R3memb3r, rem3mber - the 24th 0f December}
```

## Day 5

### Challenge 

To handle the huge load of parcels Santa introduced this year a parcel tracking system. He didn't like the black and white barcode, so he invented a more solemn barcode. Unfortunately the common barcode readers can't read it anymore, it only works with the pimped models Santa owns. Can you read the barcode?

![Flag5_1](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag5/Flag5_1.png)

### Solution

I tried a lot of things on this one. Each block has a different color and in the description the color is mentioned. I write a script which reads all the color codes in hex and  manually search for the hex values of HV19{ (48 56 31 39 7b). I find the codes at the last 2 places. I modify the script to only print the last two places and get this string.

```
583859494f46305a50345338485631397b4431666963756c745f746f5f6733745f615f5350545f5233616465727d53313039304f4d5a453045334e46503645
``` 

Convert this to ASCII and you get the flag

```
X8YIOF0ZP4S8HV19**{D1ficult_to_g3t_a_SPT_R3ader}**S1090OMZE0E3NFP6E
```

The messy script I wrote for it.

```python
#!/usr/bin/python
from PIL import Image

def rgb2hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)
def rgb2hexmod(b):
    return '{:02x}'.format(b)
img = Image.open('Flag5_1.png')  
pixels = img.convert('RGBA').load()
width, height = img.size
f = open("demofile01.txt", "a")
oldhexval='ffffff '
for x in range(width):
        r, g, b, a = pixels[x, 1]
        hexval= '%s' % (rgb2hexmod(b))
        if hexval!='ff' and hexval!=oldhexval:
            f.write(hexval)
            oldhexval = hexval
f.close
``` 

## Day 6

### Challenge

![Flag6_1](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag6/Flag6_1.png)

### Solution

I made a screenshot of the Challenge that you can see all the italic character. I guess this is bacon cipher challenge.
I copy the html code of the paragraph. I use crtl+h to remove all <em></em> Tags and capitalizes the letters.
After that I copy the text in a bacon decipher and change the alphabet to complete. I get this text with the flag

```
SANTALIKESHISBACONBUTALSOTHISBACONTHEPASSWORDISHVXBACONCIPHERISSIMPLEBUTCOOLXREPLACEXWITHBRACKETSANDUSEUPPERCASEFORALLCHARACTERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

HV{BACONCIPHERISSIMPLEBUTCOOL}
```

## Day 7

### Challenge

Santa is prototyping a new gadget for his sledge. Unfortunately it still has some glitches, but look for yourself.
There is a video with 8 LEDs in different colors.

### Solution

I see 8 lights and guess that this is binary.
I use the following script to extract each frame of the video

```python
import cv2
vidcap = cv2.VideoCapture('Flag7.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
```

I go thorugh the frames write them down in binary and translate it. The flag is:

```
HV19{1m_als0_w0rk1ng_0n_a_r3m0t3_c0ntr0l}
``` 

## Day 8

### Challenge

You hacked into the system of very-secure-shopping.com and you found a SQL-Dump with $$-credit cards numbers. As a good hacker you inform the company from which you got the dump. The managers tell you that they don't worry, because the data is encrypted.

Dump-File: dump.zip

### Goal

Analyze the "Encryption"-method and try to decrypt the flag.

### Hints

CC-Numbers are valid ones.
Cyber-Managers often doesn't know the difference between encoding and encryption.

### Solution

I open the sql dump and there is a table with CC info and a table with the flag. The CC strings and the flag is encrypted or decoded and look like this.
```
CC string:
QVXSZUVY\ZYYZ[a
QOUW[VT^VY]bZ
SPPVSSYVV\YY_\\]	
RPQRSTUVWXYZ[\]^
QTVWRSVUXW[_Z`\b
Flag string:
SlQRUPXWVo\Vuv_n_\ajjce
```
From the encrypted strings I guess the original is translated to dec, then a number is added and afterwards it's changed back to ascii. The letters get higher towards the end and therefore I guess the number which is subtracted increases by some amount. 
There is the luhn algorithm which validates the CC.  
I wrote this script which helped me to get the flag.
```python

def checkcc(ccnumber, l):
    sum = 0
    revccnumber = ccnumber[::-1]
    for i in range(l):
        if i%2 == 0:
            sum = sum + int(revccnumber[i])
        else:
            if int(revccnumber[i])*2 < 10: 
                sum = sum + (int(revccnumber[i])*2)
            else:
                sum = sum + int((int(revccnumber[i])*2/10))
                sum = sum + (int(revccnumber[i])*2%10)
    if(sum%10==0): #CC is valid
        print("valid")
        
decoded= ['QVXSZUVY\ZYYZ[a', 'QOUW[VT^VY]bZ_', 'SPPVSSYVV\YY_\\]', 'RPQRSTUVWXYZ[\]', r'QTVWRSVUXW[_Z`\b', r'SlQRUPXWVo\Vuv_n_\ajjce'] #]
for x in decoded:
    i=30 #30 intersant
    z=""
    for y in x:
        y = ord(y)-i
        y = chr(y)
        i=i+1
        z=z+y
    print(z)
    checkcc(z, len(z))
```

The flag is:

```
HV19{5M113-420H4-KK3A1-19801}
```

## Day 9

### Challenge

Visiting the following railway station has left lasting memories.

Santas brand new gifts distribution system is heavily inspired by it. Here is your personal gift, can you extract the destination path of it?

### Hints
- it starts with a single pixel
- centering is hard

### Solution

N/A
## Day 10

### Challenge
The flag is right, of course

### Resources
[Flag10](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag10/10.zip)

### Solution
I executed the binary and tried some inputs. Afterwards I ran it with ltrace, scrolled through it and got the flag.

```
HV19{Sh3ll_0bfuscat10n_1s_fut1l3}
```

## Day 11

### Challenge
The elves created an API where you get random jokes about santa.
Resources

### Resources

Go and try it here: http://whale.hacking-lab.com:10101

### Solution

I use the API Doc to create an account and tested some stuff but that doesn't help.
I try to create an admin account with different options and then I get this response.

```
curl -s -X POST -H 'Content-Type: application/json' http://whale.hacking-lab.com:10101/fsja/register --data '{"username":"gfdsa", "password": "passwordpassword", "admin":true}'

Unrecognized field "admin" (class ch.dkuhn.hv19.fsja.model.User), not marked as ignorable (3 known properties: "password", "platinum", "username"])
at [Source: org.glassfish.jersey.message.internal.ReaderInterceptorExecutor$UnCloseableInputStream@27a6c4c6; line: 1, column: 63] (through reference chain: ch.dkuhn.hv19.fsja.model.User["admin"])

```

I create a user with "paltinum"=true and login with that user. I get the flag with the next joke.

```
curl -s -X POST -H 'Content-Type: application/json' http://whale.hacking-lab.com:10101/fsja/register --data '{"username":"gfdsa", "password": "passwordpassword", "platinum":true}'

curl -s -X POST -H 'Content-Type: application/json' http://whale.hacking-lab.com:10101/fsja/login --data '{"username":"gfdsa", "password": "passwordpassword"}'

curl -X GET "http://whale.hacking-lab.com:10101/fsja/random?token=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiZ2Zkc2EiLCJwbGF0aW51bSI6dHJ1ZX0sImV4cCI6MTU3NjA1Njk2OC42OTQwMDAwMDB9.ESixd9xDQET3SYe418W7Uc5UYPQvHAg42WxWnyY7oIQ"

{"joke":"Congratulation! Sometimes bugs are rather stupid. But that's how it happens, sometimes. Doing all the crypto stuff right and forgetting the trivial stuff like input validation, Hohoho! Here's your flag: HV19{th3_cha1n_1s_0nly_as_str0ng_as_th3_w3ak3st_l1nk}","author":"Santa","platinum":true}
```

## Day 13

### Challenge

Switzerland's national security is at risk. As you try to infiltrate a secret spy facility to save the nation you stumble upon an interesting looking login portal.
Can you break it and retrieve the critical information?

### Resources

Facility: http://whale.hacking-lab.com:8888/trieme/
[HV19.13-NotesBean.java.zip](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag13/HV19.13-NotesBean.java.zip)

### Solution

I analyzed the website and the java code. The goal is to set the isAdmin boolean to true. The code uses a patriciatrie structure and the isAdmin is true if the *"auth_token_4835989* is not in the patricia trie. So we need to find a way to delete or change that with the input of the homepage. I find this site https://issues.apache.org/jira/browse/COLLECTIONS-714  and with the input *auth_token_4835989\u0000* we get the flag: 
```
HV19{get_th3_chocolateZ}
```
## Day 14

### Introduction

Let's play another little game this year. Once again, I promise it is hardly obfuscated.

### Resources

[original.pl](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag14/original.pl)

### Solution

On my first attempt I tried to remove the collision control and beat the game in "god mode" but I wasn't patient enough for that. By analyzing, I understood the script more and more and figured out where the flag is generated and how to print that out. 
I change the script that it prints out the flag at the start. I edited the following:

```perl
#The Function T
($T=sub{$t=$vMnyQdAkfgIIik->#FOO
createText($PMMtQJOcHm8eFQfdsdNAS20->()%600,$PMMtQJOcHm8eFQfdsdNAS20->()%440,#Perl!!
"-text"=>$txt=$d28Vt03MEbdY0->(),"-$y"=>$z);print $txt;})->();

#and in the loop
$p[0]+1,$p[1]+1)||[])->[0];$q==$t&&$T->();$T->();
```

Here the modified file:
[godmode.pl](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag14/godmode.pl)
The Flag is:

```
HV19{s@@jSfx4gPcvtiwxPCagrtQ@,y^p-za-oPQ^a-z\x20\n^&&s[(.)(..)][\2\1]g;s%4(...)%"p$1t"%ee}
```

## Day 15

### Challenge

The Elves are working very hard.
Look at http://whale.hacking-lab.com:2080/ to see how busy they are.

### Hints

Due to stability problems, time is extended for +24h
1) When you have the webpage open and the counter is running (for your clientid), the challenge works for you
2) Due to server instability there are websockets hangups. Reload of webpage (or restart of your script) will help and lead to 1)
3) There are possibilities to crash the server with dedicated client-ids, eg. very long client-ids. For this, the length of client is now limited to 30. For longer client-ids no count nor flag is published.

### Solution
N/A
## Day 16

### Challenge

Santa has coded a simple project for you, but sadly he removed all the operations.
But when you restore them it will print the flag!

### Resources

HV19.16-b0rked.zip

### Solution

We get a calculator which isn't working properly. It seems like we have to recreate the operations in the program. I download and install the x32dbg.
I open the .exe in x3dbg and run the program with **F9** and at the top of the program we can see that we are in the borked module.
![pic1](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag16/pic1.png)

After that i search for intermodular calls and set breakpoints. In this challenge it is the **SetDigItemInt**.
![pic2](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag16/pic2.png)

I look what happens there and figure out that above it looks for the operator and then jumps to different sections.
I set breakpoints there with **F2** and run the exe again.
![pic3](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag16/pic3.png)

I step through the program with **F7** and then it jumps to some strange place with a lot of nops. It seems like here once was the operation.
![pic4](https://github.com/sebastianbeck/ctf/blob/master/hackvent19/flag16/pic4.png)

It pushes the value of ebp+8 to eax. EBP+8 is the second value we entered in the calc. With this site i find out how to add two numbers. https://c9x.me/x86/html/file_module_x86_id_5.html.I add the operation and run the program again. The flag looks better. I repeat the steps for Substition and multiplication.
idiv is special so we need to push edx to the stack, cause saves the "Rest" in edx and then pop it again. 
https://www.felixcloutier.com/x86/idiv
The changed code looks like this:
```
004015B6 | C8 0000 00               | enter 0,0                                       |
004015BA | 8B45 08                  | mov eax,dword ptr ss:[ebp+8]                    |
004015BD | 0345 0C                  | add eax,dword ptr ss:[ebp+C]                    |
004015C0 | C9                       | leave                                           |
004015C1 | C2 0800                  | ret 8                                           |
004015C4 | C8 0000 00               | enter 0,0                                       |
004015C8 | 8B45 08                  | mov eax,dword ptr ss:[ebp+8]                    |
004015CB | 8B4D 0C                  | mov ecx,dword ptr ss:[ebp+C]                    |
004015CE | 2BC1                     | sub eax,ecx                                     |
004015D0 | C9                       | leave                                           |
004015D1 | C2 0800                  | ret 8                                           |
004015D4 | C8 0000 00               | enter 0,0                                       |
004015D8 | 8B45 08                  | mov eax,dword ptr ss:[ebp+8]                    |
004015DB | 0FAF45 0C                | imul eax,dword ptr ss:[ebp+C]                   |
004015DF | 90                       | nop                                             |
004015E0 | C9                       | leave                                           |
004015E1 | C2 0800                  | ret 8                                           |
004015E4 | C8 0000 00               | enter 0,0                                       |
004015E8 | 52                       | push edx                                        |
004015E9 | 8B45 08                  | mov eax,dword ptr ss:[ebp+8]                    |
004015EC | 33D2                     | xor edx,edx                                     |
004015EE | F77D 0C                  | idiv dword ptr ss:[ebp+C]                       |
004015F1 | 5A                       | pop edx                                         |
004015F2 | C9                       | leave                                           |
```

The flag is:

```
HV19{B0rked_Flag_Calculat0r}
```

## Day 17

### Challenge

Buy your special gifts online, but for the ultimative gift you have to become admin.

### Resources

http://whale.hacking-lab.com:8881/

### Solution

I read the source code and we need to accomplish the following:
- Register a user which is called santa (it will be transformed to all uppercase)
- login with that username and access the admin area. It will be made lowercase.
- is equal to string 'santa'
We search a Unicode char which fulfills these requirements. U+017F. I search for Unicode vulnerabilities and find this presentation. https://www.blackhat.com/presentations/bh-usa-09/WEBER/BHUSA09-Weber-UnicodeSecurityPreview-SLIDES.pdf
The correct char is U+017F. I copy and paste that char in the registration and can login afterwards. The flag is 
```
HV19{h4v1ng_fun_w1th_un1c0d3}
```

## Day 18

### Challenge 

Santa had some fun and created todays present with a special dance. this is what he made up for you:

```
096CD446EBC8E04D2FDE299BE44F322863F7A37C18763554EEE4C99C3FAD15
```

Dance with him to recover the flag.

### Resources

HV19-dance.zip
## Day 19

### Challenge

🏁🍇🎶🔤🐇🦁🍟🗞🍰📘🥖🖼🚩🥩😵⛺❗️🥐😀🍉🥞🏁👉️🧀🍎🍪🚀🙋🏔🍊😛🐔🚇🔷🎶📄🍦📩🍋💩⁉️🍄🥜🦖💣🎄🥨📺🥯📽🍖🐠📘👄🍔🍕🐖🌭🍷🦑🍴⛪🤧🌟🔓🔥🎁🧦🤬🚲🔔🕯🥶❤️💎📯🎙🎚🎛📻📱🔋😈🔌💻🐬🖨🖱🖲💾💿🧮🎥🎞🔎💡🔦🏮📔📖🏙😁💤👻🛴📙📚🥓📓🛩📜📰😂🍇🚕🔖🏷💰⛴💴💸🚁🥶💳😎🖍🚎🥳📝📁🗂🥴📅📇📈📉📊🔒⛄🌰🕷⏳📗🔨🛠🧲🐧🚑🧪🐋🧬🔬🔭📡🤪🚒💉💊🛏🛋🚽🚿🧴🧷🍩🧹🧺😺🧻🚚🧯😇🚬🗜👽🔗🧰🎿🛷🥌🎯🎱🎮🎰🎲🏎🥵🧩🎭🎨🧵🧶🎼🎤🥁🎬🏹🎓🍾💐🍞🔪💥🐉🚛🦕🔐🍗🤠🐳🧫🐟🖥🐡🌼🤢🌷🌍🌈✨🎍🌖🤯🐝🦠🦋🤮🌋🏥🏭🗽⛲💯🌁🌃🚌📕🚜🛁🛵🚦🚧⛵🛳💺🚠🛰🎆🤕💀🤓🤡👺🤖👌👎🧠👀😴🖤🔤 ❗️➡️ ㉓ 🆕🍯🐚🔢🍆🐸❗️➡️ 🖍🆕㊷ 🔂 ⌘ 🆕⏩⏩ 🐔🍨🍆❗️ 🐔㉓❗️❗️ 🍇 ⌘ ➡️🐽 ㊷ 🐽 ㉓ ⌘❗️❗️🍉 🎶🔤🍴🎙🦖📺🍉📘🍖📜🔔🌟🦑❤️💩🔋❤️🔔🍉📩🎞🏮🌟💾⛪📺🥯🥳🔤 ❗️➡️ 🅜 🎶🔤💐🐡🧰🎲🤓🚚🧩🤡🔤 ❗️➡️ 🅼 😀 🔤 🔒 ➡️ 🎅🏻⁉️ ➡️ 🎄🚩 🔤❗️📇🔪 🆕 🔡 👂🏼❗️🐔🍨🍆❗️🐔🍨👎🍆❗️❗️❗️ ➡️ 🄼 ↪️🐔🄼❗️🙌 🐔🍨🍆❗️🍇🤯🐇💻🔤👎🔤❗️🍉 ☣️🍇🆕🧠🆕🐔🅜❗️❗️➡️ ✓🔂 ⌘ 🆕⏩⏩🐔🍨🍆❗️🐔🅜❗️❗️🍇🐽 ㊷ 🐽 🅜 ⌘❗️❗️ ➡️ ⌃🐽 🄼 ⌘ 🚮🐔🄼❗️❗️➡️ ^💧🍺⌃➖🐔㉓❗️➗🐔🍨👎👍🍆❗️❗️❌^❌💧⌘❗️➡️ ⎈ ↪️ ⌘ ◀ 🐔🅼❗️🤝❎🍺🐽 ㊷ 🐽 🅼 ⌘❗️❗️➖ 🤜🤜 🐔🅜❗️➕🐔🅜❗️➖🐔🄼❗️➖🐔🅼❗️➕🐔🍨👍🍆❗️🤛✖🐔🍨👎👎👎🍆❗️🤛 🙌 🔢⎈❗️❗️🍇 🤯🐇💻🔤👎🔤❗️🍉✍✓ ⎈ ⌘ 🐔🍨👎🍆❗️❗️🍉🔡🆕📇🧠✓ 🐔🅜❗️❗️❗️➡️ ⌘↪️⌘ 🙌 🤷‍♀️🍇🤯🐇💻🔤👎🔤❗️🍉😀🍺⌘❗️🍉 🍉

### Solution

Install emoji code and then run the script.

```
 🔒 ➡️ 🎅🏻⁉️ ➡️ 🎄🚩 
🔑            
HV19{*<|:-)____\o/____;-D}
```

## Day 20

### Challenge

Santa was spying you on Discord and saw that you want something weird and obscure to reverse?
your wish is my command.

### Solution

```python
def main():
    byte300 = [0xCE, 0x55, 0x95, 0x4E, 0x38, 0x0C5, 0x89, 0x0A5, 0x1B, 0x6F, 0x5E, 0x25, 0x0D2, 0x1D, 0x2A, 0x2B, 0x5E, 0x7B, 0x39, 0x14, 0x8E, 0x0D0, 0x0F0, 0x0F8, 0x0F8, 0x0A5]
    i = 0x1337
    f=open("/PS4UPDATE.PUP", "rb")
    while i != 0x1714908:
        y=0
        f.seek(i)
        while y != 26:
            #XOR
            valu = f.read(1)
            print(byte300[y], ord(valu))
            byte300[y] = byte300[y] ^ int(ord(valu))
            y=y+1
        i=i+0x1337

    for c in byte300:
        print(chr(c), end='')
if __name__ == "__main__":
    main()
```

The flag is:

```
HV19{C0nsole_H0mebr3w_FTW}
```
## Hidden Flag1 

I searched the hidden flag in the text of flag 6. If you copy the info which is given at the end there are some strange spaces and tabs.
I googled and found stegsnow (http://manpages.ubuntu.com/manpages/bionic/man1/stegsnow.1.html) which I installed with **sudo apt-get install stegsonw** .
I run the following command and get the flag:

```
stegsnow -C textoriginal.txt 
HV19{1stHiddenFound}
``` 

## Hidden Flag 2

The filename of the flag 7 looks different. I copy it in CyberChef and it's a base58 decopded text. The flag is:

```
HV19{Dont_confuse_0_and_O}
```

## Hidden Flag 3

The Hint is : **Not each quote is compl**
The challange is marked as penetration testing so i nmap the host.

```
PORT   STATE SERVICE
17/tcp open  qotd
22/tcp open  ssh
```

Port 17 is special so I google the qotd service and it's a service called "quote of the day".
I connect to it with nc and get a single char. I guess the char changes overtime. I write a script which automates this.

```
HV19{an0ther-DaILYgn}
```

## Hidden Flag 4

Run the flag as perl code and get the flag.

```
HV19{Squ4ring the Circle}

```

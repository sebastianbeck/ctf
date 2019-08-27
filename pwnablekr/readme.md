# pwnable.kr

**What is pwnable.kr?**
> 'pwnable.kr' is a non-commercial wargame site which provides various pwn challenges regarding system exploitation. the main purpose of pwnable.kr is 'fun'.    please consider each of the challenges as a game. while playing pwnable.kr, you could learn/improve system hacking skills but that shouldn't be your only purpose.

I will only post solutions from Toddlers's Bottle, as the rules require.

> 3. challenges in Toddler's Bottle are allowed to freely post the solutions online. However, please refrain from posting solution for challenges in other categories. But if you insist, post easy ones (solved by many people) and do not spoil too much details for the sake of fun.

Let's start!

## fd
### Problem
```
Mommy! what is a file descriptor in Linux?

* try to play the wargame your self but if you are ABSOLUTE beginner, follow this tutorial link:
https://youtu.be/971eZhMHQQw

ssh fd@pwnable.kr -p2222 (pw:guest)
```
### Solution
The description is a hint. We somehow need to use a file descriptor to solve this challange.
You need to connect via ssh to the host. Afterwards I used **ls -la** to show all files from the folder.
There are the following interssting files: **flag, fd and fd.c**.
First we take a look at fd.c.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
	if(argc<2){
		printf("pass argv[1] a number\n");
		return 0;
	}
	int fd = atoi( argv[1] ) - 0x1234;
	int len = 0;
	len = read(fd, buf, 32);
	if(!strcmp("LETMEWIN\n", buf)){
		printf("good job :)\n");
		system("/bin/cat flag");
		exit(0);
	}
	printf("learn about Linux file IO\n");
	return 0;

}

```
You need to understand the functions of this programs to solve the challange.
So what does the program do? We need to pass 1 argument to the the program. That argument is converted to an integer and then we substract 0x1234 from it.
Afterwards the read function is called. Read will uses fd as file descriptor, and writes to the buf variable. 
If fd is 0 it will wait for user input. So we need to send 0x1234 in decimal as the argument. 
It prompts for user input and as we can see we need to enter **LETMEWIN** to match the string compare.
```
fd@prowl:~$ ./fd 4660
LETMEWIN
good job :)
mommy! I think I know what a file descriptor is!!
```
## collision
### Problem
```
Daddy told me about cool MD5 hash collision today.
I wanna do something like that too!

ssh col@pwnable.kr -p2222 (pw:guest)
```
### Solution
In this description we read something about a MD5 Hash collision. So that is a hint again
We connect via ssh to the host and again check for the files wiht **ls -la**.
We se the files **col.c, col and flag**. Again we take a closer look at the source code.
```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}

int main(int argc, char* argv[]){
	if(argc<2){
		printf("usage : %s [passcode]\n", argv[0]);
		return 0;
	}
	if(strlen(argv[1]) != 20){
		printf("passcode length should be 20 bytes\n");
		return 0;
	}

	if(hashcode == check_password( argv[1] )){
		system("/bin/cat flag");
		return 0;
	}
	else
		printf("wrong passcode.\n");
	return 0;
}
```
The program needs 1 argument, which should bea 20bytes long password. If that criteria is matched, it wil open the function check_password.

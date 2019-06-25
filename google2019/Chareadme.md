# STOP GAN (Path Home Network)
Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two separate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.

# Challenge 
After I had to look up the solution for the other challenge, I hope to solve this without help. 
I have never tried a bufferoverflow challenge before so let's see what I can learn.

I can download a zip file which contains a ELF32 bit executable and a .c file with source code.
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

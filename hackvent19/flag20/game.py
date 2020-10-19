def main():
    byte300 = [0xCE, 0x55, 0x95, 0x4E, 0x38, 0x0C5, 0x89, 0x0A5, 0x1B, 0x6F, 0x5E, 0x25, 0x0D2, 0x1D, 0x2A, 0x2B, 0x5E, 0x7B, 0x39, 0x14, 0x8E, 0x0D0, 0x0F0, 0x0F8, 0x0F8, 0x0A5]
    i = 0x1337
    f=open("PS4UPDATE.PUP", "rb")
    
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
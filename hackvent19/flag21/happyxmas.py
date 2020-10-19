import hashlib
from Crypto import Random
from Crypto.Cipher import AES
def main():
    #public key
    X= 0xc58966d17da18c7f019c881e187c608fcb5010ef36fba4a199e7b382a088072f
    Y= 0xd91b949eaf992c464d3e0d09c45b173b121d53097a9d47c25220c0b4beb943c
    #d = password and sha256 for priv key 
    #password is in rockyou txt
    #password is 16 long
    #the flag is encrypted with aes256
    #The key for AES is derived with pbkdf2_hmac, salt: "TwoHundredFiftySix", iterations: 256 * 256 * 256
    eflag = 'Hy97Xwv97vpwGn21finVvZj5pK/BvBjscf6vffm1po0='
    dk = hashlib.pbkdf2_hmac('sha256', b'1616161616161616', b'TwoHundredFiftySix', 256*256*256)
    print(dk.hex())
    encd = aes.decrypt()
    #aes = AES.new(key, AES.MODE_CBC, iv)
    #data = 'hello world 1234' # <- 16 bytes
    #encd = aes.encrypt(data)
    #print(encd)
if __name__ == "__main__":
    main()

    
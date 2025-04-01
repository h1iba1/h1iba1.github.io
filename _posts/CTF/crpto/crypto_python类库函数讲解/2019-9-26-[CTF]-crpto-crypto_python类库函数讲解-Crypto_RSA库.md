1.生成指定私钥私钥

```javascript
# coding=utf-8
from Crypto.PublicKey import RSA
from gmpy2 import mpz,invert
keypair=RSA.generate(1024)
keypair.p=275127860351348928173285174381581152299
keypair.q=319576316814478949870590164193048041239
keypair.e=65537
keypair.n=keypair.q*keypair.p
Qn=mpz(keypair.p-1)*(keypair.q)
keypair.d=invert(keypair.e,Qn)

pubkey=open("prikey.pem","w")
pubkey.write(str(keypair.exportKey('PEM'),encoding='utf-8'))
pubkey.close()
```



2.从公钥中读取e和n

```javascript
openssl rsa -pubin -in 【公钥文件】 -text
```

2.2从私钥中提取e和n

```javascript
openssl rsa -in 【私钥文件名】 -text
```



3.生成公钥

```javascript
# coding=utf-8
from Crypto.PublicKey import RSA
keypair=RSA.generate(1024)
keypair.p=275127860351348928173285174381581152299
keypair.q=319576316814478949870590164193048041239
keypair.e=65537
keypair.n=keypair.q*keypair.p

pubkey=open("pubkey.pem","w")
pubkey.write(str(keypair.publickey().exportKey('PEM'),encoding='utf-8'))
pubkey.close()
```



4.使用私钥解密文件

```javascript
openssl rsautl -decrypt -in 【待解密的文件dec】 -out 【解密后的文件enc】 -inkey 【私钥文件】
```



5.使用公钥加密文件

```javascript
openssl rsautl -encrypt -in 【待加密的文件dec】 -out 【加密后的文件enc】 -inkey 【公钥文件】 -pubin
```

使用openssl貌似解密解密貌似只能对一行数据进行



6.使用公私钥加解密字符串

```javascript
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

def rsa_encrypt(plain):
    with open('public.pem','rb') as f:
        data = f.read()
        key = RSA.importKey(data)
        rsa = PKCS1_v1_5.new(key)
        cipher = rsa.encrypt(plain)
        return base64.b64encode(cipher)

def rsa_decrypt(cipher):
    with open('private.pem','rb') as f:
        data = f.read()
        key = RSA.importKey(data)
        rsa = PKCS1_v1_5.new(key)
        plain = rsa.decrypt(base64.b64decode(cipher),'ERROR') # 'ERROR'必需
        return plain

if __name__ == '__main__':
    plain_text = b'This_is_a_test_string!'
    cipher = rsa_encrypt(plain_text)
    print(cipher)
    plain = rsa_decrypt(cipher)
    print(plain)
```





7.生成私钥和公钥

```javascript
from Crypto.PublicKey import RSA

rsa = RSA.generate(2048) # 返回的是密钥对象

public_pem = rsa.publickey().exportKey('PEM') # 生成公钥字节流
private_pem = rsa.exportKey('PEM') # 生成私钥字节流

f = open('public.pem','wb')
f.write(public_pem) # 将字节流写入文件
f.close()
f = open('private.pem','wb')
f.write(private_pem) # 将字节流写入文件
f.close()
```



8.从公钥中提取e和n

```javascript
#python2.7
from Crypto.PublicKey import RSA

with open('./pubkey.pem', 'r') as f:
    key = RSA.importKey(f)
    N = key.n
    e = key.e
print N
print e
```


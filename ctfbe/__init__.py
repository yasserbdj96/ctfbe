#!/usr/bin/env python
# coding:utf-8
# Code by : Yasser BDJ
# E-mail  : yasser.bdj96@gmail.com
"""
#set:usage.py,examples.py,changelog.txt
##################################################################
# USAGE :
#s
from ctfbe import ctfbe
#e
##################################################################
# EXAMPLES :
#s
from ctfbe import ctfbe

#to encrypt:
ctfbe("<THE_PATH_TO_THE_FILE_TO_BE_ENCRYPTED>").encode(passw="<PASSWORD>")

#to decode:
ctfbe("<THE_PATH_TO_THE_FILE_TO_BE_DECRYPTED>").decode(passw="<PASSWORD>",key_path="<KEY_FILE_PATH>")
#e
##################################################################
# CHANGELOG :
#s
## 1.0.2
 - Cancel the second level of encryption to increase speed.

## 1.0.1
 - Fix bugs.

## 1.0.0
 - First public release.
#e
##################################################################
"""
# VALUES :
__version__="1.0.2"
__name__="ctfbe"
__author__="Yasser Bdj (Boudjada Yasser)"
__author_email__="yasser.bdj96@gmail.com"
__github_user_name__="yasserbdj96"
__title__="CTFBE (codes texts files big data encrypted)"
__description__="A simple project to encrypt data and files. This program encrypts any type of file, whatever its size. Nothing can be decrypted without the password."
__author_website__=f"https://{__github_user_name__}.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=[__github_user_name__,'python']
__keywords__.extend(__title__.split(" "))
__keywords__.extend(__description__.split(" "))
__install_requires__=['pipincluder']
__Installation__="pip install "+__name__+"=="+__version__
__license__='MIT License'
__copyright__='Copyright © 2008->Present, '+__author__+"."
__license_text__=f'''MIT License

{__copyright__}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You also agree that if you become very rich you will give me 1% of your wealth.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
##################################################################
#s
try:
    from pipincluder import pipincluder
except:
    print("please use this command : pip install pipincluder")
    exit()

exec(pipincluder("import base64",
                 "import hashlib",
                 "import os",
                 "from datetime import date",
                 "import math",
                 "from PIL import Image",
                 "import numpy as np",
                 "import time",
                 "import random as rd",
                 "from ashar import ashar").modules())

#start ctfbe class:
class ctfbe:
    #__init__:
    def __init__(self,file,see=True):
        self.file=file
        self.see=see
        self.to=[["\\n","&"],["/","-"],["=","#"]]

    #key data:
    def key(passw):
        #chars used on encode:
        ss=['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','J','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','+','-','#','&','|','empty']
        random=rd.randint(1,255)
        rdlist=[]
        for _ in range(len(ss)):
            while random not in rdlist:
                rdlist.append(random)
            while random in rdlist:
                random=rd.randint(1,255)
        kk=""
        for i in range(len(ss)):
            kk+=f"""'{ss[i]}':{rdlist[i]},"""
        key="""self.data={"""+kk[0:len(kk)-1]+"""}"""
        p1=ashar(passw,key).encode()
        return p1

    #to base64:
    def tob64(text):
        encode64=base64.encodebytes(text)
        return str(encode64)[2:(len(str(encode64))-1)]
    
    #from base64:
    def fromb64(text):
        return base64.decodebytes(eval(f"b'{text}'"))
    
    #to md5:
    def tomd5(text):
        return hashlib.md5(text.encode()).hexdigest()
    
    #lower_upper:
    def lower_upper(char):
        if char.isupper():
            char=char.lower()
        else:
            char=char.upper()
        return char
    
    #see:
    def see(see,text,normal=True):
        if see==True:
            if normal==True:
                print(text,end="",flush=True)
            else:
                print(text)
    
    #encode:
    def encode(self,passw):
        self.passw=passw
        #open file & make it as base64 string:
        file=self.file
        ctfbe.see(self.see,f"# Open and read the file '{file}'...")
        file_open=open(file,'rb')
        file_read=file_open.read()
        file_final_str=ctfbe.tob64(file_read)
        ctfbe.see(self.see,"[DONE]",False)

        #save key file:
        key=ctfbe.key(self.passw)
        get_data=ashar(self.passw,key).decode()
        exec(f"{get_data}")

        #start an encrypted string:
        ctfbe.see(self.see,"# The beginning of the encryption chain:",False)
        
        #level_1:
        ctfbe.see(self.see,"    - Encryption level 1...")
        for j in range(len(self.to)):
            file_final_str=file_final_str.replace(self.to[j][0],self.to[j][1])
        level_1=file_final_str
        ctfbe.see(self.see,"[DONE]",False)

        level_2=level_1

        """
        #level_2:
        ctfbe.see(self.see,"    - Encryption level 2...")
        level_2=""
        for i in range(len(level_1)):
            char=list(level_1)
            level_2+=ctfbe.lower_upper(char[i])
        ctfbe.see(self.see,"[DONE]",False)
        """
        
        #level_3:
        ctfbe.see(self.see,"    - Encryption level 3...")
        level_3=level_2[::-1]
        #file size:
        sz=str(os.path.getsize(file))
        try:
            level_3=file.split(".")[0]+"|"+file.split(".")[1].upper()+"|"+sz+"|"+level_3
            fn=file.split(".")[0]
        except:
            level_3=file+"|"+"None|".upper()+sz+"|"+level_3
            fn=file
        ctfbe.see(self.see,"[DONE]",False)
        
        f=open(f"{fn}_key.txt","a")
        f.write(key)
        f.close()
        
        
        #level_4
        ctfbe.see(self.see,"    - Encryption level 4...")
        n=3
        S5=[]
        level_4=[level_3[i:i+n] for i in range(0,len(level_3),n)]
        
        for k in range(len(level_4)):
            h=list(level_4[k])
            for m in range(len(h)):
                S5.append(self.data[h[m]])
        level_4=[S5[i:i+n] for i in range(0,len(S5),n)]
        
        if len(level_4[len(level_4)-1])<3:
            ss=3-len(level_4[len(level_4)-1])
            for a in range(ss):
                level_4[len(level_4)-1].append(self.data["empty"])
        
        n=int(str(math.sqrt(len(level_4))).split('.')[0])
        
        level_4x=[level_4[i:i+n] for i in range(0,len(level_4),n)]
        
        for b in range(len(level_4x)):
            for f in range(len(level_4x[b])):
                level_4x[b][f]=tuple(level_4x[b][f])
            
        my_list = [self.data["empty"]]*3
        for s in range(len(level_4x)):
            y=len(level_4x[s])
            if y<n:
                for o in range(n-y):
                    level_4x[s].append(tuple(my_list))
        ctfbe.see(self.see,"[DONE]",False)
        
        ctfbe.see(self.see,f"# Create the encrypted file '{fn}.png'...")
        # Convert the pixels into an array using numpy
        array = np.array(level_4x, dtype=np.uint8)
        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image.save(f'{fn}.png')
        ctfbe.see(self.see,"[DONE]",False)
        
    #decode:
    def decode(self,key_path,passw):
        self.passw=passw
        
        #read key file:
        with open(key_path,'r') as file:
            data=file.read().replace('\n','')
        get_data=ashar(self.passw,data).decode()
        exec(f"{get_data}")

        code=self.file
        #start an decrypted string:
        ctfbe.see(self.see,"# The beginning of the decryption chain:",False)
        
        #level_4:
        ctfbe.see(self.see,"    - Level 4 decoding...")
        im=Image.open(code)
        width,height=im.size
        pixels=list(im.getdata())
        
        kk=[]
        for s in range(len(pixels)):
            for g in range(len(pixels[s])):
                if pixels[s][g]!=self.data["empty"]:
                    kk.append(pixels[s][g])
                    
        code=""
        for n in range(len(kk)):
            code+=list(self.data.keys())[list(self.data.values()).index(kk[n])]
        ctfbe.see(self.see,"[DONE]",False)

        #level_3:
        ctfbe.see(self.see,"    - Level 3 decoding...")
        fn,ty,sz,level_3=code.split("|")
        level_3=level_3[::-1]
        ctfbe.see(self.see,"[DONE]",False)
        
        level_2=level_3
        
        """
        #level_2:
        ctfbe.see(self.see,"    - Level 2 decoding...")
        level_2=""
        for i in range(len(level_3)):
            char=list(level_3)
            level_2+=ctfbe.lower_upper(char[i])
        ctfbe.see(self.see,"[DONE]",False)
        """
        
        #level_1:
        ctfbe.see(self.see,"    - Level 1 decoding...")
        for j in range(len(self.to)):
            level_2=level_2.replace(self.to[j][1],self.to[j][0])
        level_1=level_2
        ctfbe.see(self.see,"[DONE]",False)
        
        #Write the file:
        milliseconds = int(round(time.time() * 1000))
        today=date.today()
        d1=str(today.strftime("%d%m%Y"))+str(milliseconds)
        
        if ty!="None".upper():
            file=fn+"_"+d1+"."+ty.lower()
        else:
            file=fn+"_"+d1
        ctfbe.see(self.see,f"# Write the file '{file}'...")

        f=open(file,"wb")
        f.write(ctfbe.fromb64(level_1))
        f.close()
        ctfbe.see(self.see,"[DONE]",False)
#e
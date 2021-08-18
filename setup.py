import base64
import hashlib
import os
from datetime import date

#start ctfbe class:
class ctfbe:
    #__init__:
    def __init__(self,file,see=True):
        self.file=file
        self.see=see
        self.to=[["\\n","&"],["/","-"],["=","#"]]
        self.data = {
            'a': 0,'A': 5,'b': 10,'B': 15,'c': 20,'C': 25,'d': 30,'D': 35,
            'e': 40,'E': 45,'f': 50,'F': 55,'g': 60,'G': 65,'h': 70,'H': 75,
            'i': 80,'I': 85,'j': 90,'J': 95,'k': 100,'K': 105,'l': 110,'L': 115,
            'm': 120,'M': 125,'n': 130,'N': 135,'o': 140,'O': 145,'p': 150,'P': 155,
            'q': 160,'Q': 165,'r': 170,'R': 175,'s': 180,'S': 185,'t': 190,'T': 195,
            'u': 200,'U': 205,'v': 210,'V': 215,'w': 220,'W': 225,'x': 230,'X': 235,
            'y': 240,'Y': 245,'z': 250,'Z': 255,'&': 2,'#': 52,'-': 102,'+': 152,
            '0': 7,'1': 17,'2': 27,'3': 37,'4': 47,'5': 57,'6': 67,'7': 77,
            '8': 87,'9': 97,'|':205
        }

        
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
    def encode(self):
        #open file & make it as base64 string:
        file=self.file
        ctfbe.see(self.see,f"# Open and read the file '{file}'...")
        file_open=open(file,'rb')
        file_read=file_open.read()
        file_final_str=ctfbe.tob64(file_read)
        ctfbe.see(self.see,"[DONE]",False)

        #start an encrypted string:
        ctfbe.see(self.see,"# The beginning of the encryption chain:",False)
        
        #level_1:
        ctfbe.see(self.see,"    - Encryption level 1...")
        for j in range(len(self.to)):
            file_final_str=file_final_str.replace(self.to[j][0],self.to[j][1])
        level_1=file_final_str
        ctfbe.see(self.see,"[DONE]",False)

        #level_2:
        ctfbe.see(self.see,"    - Encryption level 2...")
        level_2=""
        for i in range(len(level_1)):
            char=list(level_1)
            level_2+=ctfbe.lower_upper(char[i])
        ctfbe.see(self.see,"[DONE]",False)

        #level_3:
        ctfbe.see(self.see,"    - Encryption level 3...")
        level_3=level_2[::-1]
        #file size:
        sz=str(os.path.getsize(file))
        try:
            level_3=file.split(".")[0]+"|"+file.split(".")[1].upper()+"|"+sz+"|"+level_3
        except:
            level_3=file+"|"+"None|".upper()+sz+"|"+level_3
        #print(ctfbe.tomd5(level_3))
        ctfbe.see(self.see,"[DONE]",False)
        
        """
        ctfbe.see(self.see,f"# Write the file '{file}.ctfbe'...")
        f=open(f'{file}.ctfbe',"w")
        f.write(level_3)
        f.close()
        ctfbe.see(self.see,"[DONE]",False)
        """
        
        #level_4
        n=3
        S5=[]
        level_4=[level_3[i:i+n] for i in range(0,len(level_3),n)]
        #print(self.data['a'])
        
        for k in range(len(level_4)):
            h=list(level_4[k])
            for m in range(len(h)):
                S5.append(self.data[h[m]])
        
        level_4=[S5[i:i+n] for i in range(0,len(S5),n)]
        
        if len(level_4[len(level_4)-1])<3:
            ss=3-len(level_4[len(level_4)-1])
            
            for a in range(ss):
                level_4[len(level_4)-1].append(99)
        
        import math
        n=int(str(math.sqrt(len(level_4))).split('.')[0])
        
        
        level_4x=[level_4[i:i+n] for i in range(0,len(level_4),n)]
        
        
        
        
        from PIL import Image
        import numpy as np
        
        
        for b in range(len(level_4x)):
            for f in range(len(level_4x[b])):
                #for c in range(len(level_4x[b][f])):

        
     
                level_4x[b][f]=tuple(level_4x[b][f])
        print(level_4x)
        
        """
        pixels = [
            [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
            [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
            [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
            [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
        ]
        """
        # Convert the pixels into an array using numpy
        array = np.array(level_4, dtype=np.uint8)

        # Use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image.save('new.png')
       
        
        #return level_4
        
    #decode:
    def decode(self):
        code=self.file
        #start an decrypted string:
        ctfbe.see(self.see,"# The beginning of the decryption chain:",False)
        
        #level_3:
        ctfbe.see(self.see,"    - Level 3 decoding...")
        fn,ty,sz,level_3=code.split("|")
        level_3=level_3[::-1]
        ctfbe.see(self.see,"[DONE]",False)
        
        #level_2:
        ctfbe.see(self.see,"    - Level 2 decoding...")
        level_2=""
        for i in range(len(level_3)):
            char=list(level_3)
            level_2+=ctfbe.lower_upper(char[i])
        ctfbe.see(self.see,"[DONE]",False)
        
        #level_1:
        ctfbe.see(self.see,"    - Level 1 decoding...")
        for j in range(len(self.to)):
            level_2=level_2.replace(self.to[j][1],self.to[j][0])
        level_1=level_2
        ctfbe.see(self.see,"[DONE]",False)
        
        #Write the file:
        
        today=date.today()
        d1=today.strftime("%d%m%Y")
        
        if ty!="None".upper():
            file=fn+"_"+d1+"."+ty.lower()
        else:
            file=fn+"_"+d1
        ctfbe.see(self.see,f"# Write the file '{file}'...")

        f=open(file,"wb")
        f.write(ctfbe.fromb64(level_1))
        f.close()
        ctfbe.see(self.see,"[DONE]",False)

        return level_1
        
p1=ctfbe("yasserbdj96.png").encode()
#p2=ctfbe(p1).decode()
print(p1)

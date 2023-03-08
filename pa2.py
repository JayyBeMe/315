import random
import hashlib
import sys

infile = open("rockyou.txt")
infile2 = open("HashedPasswords.txt")

pwDictionary = []
pwHashes = []
salts = []

def getSalt():
        
        for line in infile2:
        

                fileLine = line.strip()
                stealSalt = fileLine[7] + fileLine[8]   #or fileLine[7:8]
                salts.append(stealSalt)
        
      
        
def getPassword():
        
        for line in infile:

                fileLine2 = line.strip()
                pwDictionary.append(fileLine2)

                
#variations
#reverse
def reverse(x):
        return x[::-1]

def lowercase(x):
    for i in range(len(x)):
        if (i%2 == 0) and (charAt(i).islower()):
                            return charAt(i).switchcase()
                            
                            
            
a = lowercase('timmy')
print(a)
    
    
    

    


       

                
                
def hashPassword(salts, pw):
    for i in range(len(pwDictionary)):
        
    
        #md5 Line
        saltedPw = salts[i] + pwDictionary[i]
        hashObject = hashlib.md5(saltedPw.encode('utf-8'))
        hashHex = hashObject.hexdigest()
        pwHashes.append(hashHex)




                 
                





def createAttack():
    for i in range(len(pwDictionary)):
        for j in range(len(pwHashes)):
            #attackHash = hashPassword(salts[j], pwDictionary[i])
            #if attackHash == pwHashes[j][10:40]:
            if pwDictionary[i] == pwHashes[j]:
                #print("Cracked: " + pwHashes[j][:6] + " " + salts[j] + " " + attackHash + " " + pwDictionary[i])
                print(pwDictionary[i])
            
                                
        

                
      
      
       
                                

def report():
        print("Name" + "  " + "Salt" + "            " + "Hash" + "                 " +  "Password")
        print("----------------------------------------------------")
        
        

            
        
        print("----------------------------------------------------")
        print("New Hashes")
        print("----------------------------------------------------")

        print("Cracked Hashes: ")
        print("Uncracked Hashes: ")


getSalt()
getPassword()
hashPassword(salts, pwDictionary)
createAttack()
report()
       
              


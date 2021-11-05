from PIL import Image
import os
import sys
from colorama import Fore, Style 
from time import sleep
from random import randint


Clear=lambda: os.system("clear" if os.name=="nt" "cls" else "clear")

OwnAsc={
    "q": 10,
    "w": 11,
    "e": 12,
    "r": 13,
    "t": 14,
    "y": 15,
    "u": 16,
    "i": 17,
    "o": 18,
    "p": 19,

    "d": 20,
    "f": 21,
    "g": 22,
    "h": 23,
    "j": 24,
    "k": 25,
    "l": 26,
    ";": 27,
    "'": 28,
    "#": 29,

    "z": 30,
    "x": 31,
    "c": 32,
    "v": 33,
    "b": 34,
    "n": 35,
    "m": 36,
    ",": 37,
    ".": 38,
    "/": 39,
    
    "!": 40,
    "£": 41,
    "$": 42,
    "%": 43,
    "^": 44,
    "&": 45,
    "*": 46,
    "(": 47,
    ")": 48,
    "-": 49,

    "_": 50,
    "+": 51,
    "=": 52,
    "{": 53,
    "}": 54,
    ":": 55,
    "@": 56,
    "~": 57,
    "<": 58,
    ">": 59,

    "?": 60,
    "[": 61,
    "]": 62,
    "a": 63,
    "s": 64,
    "Q": 65,
    "W": 66,
    "E": 67,
    "R": 68,
    "T": 69,

    "Y": 70,
    "U": 71,
    "I": 72,
    "O": 73,
    "P": 74,
    "A": 75,
    "S": 76,
    "D": 77,
    "F": 78,
    "G": 79,

    "H": 80,
    "J": 81,
    "K": 82,
    "L": 83,
    "Z": 84,
    "X": 85,
    "C": 86,
    "V": 87,
    "B": 88,
    "N": 89,

    "M": 90,
}

def Decode(OwnAsc):
    file=open("messages/msg.txt", "w")
    print("do you have your own image name are do you want to open the the defealt decoding image?\n",Fore.RED,"1. I have my own\n",Fore.CYAN,"2.I am using the \"YourEncodedImage\" file ",Style.RESET_ALL)
    sys.stdout.write("Wrtie your anwser hear -->")


    file=open("key.txt", "r") # opning the file #
    arr=[] # declaring array to house the things

    # Itrates trough each item in file
    LinesInFile=""
    for line in open("key.txt").readlines(): 
        LinesInFile=LinesInFile+line
        #print("lines in ", LinesInFile)

    # goes through the string charter by charter and adds it to the arry
    for i in range(0,len(LinesInFile)):
        arr.append(LinesInFile[i])

    # Goes through the arry and removes \n
    for i in range(len(arr)):
        # try to remove the chater
        try:
            arr.remove("\n")
        #if the charter is not there then break the loop
        except Exception as err:
            if(str(err)[0:29]=="list.remove(x): x not in list"):
                break
                
    file.close()
    

    #kepp doing until brokcen
    while True:
        try:
            inpSt=int(input(Fore.MAGENTA)) # user input
            if(inpSt==1): # DO MORE HEAR
                try:
                    print(Style.RESET_ALL,"what File do you want to open: ") 
                    sys.stdout.write("Dont forget to put the folder before the file name. E.g images/image.png")
                    FileOpen=str(input(Fore.MAGENTA))

                except Exception as errr:
                    print(errr) # Handle exception better

            elif(inpSt==2):
                Style.RESET_ALL
                FileOpen="images/YourEncodedImage.png"

            elif(inpSt>2 or inpSt<1): # Rasie exception on purpose
                2+None    

            imgDecode=Image.open(FileOpen) 
            break # no errors so break 


        except Exception as err: # Ther is error

            if(str(err)[0:39]=="invalid literal for int() with base 10:"): # if they no enter number
                print(Style.RESET_ALL,"Please enter a number")
                sys.stdout.write("Wrtie your awnser hear:\t")

            elif(str(err)[0:55]=="unsupported operand type(s) for +: 'int' and 'NoneType'"): # if they enter number that is not valied
                print(Style.RESET_ALL,"Please enter a number bewteen 1 and 2")
                sys.stdout.write("Wrtie your awnser hear:\t")
            else:
                print(err) # unkown err occared
            


            #print(Style.RESET_ALL, "\n",error)
            #Send email of err

    width, hight = imgDecode.size[0], imgDecode.size[1] # get highet and width of image
    RGBvalD=imgDecode.convert("RGBA") #  convert to RGBA

    #m=0
    #n=0
    msg=[] # this will open the array which will hold the measge
    




    x=0
    y=0

    i = 0
    for y in range(hight):
        for x in range(width):
            r,g,b,aB=RGBvalD.getpixel((x,y))
            if(aB!=255): # if old code is used agin then this shold be if(n!=m):
                if(arr[i]!="1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
                    for key in OwnAsc:
                        if(arr[i] in OwnAsc.keys()):
                            xx=int(OwnAsc[arr[i]])
                            print("xx = ", xx)
                        else:
                            xx=int(arr[i])
                            print("xx when norm=",xx)
                # and hear sould be n=n+1
                r,g,b,a=RGBvalD.getpixel((xx,y))
                chrR=chr(r)
                chrG=chr(g)
                chrB=chr(b)
                
                msg.append(chrR)
                msg.append(chrG)
                msg.append(chrB) 
                i=i+1

    print(Style.RESET_ALL)

    file=open("msg.txt", "w")
    #write the msg to file
    for i in range(len(msg)):
        #print(i)
        file.write(msg[i])
        if(i==len(msg)):
            file.close()
            file=open("messages/msg.txt", "r")
            break

    #prit out msg
    print("Your meassage reads\n-------------------------------\n",Fore.YELLOW)
    for _ in range(len(msg)):
        sys.stdout.write(msg[_])
    print(Style.RESET_ALL,"\n\n-------------------------------")
    file.close()
    input("Press any key to countiue\t")
    print("Returning to menu")
    IdontKnowWhatToCallThisVar=randint(0,1)
    if(IdontKnowWhatToCallThisVar==0):
        sleep(0.5)
    else:
        sleep(0.75)
    Clear() # fucntion ends so it will automaticly go to main as is in Whilte true loop



# ENDOING #




def Encode(OwnAsc):
    # Image # 
    img = Image.open("images/DontDelThisFile.png") # Opnning up the image #
    width, hight = img.size[0], img.size[1]
    img1 = Image.open("images/DontDelThisFile.png")

    #Inputing msg
    msg = input("Enter MSG: ") # Getting msg input #

    
    file=open("key.txt", "r")
    arr=[] 

    LinesInFile=""
    for line in open("key.txt").readlines(): 
        LinesInFile=LinesInFile+line

    for i in range(0,len(LinesInFile)):
        arr.append(LinesInFile[i])

    for i in range(len(arr)):

        try:
            arr.remove("\n")
        except Exception as err:
            if(str(err)[0:29]=="list.remove(x): x not in list"):
                break
    file.close()

    x=0 # x #
    y=0 # y #

    msgAsci=[] # Arry making # 
    for x in range ((width*hight)-2):
        msgAsci.append(0)

    x=0
    y=0
    q=0
    while(q!=len(msg)):
        msgAsci.insert(q, ord(msg[q]) )
        q=q+1
    n=0


    # THIS NEEDS WORKING ON #
    # It takes the thing and makes the thing that goes through the if statment
    F=len(msg)//3
    M=len(msg)%3

    if(F>0 and M>0):
        l=F+1
        
    elif(F>0 and M==0):
        l=F
    elif(F==0 and M>0):
        l=1
    

    i=0
    for y in range(hight):
            for x in range(width):
                if(n!=l):
                    #print("n ",n)
                    #print("i ",i)
                    r=msgAsci[3*n]
                    g=msgAsci[(3*n)+1]
                    b=msgAsci[(3*n)+2]
                    if(x==width):
                        x=0
                        y=y+1
            
                    elif(y==hight and x==width):
                        print("MSG can not be fittied in this img")

                        #quit() 
                    
                    try:


                        if(arr[i]!="1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
                            for key in OwnAsc:
                                
                                if(arr[i] in OwnAsc.keys()):
                                    xx=int(OwnAsc[arr[i]])
                                    print("xx = ", xx)
                                else:
                                    xx=int(arr[i])

                        img1.putpixel((xx,y), (r,g,b,0) )
                        #print(img.getpixel((int(arr[i]),y)))
                        #print("arr spit ", arr[i])

                    except Exception as err: 

                        if(str(err)[0:23]=="list index out of range"):
                            pass
                            #add items to key
                        else:
                            #email err msg
                            pass

                   
                    #print(msgAsci)
                    n=n+1
                    i=i+1


    #save the img
    img1.save("images/YourEncodedImage.png")

abc="asdfghjklzxcvbnmqwertyuiop"
abcap="QWERTYUIOPASDFGHJKLZXCVBNM"
numbers="1234567890"
sym="!£$%^&*()_+{}:@~?><,./;'#[]-="


def check(var, randGEN, lock):
    if(var[randGEN] in lock):
        return True
    else:
        return False

while True:
    inp=input("Type: ")
    Clear()
    if(inp=="1"):
        Decode(OwnAsc)
    elif(inp=="2"):
        Encode(OwnAsc)
    elif(inp=="3"): 
        passA=0
        passAcap=0
        passN=0
        passS=0
        lock=set()
        # Generator #
        for i in range(100):
            rand=randint(0,16)
            #alfbet
            if(rand>5 and rand<10 and passA!=len(abc)-1): # 6,7,8,9
                randGEN=randint(0,len(abc)-1)

                while True:
                    if(check(abc, randGEN, lock)==True): # if the check retruens vlaue True
                        randGEN=randint(0,len(abc)-1)
                    else:
                        lock.add( abc[randGEN] ) 
                        break
                    if(passA==len(abc)-1):
                        break
                passA=passA+1

            #numbers
            elif(rand<5 and rand>0 and passN!=len(numbers)-1 ): # 4,3,2,1
                randGEN=randint(0,len(numbers)-1)
                
                while True:
                    if(check(numbers, randGEN, lock)==True ): # if the check retruens vlaue True
                        randGEN=randint(0,len(numbers)-1)
                    else:
                        lock.add( numbers[randGEN] ) 
                        break    
                    if(passA==len(numbers)-1):
                        break
                passN=passN+1

            #symbols
            elif( rand==5 or rand==10 or rand==0 or rand==11 and passN!=len(sym)-1): # 0, 5, 10, 11
                randGEN=randint(0,len(sym)-1)

                while True:
                    if(check(sym, randGEN, lock)==True): # if the check retruens vlaue True
                        randGEN=randint(0,len(sym)-1)
                    else:
                        lock.add( sym[randGEN] ) 
                        break
                    if(passS==len(abc)-1):
                        break
                passS=passS+1

            elif(rand>11 and passAcap!=len(abcap)-1): # 12, 13, 14, 15 , 16
                randGEN=randint(0, len(abcap)-1)

                while True:
                    if(check(abcap, randGEN, lock)==True):
                        randGEN=randint(0,len(abcap)-1)
                    else:
                        lock.add( abcap[randGEN] )
                        break
                    if(passAcap==len(abc)-1):
                        break
                passAcap=passAcap+1
             
            ListLock=list(lock)
            file=open("key.txt", "w")
            for i in range(len(ListLock)-1):
                file.write(ListLock[i])
            file.close()

    else:
        img=Image.open("images/YourEncodedImage.png")
        R=img.convert("RGBA")
        for i in range(100):
            print(img.getpixel((i,0)))
        quit()

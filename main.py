import os
import sys
from PIL import Image
from colorama import Fore, Style 
from time import sleep
from random import randint
from functools import lru_cache

Clear=lambda: os.system("clear" if os.name=="nt" "cls" else "clear")
#Slect = lambda: print(Style.RESET_ALL+"Slect from the files:\n"+Fore.RED+"1.AppFiles\n2.DragTheImageToDecodeHear\n3.Encoded Image",Fore.GREEN+"\n4.Return to Home",Style.RESET_ALL)

def Slect(extra):
    print(Style.RESET_ALL+"Slect from the files:\n"+Fore.RED+"1.AppFiles\n2.DragTheImageToDecodeHear\n3.Encoded Image",Style.RESET_ALL)
    for i in range(len(extra)):
        print(Fore.YELLOW+str(i+4)+".%s" %(extra[i]))
        FinalI=i
    try:
        print(Fore.GREEN+"%d.Return to Home" %(FinalI+5)+Style.RESET_ALL)
    except:
        print(Fore.GREEN+"%d.Return to Home" %(4)+Style.RESET_ALL)

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



@lru_cache(maxsize=50)
def Read(string):
    #print(string, type(string))
    stringSplit=string.split("/")
    if(len(stringSplit)==1):
        return "BaseFile"

    listt=[]
    items=0 
    WhatRemove=list()
    #print("string=",string)
    for i in range(len(string)):
        listt.append(string[i])
    #print(listt)
    for i in range(len(listt)):
        if(listt[i]=="/"):
            items=i
    #print(listt)     
         
    for i in range(items, len(listt)):
        #WhatRemove=WhatRemove+listt[i]
        WhatRemove.append(i)
        #print(WhatRemove)
    #print(listt)
    for i in range(len(WhatRemove)):
        listt[WhatRemove[i]]="@plz]#;efeq1234567890poiuytrdcvbn"

    #print(listt)
    for i in range(len(listt)):
        try:
            listt.remove("@plz]#;efeq1234567890poiuytrdcvbn")
        except:
            pass
    #print(listt)
    paf=""
    for i in range(len(listt)):
        paf=paf+listt[i] 
        #print(listt[i])
        #print("paf="+paf)
    return paf


def FileSlect(fileTopen, path, extra):
#    print("itrannnnnnnn")
 #   print("FileTopen",fileTopen)
  #  print("path",path)
   # sleep(2)
    path=fileTopen+"/"
    print(Fore.LIGHTBLUE_EX+path)
    path=str()
    FilesInslected=os.listdir(fileTopen)
    #print(FilesInslected)

    for i in range(len(FilesInslected)):
        if(os.path.isfile(fileTopen+"/"+FilesInslected[i])==True):
            print(Fore.YELLOW+str(i+1)+"."+FilesInslected[i]+Style.RESET_ALL)

        elif(os.path.isdir(fileTopen+"/"+FilesInslected[i])==True):
            print(Fore.RED+str(i+1)+"."+FilesInslected[i]+Style.RESET_ALL)
        iii=i
    print(Style.RESET_ALL+str(iii+2)+".Go back")
    sys.stdout.write("Write the number of the option --> ")
    while True:
        try:
            FileSlected=int(input(Fore.MAGENTA))
            break
        except Exception as err: 
            if(str(err)[0:len("invalid literal for int() with base 10:")]==""):
                print(Fore.RED)
                sys.stdout.write("Please entre a number:")
    #print("pppp",path)

    if(FileSlected==iii+2):
        path=Read(fileTopen)
        if(path=="BaseFile"):
            Clear()
            Slect(extra)
            sys.stdout.write("Write the number of your option --> ")
            path="BaseFile"
            return path
        #print(Fore.WHITE,path)
    
    elif(FileSlected<iii+3 or FileSlected>1):
        #path=Read(path)
        FileSel=FilesInslected[FileSlected-1]
        path=fileTopen+"/"+FileSel    

    if(os.path.isdir(path)==True):
        if(len(os.listdir(path))==0):
            Clear()
            #isitEmpty=True
            print(Style.RESET_ALL+"This folder is empty")
            #print(fileTopen)
            path=fileTopen
            FileSlect(path,path, extra)
            return path
            

        elif(len(os.listdir(path))>0):
            #isitEmpty=False
            Clear()
            path=FileSlect(path, path, extra)
            return path

    elif(os.path.isfile(path)==True):
        #print(path)
        name, ext = os.path.splitext(path)
        if(ext!=".png"):
            print(Style.RESET_ALL+"This is not a png file")
            input("press any key to continue")
            path=Read(path)
            Clear()
            FileSlect(fileTopen, path, extra)
            return path
        else:
            return path 

def Decode(OwnAsc):
    file=open("MeassageResived.txt", "w")

    file=open("AppFiles/key.txt", "r") # opning the file #
    arr=[] # declaring array to house the things

    # Itrates trough each item in file
    LinesInFile=""
    for line in open("AppFiles/key.txt").readlines(): 
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

    extra=list()
    FileInBase=os.listdir()
    for i in range(len(FileInBase)):
        if(os.path.isfile(FileInBase[i])==True):
            f, ext=os.path.splitext(FileInBase[i])
            if(ext==".png"):
                extra.append(FileInBase[i])


    #Welcome to the decoding side. 
    print(Fore.MAGENTA+"Welcome to the decoding side of this application.\n"+Fore.LIGHTBLUE_EX+"NAVAGATE "+Style.RESET_ALL +"the files to find the image you want to decode. A folder will apper red and and a non folder will be yellow")
    print(Fore.RED+"1.AppFiles\n2.DragTheImageToDecodeHear\n3.Encoded Image",Style.RESET_ALL)
    for i in range(len(extra)):
        print(Fore.YELLOW+str(i+4)+".%s" %(extra[i]))
        FinalI=i
        upperBound=i+4
        #print("upperBound",upperBound) 
    try:
        FinalI+1
    
    except Exception as err:
        if(str(err)[0:len("local variable 'FinalI' referenced before assignment")]=="local variable 'FinalI' referenced before assignment"):
            FinalI=-1
            upperBound=4
    try:
        print(Fore.GREEN+"%d.Return to Home" %(FinalI+5)+Style.RESET_ALL)
    except:
        print(Fore.GREEN+"%d.Return to Home" %(4)+Style.RESET_ALL)


    sys.stdout.write("Write the number before the file you want to slect: ")

    while True:
        while True:
            try:
                FileSlected=int(input(Fore.MAGENTA))
                break
            except Exception as err:
                if(str(err)[0:len("invalid literal for int() with base 10:")]=="invalid literal for int() with base 10:"):
                    print(Fore.RED)
                    sys.stdout.write("Please entre a number: ")


        if(FileSlected==1):
            Clear()
            path=str()
            if(len(os.listdir("AppFiles"))==0):
                print(Fore.LIGHTBLUE_EX+"AppFiles/"+Style.RESET_ALL)
                print("There is noething in this file")
                input("Press any key to countiue")
                Clear()
                Slect(extra)
                sys.stdout.write("Write the number before the file you want to slect: ")

            else:
                path=FileSlect("AppFiles", path, extra)
                if(path!="BaseFile"):
                    imgDecode=Image.open(path) 
                    break

        elif(FileSlected==2):
            Clear()
            path=str()

            if(len(os.listdir("DragTheImageToDecodeHear"))==0):
                print(Fore.LIGHTBLUE_EX+"DragTheImageToDecodeHear/"+Style.RESET_ALL)
                print("There is noething in this file")
                input("Press any key to countiue")
                Clear()
                Slect(extra)
                sys.stdout.write("Write the number before the file you want to slect: ")

            else:
                path=FileSlect("DragTheImageToDecodeHear", path, extra)
                if(path!="BaseFile"):
                    imgDecode=Image.open(path) 
                    break

        elif(FileSlected==3):
            Clear()
            path=str()
            if(len(os.listdir("Encoded Image"))==0):
                print(Fore.LIGHTBLUE_EX+"Encoded Image/"+Style.RESET_ALL)
                print("There is noething in this file")
                input("Press any key to countiue")
                Clear()
                Slect(extra)
                sys.stdout.write("Write the number before the file you want to slect: ")

            else:
                
                path=FileSlect("Encoded Image", path, extra)
                if(path!="BaseFile"):
                    imgDecode=Image.open(path) 
                    break

        elif(FileSlected>upperBound or FileSlected<1):
            Clear()
            print("Welcome to the decoding side of this application.\n"+Fore.LIGHTBLUE_EX+"NAVAGATE "+Style.RESET_ALL +"the files to find the image you want to decode. A folder will apper red and and a non folder will be yellow")
            Slect(extra)
            sys.stdout.write("Please entre a number: ")
        elif(FileSlected==FinalI+5):
            print(Style.RESET_ALL)
            Clear()
            return
        elif(FileSlected<=upperBound and FileSlected>3):
            #print("ran")
            imgDecode=Image.open(extra[FileSlected-4])
            break



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
                            #print("xx = ", xx)
                        else:
                            xx=int(arr[i])
                            #print("xx when norm=",xx)
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

    file=open("MeassageResived.txt", "w")
    #write the msg to file
    for i in range(len(msg)):
        #print(i)
        file.write(msg[i])
        if(i==len(msg)):
            file.close()
            file=open("MeassageResived.txt", "r")
            break
    Clear()

    #prit out msg
    print("Your meassage reads\n-------------------------------\n",Fore.YELLOW)
    for _ in range(len(msg)):
        sys.stdout.write(msg[_])
    print(Style.RESET_ALL,"\n\n-------------------------------",Fore.RED)
    file.close()
    print("This msg is stored in the messages folder, in the MeassageResivedfile.",Style.RESET_ALL)
    input("Press any key to countiue\t")
    print(Style.RESET_ALL,"Returning to menu")
    IdontKnowWhatToCallThisVar=randint(0,1)
    if(IdontKnowWhatToCallThisVar==0):
        sleep(0.5)
    else:
        sleep(0.75)
    Clear() # fucntion ends so it will automaticly go to main as is in Whilte true loop



# ENDOING #




def Encode(OwnAsc):
    # Image # 
    img = Image.open("AppFiles/DontDelThisFile.png") # Opnning up the image #
    width, hight = img.size[0], img.size[1]
    img1 = Image.open("AppFiles/DontDelThisFile.png")

    #Inputing msg
    while True:
        msg = input("Enter MSG: ") # Getting msg input #
        if(len(msg)==0):
            print(Fore.RED+"Please type something",Style.RESET_ALL)
        else:
            break

    file=open("AppFiles/key.txt", "r")
    arr=[] 

    LinesInFile=""
    for line in open("AppFiles/key.txt").readlines(): 
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
    elif(F==0 and M==0):
        print("please enter somwthing\nRETURNING TO MENUE")
        Clear()
        return
    

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

                        #quit() Do somwthing hear
                    
                    try:


                        if(arr[i]!="1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
                            for key in OwnAsc:
                                
                                if(arr[i] in OwnAsc.keys()):
                                    xx=int(OwnAsc[arr[i]])
                                    #print("xx = ", xx)
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
    img1.save("Encoded Image/Encoded Image.png")
    Clear()

abc="asdfghjklzxcvbnmqwertyuiop"
abcap="QWERTYUIOPASDFGHJKLZXCVBNM"
numbers="1234567890"
sym="!£$%^&*()_+{}:@~?><,./;'#[]-="


def check(var, randGEN, lock):
    if(var[randGEN] in lock):
        return True
    else:
        return False

def genrator(var ,passes):
    randGEN=randint(0, len(var)-1)

    while True:
        if(check(var, randGEN, lock)==True):
            randGEN=randint(0,len(var)-1)
        else:
            lock.add( var[randGEN] )
            break
        if(passes==len(var)-1):
            break
        passes=passes+1



while True:
    print("Welcome to the",Fore.LIGHTBLUE_EX,"Image ENCODER ", Fore.RED , "\n1.Encode the Image",Fore.BLUE, "\n2.Decode the image", Fore.LIGHTGREEN_EX,"\n3.Genrate key",Style.RESET_ALL)
    sys.stdout.write("Type the number hear: ")
    inp=input(Fore.MAGENTA) # try to see if number and other exsceptions
    print(Style.RESET_ALL)
    Clear()
    if(inp=="1"):
        Encode(OwnAsc)
    elif(inp=="2"):
        Decode(OwnAsc)
    elif(inp=="3"): 
        print("Genrating Key \\")
        sleep(0.25)
        Clear()
        Clear()
        print("Genrating Key /")
        sleep(0.25)
        Clear()
        rand=randint(0,1)
        if(rand==1):
            print("Genrating Key --")
            sleep(0.25)
            Clear()
            rand=randint(0,1)
            if(rand==1):
                print("Genrating Key |")
                sleep(0.25)
                Clear()

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
                genrator(abc,passA)

            #numbers
            elif(rand<5 and rand>0 and passN!=len(numbers)-1 ): # 4,3,2,1
                genrator(numbers,passN)

            #symbols
            elif( rand==5 or rand==10 or rand==0 or rand==11 and passS!=len(sym)-1): # 0, 5, 10, 11
                genrator(sym,passS,)

            #caps
            elif(rand>11 and passAcap!=len(abcap)-1): # 12, 13, 14, 15 , 16
                genrator(abcap, passAcap)
             
            ListLock=list(lock)
            file=open("AppFiles/key.txt", "w")
            for i in range(len(ListLock)-1):
                file.write(ListLock[i])
            file.close()

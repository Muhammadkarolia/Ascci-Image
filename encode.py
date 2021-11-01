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
    "[": 20,
    "]": 21,
    "a": 22,
    "s": 19,
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
   "\\": 30,
    "z": 31,
    "x": 32,
    "c": 33,
    "v": 34,
    "b": 35,
    "n": 36,
    "m": 37,
    ",": 38,
    ".": 39,
    "/": 40,
}

def Decode():
    file=open("messages/msg.txt", "w")
    print("do you have your own image name are do you want to open the the defealt decoding image?\n",Fore.RED,"1. I have my own\n",Fore.CYAN,"2.I am using the \"YourEncodedImage\" file ",Style.RESET_ALL)
    sys.stdout.write("Wrtie your anwser hear -->")

    file=open("key.txt", "r") # opning the file #
    arr=[] # declaring array to house the things

    # Itrates trough each item in file
    LinesInFile=""
    for line in open("key.txt").readlines(): 
        LinesInFile=LinesInFile+line

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

    m=0
    n=0
    msg=[] # this will open the array which will hold the measge
    i=0 # this will coude the loop to break
    file=open("msg.txt", "w")
    for y in range(hight):
        for x in range(width):
            i=i+1
            if(i==len(arr)): # the len of the key is equl to passes(i) then break 
                break
            r,g,b,a=RGBvalD.getpixel( (int(arr[x]),y) )
            if(a!=255):
                m=m+1
        if(i==len(arr)):
            break
    #x=0
    #y=0 

    # get the msg form the img
    for y in range(hight):
        for x in range(width):
            if(n!=m):      
                n=n+1
                r,g,b,a=RGBvalD.getpixel((int(arr[x]),y))
                chrR=chr(r)
                chrG=chr(g)
                chrB=chr(b)
                
                msg.append(chrR)
                msg.append(chrG)
                msg.append(chrB) 

    print(Style.RESET_ALL)

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
    input("Press any key to countiue\t")
    print("Returning to menu")
    IdontKnowWhatToCallThisVar=randint(0,1)
    if(IdontKnowWhatToCallThisVar==0):
        sleep(0.5)
    else:
        sleep(0.75)
    Clear() # fucntion ends so it will automaticly go to main as is in Whilte true loop


def Encode():
    # Image # 
    img = Image.open("images/DontDelThisFile.png") # Opnning up the image #
    width, hight = img.size[0], img.size[1]
    img1 = Image.open("images/DontDelThisFile.png")

    #Inputing msg
    msg = input("Enter MSG: ") # Getting msg input #

    """
    file=open("key.txt", "r") # opning key
    fileAPP=open("key.txt","a") # opning key for adding things
    arr=[]  
    arrord=[]
    arrordsplit=[]
    var=file.readline()

    for i in range(0,len(var)):
        arr.append(var[i])
        arrord.append(arr[i])
        for l in range(len(str(arrord[i]))):
            arrordsplit.append(str(arrord[i])[l])""" #old code if new idea no work

    
    file=open("key.txt", "r")
    arr=[] 
    fileAPP=open("key.txt","a") 

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
                        quit() 
                    
                    try:
                        
                                    
                        img1.putpixel((int(arr[i]),y), (r,g,b,0) )
                        print(img.getpixel((int(arr[i]),y)))
                        #print("arr spit ", arr[i])

                    except Exception as err: 

                        if(str(err)[0:23]=="list index out of range"):
                            #print("wow")
                            rand=randint(1,9)

                            for m in range(len(arr)):

                                # These need fixing
                                """if(arr[m]==rand):
                                    if((arr[m]+1)>=99):
                                        rand=randint(arr[m]-10,100)
                                    elif((arr[m]+1)<99):
                                        rand=randint(arr[m]+1,100)
                                    elif(arr[m]!=rand):
                                        pass

                                for n in range(len(arr)):
                                    if(arr[m]==arr[n]):
                                        arr[n]=randint(m+1,9)""" # old code
                                #new indea
                                


                            fileAPP.write( str(rand) )
                        elif(str(err)[0:23]!="list index out of range"):
                            #email err msg
                            pass

                   
                    #print(msgAsci)
                    n=n+1
                    i=i+1


    #save the img
    img1.save("images/YourEncodedImage.png")

inp=input("Type: ")
Clear()
if(inp=="1"):
    Decode()
else:
    Encode()
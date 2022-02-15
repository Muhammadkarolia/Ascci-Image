import threading
import os
import sys
from PIL import Image
from colorama import Fore, Style 
from time import sleep
from random import randint
from functools import lru_cache

Blue = Fore.BLUE
Red = Fore.RED
LightBlue = Fore.LIGHTBLUE_EX
Yellow = Fore.YELLOW
LightGreen = Fore.LIGHTGREEN_EX
Magenta = Fore.MAGENTA
Green = Fore.GREEN
Reset = Style.RESET_ALL
Dim = Style.DIM


Clear = lambda: os.system("clear" if os.name == "nt" "cls" else "clear")
Active = False # This is for the loading screen
# When loading screen is active this will be true
# Used in: "LoadingScreen" and "inp == 3"

def Slect(InBase): # InBase is the files that are added by the user

    # Goes thorugh the base files and sees if the 
    for i in range(len(InBase)):
        if(os.path.isfile(InBase[i])):
            print(Yellow+str(i+1)+".%s" %(InBase[i]))
        else:
             print(Red+str(i+1)+".%s" %(InBase[i]))
        FinalI = i # So that we know what the last pass was.

    print(Green+"%d.Return to Home" %(FinalI+2)+Reset) # Will retren err if FinalI no exit
    # This will happen when there is no InBase files

# loding screen.
# Will always be runnig in the backrouns once inp == 3 has Run
def LoadingScreen():
    global Active
    Sym=["/","-", "\\", "|"]
    while(Active == True):
        for sym in Sym:
            print("Loading %s" % sym)
            sleep(0.25)
            Clear()

# This needs to be changed in to a massive Jason file
OwnAsc={
    "w": 11,
    "q": 10,
    "e": 12,
    "r": 13,
    "y": 15,
    "t": 14,
    "%": 43,
    "f": 21,
    "i": 17,
    "o": 18,
    "p": 19,

    "d": 20,
    "u": 16,
    "g": 22,
    "h": 23,
    "j": 24,
    "k": 25,
    "9": 3,
    ";": 27,
    "'": 28,
    "#": 29,

    "z": 30,
    "x": 31,
    "c": 32,
    "v": 33,
    "b": 34,
    "n": 35,
    "*": 46,
    ",": 37,
    ".": 38,
    "/": 39,

    "4": 1,
    "2": 2,
    "m": 36,
    "0": 4,
    "1": 5,
    "8": 6,
    "7": 7,
    "&": 45,
    "l": 26,

    "3": 9,
    "!": 40,
    "}": 54,
    "6": 0,
    "$": 42,
    "-": 49,
    "^": 44,
    "=": 52,
    "£": 41,
    "(": 47,
    "Q": 65,

    "<": 58,
    "+": 51,
    ")": 48,
    "{": 53,
    ":": 55,
    ">": 59,
    "_": 50,
    "~": 57,
    "5": 8,

    "?": 60,
    "[": 61,
    "]": 62,
    "a": 63,
    "Y": 70,
    "W": 66,
    "s": 64,
    "E": 67,
    "R": 68,

    "T": 69,
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
    "Z": 84,
    "K": 82,
    "L": 83,
    "@": 56,
    "M": 90,
    "N": 89,
    "C": 86,
    "V": 87,
    "B": 88,
    "J": 81,

    "X": 85,
}


@lru_cache(maxsize=50) 
def Read(path):

    pathSplit = path.split("/") # splits in to an array each of the file names
    if(len(pathSplit) == 1): # It is just to see if they are alredy at the base file
        return "BaseFile" #Send msg that they are at base file screen

    listt = [] # The path that is beofre 
    items = 0 # The ammount of items that the item is that we wont to remove
    WhatRemove = [] # what we are going to remove
    # This will rename the fiele to a rnd string 

    for i in range(len(path)): # The lenght of the path is string format
        listt.append(path[i]) # append evrey single charter as seprate item

    for index in range(len(listt)): # Now we find where the last "/" is in the arr
        if(listt[index] == "/"):
            items = index # Stores the index of the last "/"
    

    for i in range(items, len(listt)):
        WhatRemove.append(i) # Takes the indexs of the itesm to be remvoed

    for i in range(len(WhatRemove)):
        listt[WhatRemove[i]] = ":lfeTestinghi123hi321klo559lkobu@;./<ia" # Reaplces them items. Do not change

    for i in range(len(listt)):
        try:
            listt.remove(":lfeTestinghi123hi321klo559lkobu@;./<ia")
        except:
            break
    
    paf = ""
    for i in range(len(listt)):
        paf = paf+listt[i] #append the listt items to a string

    return paf



def FileSlect(fileTopen, path, InBase): # pramters can be traced easly 
    path = fileTopen+"/"
    print(LightBlue+path)
    path = str()
    FilesInslected = os.listdir(fileTopen)


    for i in range(len(FilesInslected)):
        if(os.path.isfile(fileTopen+"/"+FilesInslected[i]) == True): # if the folder is a file 
            print(Yellow+str(i+1)+"."+FilesInslected[i]+Reset) # use yellow colour

        elif(os.path.isdir(fileTopen+"/"+FilesInslected[i]) == True): # else use red colour
            print(Red+str(i+1)+"."+FilesInslected[i]+Reset)
        iii = i # Take the last itration of i 

    print(Reset+str(iii+2)+".Go back")
    sys.stdout.write("Write the number of the option --> ")
    
    # Self explantory
    while True:
        try:
            FileSlected = int(input(Magenta))
            if(len(os.listdir(fileTopen))+1<FileSlected or FileSlected<0):
                print(Red)
                sys.stdout.write("Please entre a valid number:")
            else:
                break

        except Exception as err: 
            if(str(err)[0:len("invalid literal for int() with base 10:")] == "invalid literal for int() with base 10:"):
                print(Red)
                sys.stdout.write("Please entre a number:")

    # Needs to be +2(the iii)
    if(FileSlected == iii+2): # if you dont understand then... what the hell, you are stupid

        path = Read(fileTopen) # Rollbacks the file
        if(path == "BaseFile"): # If at base file then:
            Clear()
            Slect(InBase) # Shows base slection screen.
            sys.stdout.write("Write the number of your option --> ")
            path = "BaseFile" # At base files
            return path # if At Base file then 
            
    elif(FileSlected<iii+3 or FileSlected>1): # Agin this is self explantory
        FileSel = FilesInslected[FileSlected-1]
        path = fileTopen+"/"+FileSel    

    if(os.path.isdir(path)):
        if(len(os.listdir(path)) == 0):
            Clear()
            print(Reset+"This folder is empty")
            path = fileTopen
            FileSlect(path,path, InBase)
            return path
            

        elif(len(os.listdir(path))>0):
            Clear()
            path = FileSlect(path, path, InBase)
            return path

    elif(os.path.isfile(path)):
        name, ext = os.path.splitext(path) # Splits the last item in the path to its name and ext
        if(ext!=".png"):
            print(Reset+"This is not a png file")
            input("press any key to continue")
            path = Read(path) # Remove the last item
            Clear()
            FileSlect(fileTopen, path, InBase)
            return path
        else:
            return path 



def Decode(OwnAsc):
    file = open("MeassageResived.txt", "w")

    file = open("AppFiles/key.txt", "r") # opning the file #

    # Itrates trough each item in file
    LinesInFile = []
    for lines in file.readlines():
        for i in range(len(lines)):
            LinesInFile.append(lines[i])

    # goes through the string charter by charter and adds it to the arry
    #for i in range(0,len(LinesInFile)):

    file.close()

    InBase = [] # the amount of InBase files in the base
    FileInBase = os.listdir() # All the files
    for i in range(len(FileInBase)):
        if(os.path.isfile(FileInBase[i]) == True):
            f, ext = os.path.splitext(FileInBase[i])
            if(ext == ".png"):
                InBase.append(FileInBase[i])

        elif(os.path.isdir(FileInBase[i]) == True):
            f, ext = os.path.splitext(FileInBase[i])
            if(f == ".upm" or f == ".git"):
                continue
            else:
                InBase.append(FileInBase[i])


    #Welcome to the decoding side. 
    print(Magenta+"Welcome to the decoding side of this application.\n"+LightBlue+"NAVAGATE "+Reset +"the files to find the image you want to decode. A folder will apper red and and a non folder will be yellow")
    for i in range(len(InBase)):
        if(os.path.isfile(InBase[i]) == True):
            print(Yellow+str(i+1)+".%s" %(InBase[i]))
        else:
            print(Red+str(i+1)+".%s" %(InBase[i]))
        FinalI = i

    print(Green+"%d.Return to Home" %(FinalI+2)+Reset)



    sys.stdout.write("Write the number before the file you want to slect: ")

    while True:
        while True:
            try:
                FileSlected = int(input(Magenta))
                if(FileSlected == 0):
                    None+None
                FileSlected += -1
                break
            except Exception as err:
                if(str(err)[0:len("invalid literal for int() with base 10:")] == "invalid literal for int() with base 10:"):
                    print(Red)
                    sys.stdout.write("Please entre a number: ")
                elif( str(err)[0: 60] == "unsupported operand type(s) for +: 'NoneType' and 'NoneType'"):
                    print(Red)
                    sys.stdout.write("Please entre a valid number: ")
        

        if(FileSlected < len(InBase) and FileSlected >= 0):
            if(os.path.exists(InBase[FileSlected])):
                if(os.path.isfile(InBase[FileSlected])):
                    Name, Ext = os.path.splitext( InBase[FileSlected] )
                    if(Ext == ".png"):
                        imgDecode = Image.open( InBase[FileSlected] )
                        Clear()
                        break
                    else:
                        print("This is not a png file. ")
                        sys.stdout.write("Please select a png file or a folder: ")
                else:
                    Clear()
                    path = ""
                    path = FileSlect(InBase[FileSlected], path, InBase)
                    if(path != "BaseFile"):
                        imgDecode = Image.open(path)
                        break


    # Finding the ammount of pixels in the image which have a Alpah value of 0
    # This is becouase them pixels have leters enocded in them
    # Whith the ammount of pixeks stored in a varible i know how many times to itrate through the for loop
    width, hight  =  imgDecode.size[0], imgDecode.size[1]
    RGBvalDA = imgDecode.convert("RGBA") #  convert to RGBA
    ranage = 0
    for y in range(hight):
        for x in range(width):
            r,g,b,a = RGBvalDA.getpixel((x,y))
            if(a == 0):
                ranage+=1

    RGBvalD = imgDecode.convert("RGB") #  convert to RGB

    #m = 0
    #n = 0
    msg = [] # this will open the array which will hold the measge
    

    y = 0
    i = 0
    index = 0
    isn = False
    while(i!=ranage):
        for keys in OwnAsc:
            if(LinesInFile[index] in OwnAsc.keys()): # needs a specfix index not i
                xx = OwnAsc[LinesInFile[index]]
                isn = False
                break
            elif(LinesInFile[index] == "\n"):
                y+=1
                isn = True
                break
                
        if(isn == False):
            r,g,b = RGBvalD.getpixel((xx,y))
            chrR = chr(r)
            chrG = chr(g)
            chrB = chr(b)
            msg.append(chrR)
            msg.append(chrG)
            msg.append(chrB)
            i+=1
        index+=1


    #print(arr.index("8212"))
    print(Reset)

    file = open("MeassageResived.txt", "w")
    #write the msg to file
    for i in range(len(msg)): # Leave as for i in range
        # Dont change to for item in msg
        if(msg[i]==chr(0)):
            continue
        else:
            file.write(msg[i])
        if(i == len(msg)): # Becouase of this line
            file.close()
            file = open("MeassageResived.txt", "r")
            break
    Clear()

    #prit out msg
    print("Your meassage reads\n-------------------------------\n",Yellow)
    for _ in range(len(msg)):
        sys.stdout.write(msg[_])
    print(Reset,"\n\n-------------------------------",Red)
    file.close()
    print("This msg is stored in the messages folder, in the MeassageResivedfile.",Reset)
    input("Press any key to countiue\t")
    print(Reset+"Returning to menu")
    IdontKnowWhatToCallThisVar = randint(0,1)
    if(IdontKnowWhatToCallThisVar == 0):
        sleep(0.5)
    else:
        sleep(0.75)
    Clear() # fucntion ends so it will automaticly go to main as is in Whilte true loop



# ENCODEING #




def Encode(OwnAsc):
    # Image # 
    img = Image.open("AppFiles/DontDelThisFile.png") # Opnning up the image #
    width, hight = img.size[0], img.size[1]
    img1 = Image.open("AppFiles/DontDelThisFile.png")

    #Inputing msg
    while True:
        msg = input("Enter MSG: ") # Getting msg input #
        if(len(msg) == 0):
            print(Red+"Please type something",Reset)
        else:
            break

    file = open("AppFiles/key.txt", "r")
    arr = [] 

    LinesInFile = []
    for lines in file.readlines():
        for i in range(len(lines)):
            LinesInFile.append(lines[i])

    for i in range(0,len(LinesInFile)):
        arr.append(LinesInFile[i])

    file.close()

    x = 0 # x #
    y = 0 # y #

    msgAsci = [] # Arry making # 

    for q in range(len(msg)):
        msgAsci.append(ord(msg[q]))

    #print(msg)
    n = 0


    # THIS NEEDS WORKING ON #
    # It takes the mod and div of the len(msg) and makes the thing that goes through the if statment
    F = len(msg)//3
    M = len(msg)%3

    if(F>0 and M>0):
        l = F+1
        
    elif(F>0 and M == 0):
        l = F
    elif(F == 0 and M>0):
        l = 1
    elif(F == 0 and M == 0):
        print("please enter somwthing\nRETURNING TO MENUE")
        Clear()
        return

    #l+=1
    i = 0
    addY = 0
    Broc = False
    for y in range(hight):
            for x in range(width):
                Broc = False
                if(n!=l):
                    #print("n ",n)
                    #print("i ",i)#
                    try:
                        r = msgAsci[3*n]
                        try:
                            g = msgAsci[(3*n)+1]
                            try:
                                b = msgAsci[(3*n)+2]
                            except:
                                b = 0
                        except:
                            g = 0
                            b = 0
                    except:
                        n=l
                        break
                        
                    if(y == hight and x == width):
                        print("MSG can not be fittied in this img")

                        #quit() Do somwthing hear
                    
                    try:
                        for key in OwnAsc:
                                
                            if(arr[i] in OwnAsc.keys()):
                                xx = int(OwnAsc[arr[i]])
                                break
                                #print("xx  =  ", xx)
                            elif(arr[i] == "\n"):
                                addY+=1
                                Broc = True
                                break 
                        else:
                            xx = int(arr[i])
                        if(Broc == False):
                            try:
                                img1.putpixel((xx,y+addY), (r,g,b,0) )
                                n+=1
                            except Exception as err:
                                print(Red+"ERR",err,Reset)
                                input("press enter to contiue")
                        #print(img.getpixel((int(arr[i]),y)))
                        #print("arr spit ", arr[i])

                    except Exception as err: 
                        print(Red,err)
                        if(str(err)[0:23] == "list index out of range"):
                            pass
                            #add items to key
                        else:
                            #email err msg
                            pass

                   
                    #print(msgAsci)
                    i+=1
    input("Press enter to return to Menu")

    #save the img
    img1.save("Encoded Image/Encoded Image.png")
    Clear()

abc = "asdfghjklzxcvbnmqwertyuiop" 
abcap = "QWERTYUIOPASDFGHJKLZXCVBNM" 
numbers = "1234567890" 
sym = "!£$%^&*()_+{}:@~?><,./;'#[]-= " 


def check(var, randGEN, lock):
    if(var[randGEN] in lock):
        return True
    else:
        return False

def genrator(var ,passes):
    randGEN = randint(0, len(var)-1)

    while True:
        if(check(var, randGEN, lock) == True):
            randGEN = randint(0,len(var)-1)
        else:
            lock.add( var[randGEN] )
            break
        if(passes == len(var)-1):
            break
        passes = passes+1

print("Welcome to the",LightBlue,"Image ENCODER ", Red , "\n1.Encode the Image",Blue, "\n2.Decode the image", LightGreen,"\n3.Genrate key",Blue+Dim,"\n4.Quit",Reset)
FirstPass = True



while True:
    if(FirstPass == False):
        print(Reset+"chose one of the options",LightBlue,"Image ENCODER ", Red , "\n1.Encode the Image",Blue, "\n2.Decode the image", LightGreen,"\n3.Genrate key",Blue+Dim,"\n4.Quit",Reset)
    FirstPass = False
    sys.stdout.write("Type the number hear: ")
    while True:
        try:
            inp = int(input(Magenta)) # try to see if number and other exsceptions
            break
        except Exception as err:
            Clear()
            if(str(err)[0:len("invalid literal for int() with base 10:")] == "invalid literal for int() with base 10:"):
                print(Reset+"chose one of the options",LightBlue,"Image ENCODER ", Red , "\n1.Encode the Image",Blue, "\n2.Decode the image", LightGreen,"\n3.Genrate key",Blue+Dim,"\n4.Quit",Reset+Red)
                sys.stdout.write("please entre a number: ")

    
    print(Reset)
    if(inp == 1):
        Clear()
        Encode(OwnAsc)
    elif(inp == 2):
        Clear()
        Decode(OwnAsc)
    elif(inp == 3):
        Clear()
        Active = True
        lock = threading.Thread(target = LoadingScreen)
        lock.start()

        # Generator #
        for y in range(100):
            passA = 0
            passAcap = 0
            passN = 0
            passS = 0
            lock = set()
            for x in range(99):
                rand = randint(0,16)
                #alfbet
                if(rand>5 and rand<10 and passA!=len(abc)-1): # 6,7,8,9
                    genrator(abc,passA)

                #numbers
                elif(rand<5 and rand>0 and passN!=len(numbers)-1 ): # 4,3,2,1
                    genrator(numbers,passN)

                #symbols
                elif( rand == 5 or rand == 10 or rand == 0 or rand == 11 and passS!=len(sym)-1): # 0, 5, 10, 11
                    genrator(sym,passS)

                #caps
                elif(rand>11 and passAcap!=len(abcap)-1): # 12, 13, 14, 15 , 16
                    genrator(abcap, passAcap)
                
                ListLock = list(lock)  
                if(x == 98 and y!=99):
                    #print("running")
                    ListLock.append("\n")
                    #print(ListLock)
                if(y == 0 and x == 0):
                    #print("y == 0")
                    file = open("AppFiles/key.txt", "w")
                else:
                    #print("y!=0")
                    file = open("AppFiles/key.txt", "a")
            for i in range(len(ListLock)):
                file.write(ListLock[i])
            file.close()
        Active = False
        sleep(1.5)
        input("Press enter to return to menu")
        Clear()
    elif(inp == 4):
        quit()
    else:
        print("number out of range Please try agin")
        sleep(1.5)
        Clear()
    
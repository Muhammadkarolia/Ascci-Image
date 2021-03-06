import threading
import os
import sys
from PIL import Image
from colorama import Fore, Style 
from time import sleep
from random import randint
from functools import lru_cache

Clear = lambda: os.system("clear" if os.name == "nt" "cls" else "clear")
Active = False # This is for the loading screen
# When loading screen is active this will be true
# Used in: "LoadingScreen" and "inp == 3"

def Slect(extra): # extra is the files that are added by the user
    print(Style.RESET_ALL+"Slect from the files:\n"+Fore.RED+"1.AppFiles\n2.DragTheImageToDecodeHear\n3.Encoded Image",Style.RESET_ALL) # Main files. Will always be there

    # Goes thorugh the base files and sees if the 
    for i in range(len(extra)):
        print(Fore.YELLOW+str(i+4)+".%s" %(extra[i])) # Will be yellow since user is not lilley to add foldders
        FinalI = i # So that we know what the last pass was.
    try:
        print(Fore.GREEN+"%d.Return to Home" %(FinalI+5)+Style.RESET_ALL) # Will retren err if FinalI no exit
        # This will happen when there is no extra files
    except:
        print(Fore.GREEN+"4.Return to Home"+Style.RESET_ALL)


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

    "4": 1,
    "2": 2,
    "9": 3,
    "0": 4,
    "1": 5,
    "8": 6,
    "7": 7,
    "5": 8,
    "3": 9,
    "6": 0,

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



def FileSlect(fileTopen, path, extra): # pramters can be traced easly 
    path = fileTopen+"/"
    print(Fore.LIGHTBLUE_EX+path)
    path = str()
    FilesInslected = os.listdir(fileTopen)


    for i in range(len(FilesInslected)):
        if(os.path.isfile(fileTopen+"/"+FilesInslected[i]) == True): # if the folder is a file 
            print(Fore.YELLOW+str(i+1)+"."+FilesInslected[i]+Style.RESET_ALL) # use yellow colour

        elif(os.path.isdir(fileTopen+"/"+FilesInslected[i]) == True): # else use red colour
            print(Fore.RED+str(i+1)+"."+FilesInslected[i]+Style.RESET_ALL)
        iii = i # Take the last itration of i 


    print(Style.RESET_ALL+str(iii+2)+".Go back")
    sys.stdout.write("Write the number of the option --> ")
    
    # Self explantory
    while True:
        try:
            FileSlected = int(input(Fore.MAGENTA))
            if(len(os.listdir(fileTopen))+1<FileSlected or FileSlected<0):
                print(Fore.RED)
                sys.stdout.write("Please entre a valid number:")
            else:
                break

        except Exception as err: 
            if(str(err)[0:len("invalid literal for int() with base 10:")] == "invalid literal for int() with base 10:"):
                print(Fore.RED)
                sys.stdout.write("Please entre a number:")

    # Needs to be +2(the iii)
    if(FileSlected == iii+2): # if you dont understand then... what the hell, you are stupid

        path = Read(fileTopen) # Rollbacks the file
        if(path == "BaseFile"):
            Clear()
            Slect(extra) # Shows the base slection screen.
            sys.stdout.write("Write the number of your option --> ")
            path = "BaseFile" # At base files
            return path # This part is confusing. BUT trace it properly and you will see the beuty of this
            # Essently the lines above show the user the UI
            # and when we hop back in to the Decoding func then the loop will loop back round and the user inp will be taken
            # This decrease run time
            
    elif(FileSlected<iii+3 or FileSlected>1): # Agin this is self explantory
        FileSel = FilesInslected[FileSlected-1]
        path = fileTopen+"/"+FileSel    

    if(os.path.isdir(path) == True):
        if(len(os.listdir(path)) == 0):
            Clear()
            print(Style.RESET_ALL+"This folder is empty")
            path = fileTopen
            FileSlect(path,path, extra)
            return path
            

        elif(len(os.listdir(path))>0):
            Clear()
            path = FileSlect(path, path, extra)
            return path

    elif(os.path.isfile(path) == True):
        name, ext = os.path.splitext(path) # Splits the last item in the path to its name and ext
        if(ext!=".png"):
            print(Style.RESET_ALL+"This is not a png file")
            input("press any key to continue")
            path = Read(path) # Remove the last item
            Clear()
            FileSlect(fileTopen, path, extra)
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

    extra = [] # the amount of extra files in the base
    FileInBase = os.listdir() # All the files
    for i in range(len(FileInBase)):
        if(os.path.isfile(FileInBase[i]) == True):
            f, ext = os.path.splitext(FileInBase[i])
            if(ext == ".png"):
                extra.append(FileInBase[i])


    #Welcome to the decoding side. 
    print(Fore.MAGENTA+"Welcome to the decoding side of this application.\n"+Fore.LIGHTBLUE_EX+"NAVAGATE "+Style.RESET_ALL +"the files to find the image you want to decode. A folder will apper red and and a non folder will be yellow")
    print(Fore.RED+"1.AppFiles\n2.DragTheImageToDecodeHear\n3.Encoded Image",Style.RESET_ALL)
    for i in range(len(extra)):
        print(Fore.YELLOW+str(i+4)+".%s" %(extra[i]))
        FinalI = i
        upperBound = i+4
        #print("upperBound",upperBound) 
    try:
        FinalI+1
    
    except Exception as err:
        if(str(err)[0:len("local variable 'FinalI' referenced before assignment")] == "local variable 'FinalI' referenced before assignment"):
            FinalI = -1
            upperBound = 4
    try:
        print(Fore.GREEN+"%d.Return to Home" %(FinalI+5)+Style.RESET_ALL)
    except:
        print(Fore.GREEN+"%d.Return to Home" %(4)+Style.RESET_ALL)


    sys.stdout.write("Write the number before the file you want to slect: ")

    while True:
        while True:
            try:
                FileSlected = int(input(Fore.MAGENTA))
                break
            except Exception as err:
                if(str(err)[0:len("invalid literal for int() with base 10:")] == "invalid literal for int() with base 10:"):
                    print(Fore.RED)
                    sys.stdout.write("Please entre a number: ")


        if(FileSlected == 1):
            Clear()
            path = str()
            if(len(os.listdir("AppFiles")) == 0):
                print(Fore.LIGHTBLUE_EX+"AppFiles/"+Style.RESET_ALL)
                print("There is noething in this file")
                input("Press any key to countiue")
                Clear()
                Slect(extra)
                sys.stdout.write("Write the number before the file you want to slect: ")

            else:
                path = FileSlect("AppFiles", path, extra)
                if(path!="BaseFile"):
                    imgDecode = Image.open(path) 
                    break

        elif(FileSlected == 2):
            Clear()
            path = str()

            if(len(os.listdir("DragTheImageToDecodeHear")) == 0):
                print(Fore.LIGHTBLUE_EX+"DragTheImageToDecodeHear/"+Style.RESET_ALL)
                print("There is noething in this file")
                input("Press any key to countiue")
                Clear()
                Slect(extra)
                sys.stdout.write("Write the number before the file you want to slect: ")

            else:
                path = FileSlect("DragTheImageToDecodeHear", path, extra)
                if(path!="BaseFile"):
                    imgDecode = Image.open(path) 
                    break

        elif(FileSlected == 3):
            Clear()
            path=str()
            if(len(os.listdir("Encoded Image")) == 0):
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
        elif(FileSlected == FinalI+5):
            print(Style.RESET_ALL)
            Clear()
            return
        elif(FileSlected<=upperBound and FileSlected>3):
            #print("ran")
            imgDecode = Image.open(extra[FileSlected-4])
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
    print(Style.RESET_ALL)

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
    print("Your meassage reads\n-------------------------------\n",Fore.YELLOW)
    for _ in range(len(msg)):
        sys.stdout.write(msg[_])
    print(Style.RESET_ALL,"\n\n-------------------------------",Fore.RED)
    file.close()
    print("This msg is stored in the messages folder, in the MeassageResivedfile.",Style.RESET_ALL)
    input("Press any key to countiue\t")
    print(Style.RESET_ALL+"Returning to menu")
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
            print(Fore.RED+"Please type something",Style.RESET_ALL)
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
                                print(Fore.RED+"ERR",err,Style.RESET_ALL)
                                input("press enter to contiue")
                        #print(img.getpixel((int(arr[i]),y)))
                        #print("arr spit ", arr[i])

                    except Exception as err: 
                        print(Fore.RED,err)
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

print("Welcome to the",Fore.LIGHTBLUE_EX,"Image ENCODER ", Fore.RED , "\n1.Encode the Image",Fore.BLUE, "\n2.Decode the image", Fore.LIGHTGREEN_EX,"\n3.Genrate key",Fore.BLUE+Style.DIM,"\n4.Quit",Style.RESET_ALL)
FirstPass = True



while True:
    if(FirstPass == False):
        print(Style.RESET_ALL+"chose one of the options",Fore.LIGHTBLUE_EX,"Image ENCODER ", Fore.RED , "\n1.Encode the Image",Fore.BLUE, "\n2.Decode the image", Fore.LIGHTGREEN_EX,"\n3.Genrate key",Fore.BLUE+Style.DIM,"\n4.Quit",Style.RESET_ALL)
    FirstPass = False
    sys.stdout.write("Type the number hear: ")
    while True:
        try:
            inp = int(input(Fore.MAGENTA)) # try to see if number and other exsceptions
            break
        except Exception as err:
            Clear()
            if(str(err)[0:len("invalid literal for int() with base 10:")] == "invalid literal for int() with base 10:"):
                print(Style.RESET_ALL+"chose one of the options",Fore.LIGHTBLUE_EX,"Image ENCODER ", Fore.RED , "\n1.Encode the Image",Fore.BLUE, "\n2.Decode the image", Fore.LIGHTGREEN_EX,"\n3.Genrate key",Fore.BLUE+Style.DIM,"\n4.Quit",Style.RESET_ALL+Fore.RED)
                sys.stdout.write("please entre a number: ")

    
    print(Style.RESET_ALL)
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
    
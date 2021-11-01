file=open("test.txt", "r") # opning the file #
arr=[] # declaring intaila array to house

# declaring the Variable that will hold the Key
# It also itrates trough each item in the text file and adds it to    the end of the string
LinesInFile=""
for line in open("test.txt").readlines(): 
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
#Lab project
#Abdullah AlQudaihi 
from math import sqrt
def main():
    print("starting")
    exit = False
    dict1 = {} #Assigning all global variables
    listAll = []
    listZ = []
    listX = []
    listY = []
    listId = []
    empty = 0
    count = 0
    pointX = 0
    pointY = 0
    pointZ = 0
    id = 0
    sumX = 0
    sumY = 0
    sumZ = 0
    while not exit: #program will run until it is false when user select exit option it will true and terminate the program
        menu()
        choice= int(input("Please select your choice: ")) # taking input of user
        while choice <= 0 or choice >= 8:       # validating for user not select option other then given 1 - 9             
            print("Error: Wrong option selected!")
            choice= int(input("Enter Your Choice: "))
        if choice == 1: 
            addPoint(count,listX,listY,listZ,listAll,listId,dict1,empty,pointX,pointY,pointZ,id,sumX,sumY,sumZ)
        if choice == 2:
            deletePoint(listId,dict1,count,listX,listY,listZ,sumX,sumY,sumZ)
        if choice == 3:
            editPoint(listId,dict1,listX,listY,listZ,listAll,empty,count)
        if choice == 4:
            displayPoint()
        if choice == 5:
            centriodCalc(sumX,sumY,sumZ,count,listX,listY,listZ)
        if choice == 6:
            distance(sumX,sumY,sumZ,centroidX,centroidY,centroidZ,listX,listY,listZ)
        if choice == 7:
            exit = True


def menu():
    print("-"*65)
    print("                  Centroid Calculator     ")
    print("1. Add a new point")
    print("2. Delete a point")
    print("3. Edit a point")
    print("4. Display all points entered with ID.")
    print("5. Calculate all points and display the centroid.")
    print("6. Display the distance.")
    print("7. Exit.")
    print("-"*65)


    

def addPoint(count,listX,listY,listZ,listAll,listId,dict1,empty,pointX,pointY,pointZ,id,sumX,sumY,sumZ):
    outfile = open("data.txt","w") #opening the data file for writing
    outfile.truncate(0) #clearing the file each time the function is called
    pointX = input("Enter an x coordinate:  ") #Taking input for X coordinate
    pointY = input("Enter a y coordinate: ") #Taking input for Y coordinate
    pointZ = input("Enter a z coordinate: ") #Taking input for Z coordinate
    if pointX == "" or pointX == " ": #If an empty string is entered or a space set the value to 0
        pointX = 0
        empty = ""
    if pointY == "" or pointY == " ":
        pointY = 0
        empty = ""
    if pointZ == "" or pointZ == " ":
        pointZ = 0
        empty = ""  
    if empty != "": #Skipping the if conditions inside if value = 0
        if pointX.isdigit(): #Checking if the value is a digit and converting it into a float
            pointX = float(pointX)
        if pointY.isdigit():
            pointY = float(pointY)
        if pointZ.isdigit():
            pointZ = float(pointZ)
    id = input("Enter an id for the point: ") #Taking the input for the id for the point
    if id in listId: #Checking if the id is unique
        print("This id has already been taken.")
    else: 
        listId.append(id) #Adding each value to a global list
        listX.append(pointX) 
        listY.append(pointY) 
        listZ.append(pointZ)
        listAll.append(pointX)
        listAll.append(pointY)
        listAll.append(pointZ)
        dict1[id] = (pointX,pointY,pointZ) #Creating a dictonary for each point
        print("The point has been added successfully!")
        count = 0
        for i in listX:
            count += 1
        print(count)
        sumX = sumX + pointX
        sumY = sumY + pointY
        sumZ = sumZ + pointZ
        outfile.write("coordination\n") #Writing in the file
        outfile.write("(x,y,z)\n")
        for i in range(count):
            x = str(listX[i])
            y = str(listY[i])
            z = str(listZ[i])
            outfile.write("%s\t%s\t%s\n"%(x,y,z))
        outfile.write("Point ID:\n")
        for j in range(count):
            stringId = str(listId[j])
            outfile.write("%s\n"%stringId)
        outfile.write("# of points:\n")
        stringCount = str(count)
        outfile.write("%s"%stringCount)
        outfile.close()
    print(sumX)


def deletePoint(listId,dict1,count,listX,listY,listZ,sumX,sumY,sumZ): #A function for deleting a point
    idDelete = input("Enter the id you wish to be deleted: ") #Choosing which id the user wishes to be deleted
    if idDelete in listId: #Checking if the id is in the list
        outfile = open("data.txt","w") #opening the data file for writing
        outfile.truncate(0)
        toDelete = listId.index(idDelete)
        listId.remove(idDelete)
        x = listX[toDelete]
        y = listY[toDelete]
        z = listZ[toDelete]
        dict1.pop(idDelete)
        listX.pop(toDelete)
        listY.pop(toDelete)
        listZ.pop(toDelete)
        sumX = 0
        sumY = 0
        sumZ = 0
        for i in listX:
            sumX += i
        for j in listY:
            sumY += j
        for k in listZ:
            sumZ += k
        print("The point has been deleted successfully!")
        for i in listX:
            count += 1
        outfile.write("coordination\n") #Writing in the file
        outfile.write("(x,y,z)\n")
        for i in range(count):
            x = str(listX[i])
            y = str(listY[i])
            z = str(listZ[i])
            outfile.write("%s\t%s\t%s\n"%(x,y,z))
            outfile.write("Point ID:\n")
        for j in range(count):
            stringId = str(listId[j])
            outfile.write("%s\n"%stringId)
            outfile.write("# of points:\n")
            stringCount = str(count)
            outfile.write("%s"%stringCount)
            outfile.close()
        print(sumX)
        print(count)
    else:
        print("This id is not available: ") 


        
        
        
def editPoint(listId,dict1,listX,listY,listZ,listAll,empty,count): #A function to edit a point
    idEdit = input("Enter the id you wish to edit: ")
    if idEdit in listId: #Checking if the id is in the list
        outfile = open("data.txt","w") 
        outfile.truncate(0) 
        placeId = listId.index(idEdit)
        listId.remove(idEdit)
        dict1.pop(idEdit)
        listX.pop(placeId)
        listY.pop(placeId)
        listZ.pop(placeId)
        pointX = input("Enter an x coordinate:  ")
        pointY = input("Enter a y coordinate: ")
        pointZ = input("Enter a z coordinate: ")
        if pointX == "" or pointX == " ": #If an empty string is entered or a space set the value to 0
            pointX = 0
            empty = ""
        if pointY == "" or pointY == " ":
            pointY = 0
            empty = ""
        if pointZ == "" or pointZ == " ":
            pointZ = 0
            empty = ""  
        if empty != "": #Skipping the if conditions inside if value = 0
            if pointX.isdigit(): #Checking if the value is a digit and converting it into a float
                pointX = float(pointX)
            if pointY.isdigit():
                pointY = float(pointY)
            if pointZ.isdigit():
                pointZ = float(pointZ)
        id = idEdit
        listId.append(id)
        listX.append(pointX) 
        listY.append(pointY) 
        listZ.append(pointZ)
        listAll.append(pointX)
        listAll.append(pointY)
        listAll.append(pointZ)
        dict1[id] = (pointX,pointY,pointZ)
        sumX = 0
        sumY = 0
        sumZ = 0
        count = (listId.index(id)+1)
        for i in listX:
            sumX += i
        for j in listY:
            sumY += j
        for k in listZ:
            sumZ += k
        print("The point has been edited successfully!")
        outfile.write("coordination\n") #Writing in the file
        outfile.write("(x,y,z)\n")
        for i in range(count):
            x = str(listX[i])
            y = str(listY[i])
            z = str(listZ[i])
            outfile.write("%s\t%s\t%s\n"%(x,y,z))
        outfile.write("Point ID:\n")
        for j in range(count):
            stringId = str(listId[j])
            outfile.write("%s\n"%stringId)
        outfile.write("# of points:\n")
        stringCount = str(count)
        outfile.write("%s"%stringCount)
        outfile.close()
        print(sumX)
        print(count)
    else:
        print("You have entered a id that doesn't exist.")


def displayPoint():
    f = open("data.txt","r")
    fContent = f.read()
    print(fContent)
    f.close()




def centriodCalc(sumX,sumY,sumZ,count,listX,listY,listZ): #A fucnction to calculate the centroid of the points
    global centroidX #Making them global variables so we can use them in the distance function
    global centroidY 
    global centroidZ
    sumX = 0
    sumY = 0
    sumZ = 0
    count = 0
    for i in listX:
        count +=1
    for i in listX:
        sumX += i
    for j in listY:
        sumY += j
    for k in listZ:
        sumZ += k 
    print(sumX)
    print(count)
    centroidX = sumX / count
    centroidY = sumY / count
    centroidZ = sumZ / count
    print("Centroid = (%.2f,%.2f,%.2f)"%(centroidX,centroidY,centroidZ))


def distance(sumX,sumY,sumZ,centroidX,centroidY,centroidZ,listX,listY,listZ): #A function to get the distance between the points and the centroid
    sumX = 0
    sumY = 0
    sumZ = 0
    count = 0
    for i in listX:
        count +=1
    for i in listX:
        sumX += i
    for j in listY:
        sumY += j
    for k in listZ:
        sumZ += k 
    distance = sqrt(((sumX-centroidX)**2)+((sumY-centroidY)**2)+((sumZ-centroidZ)**2))
    print("Distance = %.2f"%distance)




main() #Calling the main function

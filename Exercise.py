import json
import time

def savedata(name, age, passcode) :
    user = False
    with open("exercise.json") as f : 
        file_data = json.load(f)
    for i in file_data : 
        for j in i.values() :
            if j == name : 
                user = True
                
    if user == False : 
        with open("exercise.json", "w") as writedata : 
            file_data.append({"name" : name, "age" : age, "passcode" : passcode})
            json.dump(file_data, writedata, indent=2)
        time.sleep(0.5)
        print("Data Saved!")
    else : 
        time.sleep(0.5)
        print("The user is already registered!")
        
def editdata(name) : 
    user = False
    with open("exercise.json") as f : 
        file_data = json.load(f)
    
    time.sleep(0.5)
    print("Searching for records....................")
    time.sleep(0.5)
    for i in file_data : 
        for j in i.values() :
            if j == name : 
                print("User found in the records!")
                time.sleep(0.5)
                user = True
    
                
    if user == True :
        passcode = int(input("Enter your passcode : "))
        for x in range(len(file_data)) : 
            if file_data[x]["name"] == name :
                realpass = file_data[x]["passcode"]
                break
        if int(realpass) == passcode : 
            time.sleep(0.5)
            print("User verified!")
            time.sleep(1)
            useredit = int(input("What do you want to edit?\n1. Name\n2. Age\n3. Passcode\n"))
            time.sleep(1)
            if useredit == 1 : 
                new = input("Enter new name to be saved : ")
                file_data[x]["name"] = new
                with open("exercise.json", "w") as writing :
                    json.dump(file_data, writing, indent=2)
                print("Overwriting of data successful!")
            elif useredit == 2 : 
                new = int(input("Enter new age to be saved : "))
                file_data[x]["age"] = new
                with open("exercise.json", "w") as writing :
                    json.dump(file_data, writing, indent=2)
                print("Overwriting of data successful!")
            elif useredit == 3 : 
                new = int(input("Enter new passcode to be saved : "))
                file_data[x]["passcode"] = new
                with open("exercise.json", "w") as writing :
                    json.dump(file_data, writing, indent=2)
                print("Overwriting of data successful!")
            else : 
                print("Invalid choice :(")             
        else : 
            time.sleep(1)
            print("You entered the wrong passcode! Access denied.")
    else : 
        time.sleep(0.5)
        print(f"User with the name {name} not found in the records.")
            
time.sleep(1)
print("-----------------------------------------------------\nDo you want to :")
time.sleep(0.5)
print("1. Upload new data")
time.sleep(0.5)
print("2. Edit old data")
time.sleep(0.5)
print("3. Exit\n-------------------------------------------------------")
time.sleep(0.5)

choice = int(input())
time.sleep(1)

if choice == 1 : 
    a = input("Enter your name : ")
    b = int(input("Enter your age : "))
    c = input("Enter your passcode : ")
    if len(c) == 4 :
        c = int(c)
        savedata(a, b, c)
    else :
        print("Please choose a 4 digit password....")
elif choice == 2 : 
    a = input("Enter your name : ")
    editdata(a)






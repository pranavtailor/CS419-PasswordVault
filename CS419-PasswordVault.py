import tkinter as tk
import tkinter.font as font
from tkinter import *
import os
import json

root = tk.Tk()

HEIGHT = 500
WIDTH = 400

root.title("Password Locker")

# Creating initial login page
canvas = tk.Canvas(height = HEIGHT, width = WIDTH)
canvas.pack()

# Defining font
smallFont = font.Font(family='Helvtica', size=18)
bigFont = font.Font(family='Helvtica', size=24)

# Create Master Password page
def createMasterPass():
    # create window
    topCreateMasterPass = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topCreateMasterPass.title("Create Master Password")
    # Put Created Master Password into new text doc called MasterPass.txt
    # If master pass already exists, print error message
    def storeMasterPass():
        data = open('MasterPassword.txt', 'a')
        masterPassword = enterNewMasterPass_Entry.get()
        if not os.stat('MasterPassword.txt').st_size == 0:
            # Master Pass already exists pop up label (red)
            masterAlreadyExists_Label = tk.Label(topCreateMasterPass, text = "Master Password Already Exists", fg='#FF0000')
            masterAlreadyExists_Label.place(relx = .25, rely = .5, relwidth = .5, relheight = .1)
        else:
            data.write(masterPassword)
            data.close()
            topCreateMasterPass.destroy()
    
    
    # Create master password label
    createNewMasterPass_Label = tk.Label(topCreateMasterPass, text = "Create Master Password")
    createNewMasterPass_Label.place(relx = .1, rely = .1, relwidth = .8, relheight = .1)
    createNewMasterPass_Label['font'] = smallFont
    # Enter new master password entry
    enterNewMasterPass_Entry = tk.Entry(topCreateMasterPass)
    enterNewMasterPass_Entry.place(relx = .25, rely = .2, relwidth = .5, relheight = .1)
    # Submit button 
    createMasterPass_Button = tk.Button(topCreateMasterPass, text = "Submit", command = storeMasterPass)
    createMasterPass_Button.place(relx = .35, rely = .4, relwidth = .3, relheight = .1)
    
    # tips text
    tip1Text = 'TIPS:'
    tip2Text = '1. Make your Master Password something that you would remember.'
    tip3Text = '2. Make it secure by adding numbers, letters, and special characers'
    tip4Text = '3. Enjoy!'
    text_Label1 = tk.Label(topCreateMasterPass, text = tip1Text)
    text_Label1.place(relx = .25, rely = .7, relwidth = .5, relheight = .05)
    text_Label2 = tk.Label(topCreateMasterPass, text = tip2Text)
    text_Label2.place(relx = 0, rely = .8, relwidth = 1, relheight = .05)
    text_Label3 = tk.Label(topCreateMasterPass, text = tip3Text)
    text_Label3.place(relx = 0, rely = .85, relwidth = 1, relheight = .05)
    text_Label4 = tk.Label(topCreateMasterPass, text = tip4Text)
    text_Label4.place(relx = .01, rely = .9, relwidth = .2, relheight = .05)

# newEntry page for inputting new entry into passwords.json
def newEntry():
    topNewEntry = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topNewEntry.title("New Entry")
    # Put info in dictionary
    def storeData():
        software = software_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        if software != '' and username != '' and password != '':
            pass_dict[software] = [username, password]
            topNewEntry.destroy()
    # section 1 (what software is it)
    software_label = tk.Label(topNewEntry, text = "Software: ")
    software_label.place(relx = .1, rely = .1)
    software_label['font'] = smallFont
    software_entry = tk.Entry(topNewEntry)
    software_entry.place(relx = .4, rely = .1, relwidth = .4, relheight = .1)
    # section 2 what is username)
    username_label = tk.Label(topNewEntry, text = "Username: ")
    username_label.place(relx = .1, rely = .3)
    username_label['font'] = smallFont
    username_entry = tk.Entry(topNewEntry)
    username_entry.place(relx = .4, rely = .3, relwidth = .4, relheight = .1)
    # section 3 (what is password)
    password_label = tk.Label(topNewEntry, text = "Password: ")
    password_label.place(relx = .1, rely = .5)
    password_label['font'] = smallFont
    password_entry = tk.Entry(topNewEntry)
    password_entry.place(relx = .4, rely = .5, relwidth = .4, relheight = .1)
    # Enter button
    Enter_button = tk.Button(topNewEntry, text = "Enter", command = storeData)
    Enter_button.place(relx = .2, rely = .7, relwidth = .6, relheight = .2)


uName_StringVar = StringVar()
pWord_StringVar = StringVar()
softwareDNE_StringVar = StringVar()
# Retrieve Entry Page
def retrieveEntry():
    topRetrieveEntry = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topRetrieveEntry.title("Retrieve Entry")
    def getData():
        software = software2_entry.get()
        if software in pass_dict:
            username = pass_dict[software][0]
            password = pass_dict[software][1]
            uName_StringVar.set(username)
            pWord_StringVar.set(password)
            softwareDNE_StringVar.set("")
        else:
            uName_StringVar.set('')
            pWord_StringVar.set('')
            softwareDNE_StringVar.set("Software Does Not Exist")
        
        # Label to show username/password)
        showUser_label = tk.Label(topRetrieveEntry, textvariable = uName_StringVar)
        showUser_label.place(relx = .4, rely = .3)
        showUser_label['font'] = smallFont
        showPass_label = tk.Label(topRetrieveEntry, textvariable = pWord_StringVar)
        showPass_label.place(relx = .4, rely = .4)
        showPass_label['font'] = smallFont
        softwareDNE_Label = tk.Label(topRetrieveEntry, textvariable = softwareDNE_StringVar, fg='#FF0000')
        softwareDNE_Label.place(relx = .3, rely = .6, relwidth = .4, relheight = .1)
    # Section 1 (what software is it)
    software2_label = tk.Label(topRetrieveEntry, text = "Software: ")
    software2_label.place(relx = .1, rely = .1)
    software2_label['font'] = smallFont
    software2_entry = tk.Entry(topRetrieveEntry)
    software2_entry.place(relx = .4, rely = .1, relwidth = .4, relheight = .1)
    # Username and password tag in front of where credentials will show up
    UserTag_Label = tk.Label(topRetrieveEntry, text = "Username: ")
    UserTag_Label.place(relx = .1, rely = .3)
    UserTag_Label['font'] = smallFont
    UserPass_Label = tk.Label(topRetrieveEntry, text = "Password: ")
    UserPass_Label.place(relx = .1, rely = .4)
    UserPass_Label['font'] = smallFont
    # Enter button
    Enter2_button = tk.Button(topRetrieveEntry, text = "Enter", command = getData)
    Enter2_button.place(relx = .2, rely = .7, relwidth = .6, relheight = .2)


# Page with 'New Entry' and 'Retrieve Entry' buttons
def homePageAfterEnter():
    # create window
    homePage = tk.Toplevel(height = HEIGHT, width = WIDTH)
    homePage.title("Password Locker")
    # Welcome label
    welcome_Label = tk.Label(homePage, text = "Welcome to Password Locker!")
    welcome_Label.place(relx = .05, rely = .05, relwidth = .9, relheight = .1)
    welcome_Label['font'] = smallFont
    # New Entry button
    newEntry_Button = tk.Button(homePage, text = "New Entry", command = newEntry)
    newEntry_Button.place(relx = .25, rely = .3, relwidth = .5, relheight = .1)
    newEntry_Button['font'] = smallFont
    # Retrieve Entry button
    retrieveEntry_Button = tk.Button(homePage, text = "Retrieve Entry", command = retrieveEntry)
    retrieveEntry_Button.place(relx = .25, rely = .5, relwidth = .5, relheight = .1)
    retrieveEntry_Button['font'] = smallFont
    
    # load json file into python dictionary
    global pass_dict
    try:
        pass_file = open('passwords.json', 'r')
        pass_dict = json.load(pass_file)
        pass_file.close()
    except FileNotFoundError:
        pass_dict = {}

    # called when homePage is closed
    def on_closing_home():
        pass_file = open('passwords.json', 'w')
        json.dump(pass_dict, pass_file, indent=4)
        pass_file.close()

        homePage.destroy()

    homePage.wm_protocol("WM_DELETE_WINDOW", on_closing_home)

    

# check if master password entered is correct
def checkMasterPassToLogin():
    data = open('MasterPassword.txt', 'r')
    masterPass = data.read()
    inputtedMasterPass = enterMasterPass_Entry.get()
    if inputtedMasterPass != masterPass:
        incorrectMaster_Label = tk.Label(canvas, text = "Incorrect Master Password", fg='#FF0000')
        incorrectMaster_Label.place(relx = .25, rely = .45, relwidth = .5, relheight = .1)
    elif inputtedMasterPass == masterPass:
        homePageAfterEnter()

    data.close()

# Checks the strength of the password by checking for variation of character in the password
def PassStrengthChecker():
    #Creates window
    topRetrieveEntry = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topRetrieveEntry.title("Password Strength Checker")
    def PasswordCalculator():
        Password = Password_Entry.get()
        score = 0
        score += (len(Password) * 4)
        lowercase = 0
        uppercase = 0
        number = 0
        miscchar = 0
        #Scans the password and adds points based off of the character types
        for character in Password:
            if character in "abcdefghijklmnopqrstuvwxyz":
                score += 2
                lowercase = 1
            elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                score += 2
                uppercase = 1
            elif character in "0123456789":
                score += 2
                number = 1
            elif character in "!@#$%^&*()-_`~?,.<>;:'+=/{}[]|":
                score += 2
                miscchar = 1
            else: score += 0 #Letter not found using our set of characters to scan for. Ignore key
        for character1, character2 in zip(Password, Password[1:]):
            if character1 == character2:
                score -= len(Password)
        #Checks for missing character types, subtracts points if none are in the password
        if lowercase == 0:
            score -= len(Password)
        if uppercase == 0:
            score -= len(Password)
        if number == 0:
            score -= len(Password)
        if miscchar == 0:
            score -= len(Password)
        #Grades score and returns strength based off of the score
        if score < 0:
            passStr = ("Very Weak Password!")
        elif score < 20:
            passStr=("Weak Password!")
        elif score < 50:
            passStr=("Strong Password!")
        else:
            passStr=("Very Strong Password")
        Passwordstrength = tk.Label(topRetrieveEntry, text=passStr)
        Passwordstrength.place(relx=.15, rely=.6, relwidth=.7, relheight=.05)
        Passwordscore = tk.Label(topRetrieveEntry, text=score)
        Passwordscore.place(relx=.15, rely=.65, relwidth=.7, relheight=.05)

    # Creates password checker label
    PasswordStrengthTest_Label = tk.Label(topRetrieveEntry, text="Enter password to be checked")
    PasswordStrengthTest_Label.place(relx=.1, rely=.1, relwidth=.85, relheight=.1)
    PasswordStrengthTest_Label['font'] = smallFont
    # Creates box to enter password to be checked
    Password_Entry = tk.Entry(topRetrieveEntry)
    Password_Entry.place(relx=.25, rely=.2, relwidth=.5, relheight=.1)
    # Submit password button
    PasswordStrengthTest_Button = tk.Button(topRetrieveEntry, text="Submit", command=PasswordCalculator)
    PasswordStrengthTest_Button.place(relx=.35, rely=.4, relwidth=.3, relheight=.1)
    tip = "Do not enter your own password into this box!"
    tip1 = "Use all sorts of characters like:"
    tip2 = "lowercase, uppercase, numbers, and even special characters!"
    text_Label1 = tk.Label(topRetrieveEntry, text=tip)
    text_Label1.place(relx = .15, rely = .7, relwidth = .7, relheight = .05)
    text_Label2 = tk.Label(topRetrieveEntry, text=tip1)
    text_Label2.place(relx = .15, rely = .75, relwidth = .7, relheight = .05)
    text_Label3 = tk.Label(topRetrieveEntry, text=tip2)
    text_Label3.place(relx = .025, rely = .8, relwidth = 1, relheight = .05)



# Login page (in canvas)
# Functionality: Login, Set master password
# Enter Master password label
enterMasterPass_Label = tk.Label(canvas, text = "Enter Master Password: ")
enterMasterPass_Label.place(relx = .1, rely = .1, relwidth = .8, relheight = .1)
enterMasterPass_Label['font'] = bigFont
# Entry where you enter master password
enterMasterPass_Entry = tk.Entry(canvas)
enterMasterPass_Entry.place(relx = .25, rely = .2, relwidth = .5, relheight = .1)
# Submit button 
goMasterPass_Button = tk.Button(canvas, text = "Submit", command = checkMasterPassToLogin)
goMasterPass_Button.place(relx = .35, rely = .35, relwidth = .3, relheight = .1)
# First time user label
dontHaveMasterPass_Label = tk.Label(canvas, text="First time user?")
dontHaveMasterPass_Label.place(relx = .1, rely = .6, relwidth = .8, relheight = .1)
enterMasterPass_Label['font'] = smallFont
# Create master password button
dontHaveMasterPass_Button = tk.Button(canvas, text = "Create Master Password", command = createMasterPass)
dontHaveMasterPass_Button.place(relx = .2, rely = .7, relwidth = .6, relheight = .2)
#Test password Strength button
PasswordStrengthTest_Button = tk.Button(canvas, text = "Test Password Strength", command = PassStrengthChecker)
PasswordStrengthTest_Button.place(relx = .2, rely = .9, relwidth = .6, relheight = .1)




root.mainloop()
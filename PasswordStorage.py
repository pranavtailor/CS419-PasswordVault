import tkinter as tk
import tkinter.font as font

root = tk.Tk()

HEIGHT = 400
WIDTH = 300

root.title("Password Locker")

# New Entry page
def newEntry():
    topNewEntry = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topNewEntry.title("New Entry")

    # Put info in text doc
    def storeData():
        data = open('Passwords.txt', 'a')
        software = software_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        data.write(software + ': ' + username + ', ' + password + "\n")
        data.close()
        topNewEntry.destroy()

    # section 1 (what software is it)
    software_label = tk.Label(topNewEntry, text = "Software: ")
    software_label.place(relx = .1, rely = .1)
    software_label['font'] = myFont

    software_entry = tk.Entry(topNewEntry)
    software_entry.place(relx = .4, rely = .1, relwidth = .4, relheight = .1)

    # section 2 what is username)
    username_label = tk.Label(topNewEntry, text = "Username: ")
    username_label.place(relx = .1, rely = .3)
    username_label['font'] = myFont

    username_entry = tk.Entry(topNewEntry)
    username_entry.place(relx = .4, rely = .3, relwidth = .4, relheight = .1)

    # section 3 (what is password)
    password_label = tk.Label(topNewEntry, text = "Password: ")
    password_label.place(relx = .1, rely = .5)
    password_label['font'] = myFont

    password_entry = tk.Entry(topNewEntry)
    password_entry.place(relx = .4, rely = .5, relwidth = .4, relheight = .1)

    # Enter button
    Enter_button = tk.Button(topNewEntry, text = "Enter", command = storeData)
    Enter_button.place(relx = .2, rely = .7, relwidth = .6, relheight = .2)



# Retrieve Entry page
def retrieveEntry():
    topRetrieveEntry = tk.Toplevel(height = HEIGHT, width = WIDTH)
    topRetrieveEntry.title("Retrieve Entry")

    def getData():
        data = open('Passwords.txt', 'r')
        text = data.readlines()
        newList = []

        for line in text:
            newList.append(line.strip())

        software = software2_entry.get()

        for i in newList:
            firstWord = i.split(':')[0] 
            if firstWord == software:
                secondWord = i.split(':')[1]

        # Label to show username/password)
        username = secondWord.split(',')[0]
        password = secondWord.split(',')[1]

        showUser_label = tk.Label(topRetrieveEntry, text = username)
        showUser_label.place(relx = .35, rely = .3)
        showUser_label['font'] = myFont

        showPass_label = tk.Label(topRetrieveEntry, text = password)
        showPass_label.place(relx = .35, rely = .4)
        showPass_label['font'] = myFont


    # Section 1 (what software is it)
    software2_label = tk.Label(topRetrieveEntry, text = "Software: ")
    software2_label.place(relx = .1, rely = .1)
    software2_label['font'] = myFont

    software2_entry = tk.Entry(topRetrieveEntry)
    software2_entry.place(relx = .4, rely = .1, relwidth = .4, relheight = .1)


    # Username and password tag in front of where credentials will show up
    UserTag_Label = tk.Label(topRetrieveEntry, text = "Username: ")
    UserTag_Label.place(relx = .1, rely = .3)
    UserTag_Label['font'] = myFont

    UserPass_Label = tk.Label(topRetrieveEntry, text = "Password: ")
    UserPass_Label.place(relx = .1, rely = .4)
    UserPass_Label['font'] = myFont
    

    # Enter button
    Enter2_button = tk.Button(topRetrieveEntry, text = "Enter", command = getData)
    Enter2_button.place(relx = .2, rely = .7, relwidth = .6, relheight = .2)

    

# Defining font
myFont = font.Font(family='Helvtica', size=11)

# Entire footprint
canvas = tk.Canvas(height = HEIGHT, width = WIDTH)
canvas.pack()

# Main page buttons
button_new = tk.Button(canvas, text = "New Entry", command = newEntry)
button_new.place(relx = .3, rely = .3, relwidth = .4, relheight = .1)
button_new['font'] = myFont

button_retrieve = tk.Button(canvas, text = "Retrieve Entry", command = retrieveEntry)
button_retrieve.place(relx = .3, rely = .5, relwidth = .4, relheight = .1)
button_retrieve['font'] = myFont


root.mainloop()
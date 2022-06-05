import tkinter as Tk
import tkinter.ttk as ttk
import os

#check if file exists, if not create them
if not os.path.exists("cookie.txt"):
    with open("cookie.txt", "w") as f:
        f.write("0")
if not os.path.exists("multiplier.txt"):
    with open("multiplier.txt", "w") as f:
        f.write("1")









#Check if file exists



global counts

count = 0
reopen = True

#Read the value of the variable from the file
def read():
    global count
    global multiplier
    with open("cookie.txt", "r") as f:
        count = int(f.read())
    with open("multiplier.txt", "r") as f:
        multiplier = int(f.read())

read()


if(multiplier == 0):
    multiplier = 1
if(multiplier == ""):
    multiplier = 1




counts = count
count = counts

#Create a class


def click(self):
    global count
    global counts
    count += multiplier
    Self.label.config(text=count)

def close(self):
    global reopen
    reopen = False
    self.destroy()

def reset(self):
    global count
    global counts
    count = 0
    counts = 0
    self.label.config(text=count)

def upgrade():
    global multiplier
    global count
    if(count >= 100):
        multiplier += 1
        count -= 100
        print("You have upgraded your cookie production!")
        print("You now produce " + str(multiplier) + " cookies per click!")


#Create a window with title Cookie Clicker which has a button with a Cookie emoji with font size of 40"
main = Tk.Tk()
main.title("Cookie Clicker")
main.geometry("200x200")

#Set the variable to what is in the file
#with open("cookie.txt", "r") as f:
#    count = int(f.read())



#Create a button that when clicked increses a variable by 1 and displays the value in the label
def click():
    global count
    count += multiplier
    label.config(text=count)


#Create a label that displays the value of the variable
label = Tk.Label(main, text=count)
label.pack()

#Create a button that when clicked calls the click function
button = Tk.Button(main, text="🍪", command=click)
button.pack()

#Create a button that when clicked closes the window and saves the value of the variable to a file
def close():
    global count
    global multiplier
    with open("cookie.txt", "w") as f:
        f.write(str(count))
    with open("multiplier.txt", "w") as f:
        f.write(str(multiplier))
    main.destroy()
    


#Create a button that calls the close function
button2 = Tk.Button(main, text="Close", command=close)
button2.pack()

#Create a button that resets the variable and saves it to the file
def reset():
    global count
    global multiplier
    multiplier = 1
    count = 0
    with open("cookie.txt", "w") as f:
        f.write(str(count))
    label.config(text=count)
    

#Create a button that calls the reset function
button3 = Tk.Button(main, text="Reset", command=reset)
button3.pack()





#Create a button that calls the open function
button6 = Tk.Button(main, text="Upgrade 1, 100 Cookies", command=upgrade)
button6.pack()
#Start the main loop
main.mainloop() 	







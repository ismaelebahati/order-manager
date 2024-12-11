from tkinter import *
from datetime import datetime
import os


data ={} 

database = open("./kindabackend/coded_orders.txt", "r")
n = int(database.readline().strip())
for i in range (n):
    old = database.readline().strip().split()
    data[int(old[1])] = int(old[0])
database.close()

def convert(date_string):
    try:
        date_format = "%d/%m/%Y"
        given_date = datetime.strptime(date_string, date_format)
        start_date = datetime(2000, 1, 1)
        return (given_date - start_date).days
    except ValueError:
        return -1


win = Tk()
win.geometry("2000x2000")
win.configure(bg="white")
win.title("orgia_nizer")

indate = StringVar()
incode = StringVar() 
different = StringVar() 



def saveorder():
    database = open("./kindabackend/coded_orders.txt", "w")
    print(data)
    database.write(str(len(data)))
    database.write("\n")
    for key, el in data.items():
        database.write(str(el))
        database.write(" ")
        database.write(str(key))
        database.write("\n")
    database.close()


def getorder():
    realcode = incode.get()
    realdate = indate.get()
    incode.set("")
    indate.set("")
    days = convert(realdate)
    if (realcode.isnumeric() and int(realcode) <= 5000 and days !=-1):
        data[int(realcode)] = days
        error.pack_forget()
    else:
        error.pack()

def getorder2(event):
    getorder()

def callc():
    os.system("g++ ./kindabackend/optimization.cpp -o ./kindabackend/optimization.out")
    os.system("./kindabackend/optimization.out")
    getres()

results = {}

def getres():
    i=0
    supfile = open("./kindabackend/res.txt", "r")
    for line in supfile:
        line = line.strip().split()
        if int(line[0]) == -1:
            results[i] = [-1, []]
        else:
            results[i] = [int(line[0]),[]]
            j=1
            while j<= 3*len(data):
                results[i][1].append([line[j], line[j+1], line[j+2]])
                j+=3
        i += 1


def show():
    print(results)
    listbox.pack_forget()
    index = int(different.get())
    if (index>=len(results)):
        return
    listbox.delete(0, END)
    if (results[index][0] == -1):
        listbox.insert(1, "NOT POSSIBLE WITH ONLY THESE DAYS")
        listbox.pack()
        return
    j=1
    for thing in (results[index][1]):
        listbox.insert(j, str(thing[0]) +"  "+ str(thing[1] +" "+ str(thing[2])))

        j +=1
    listbox.pack()
win.bind("<Return>", getorder2)

##labels




title = Label(win,
              text="Insert an order or engagement",
              bg = "white",
              anchor = CENTER,
              font = ("Helvetica", 15),height=2, width=30
              )
error = Label(win,
              text="invalid input, remember to use specified format",
              bg = "white",
              fg = "red",
              anchor = CENTER,
              font = ("Helvetica", 15),height=2, width=60
              )
#err
#code

code = Label(win,
              text="insert the code (a number up to 5000)",
              bg = "white",
              anchor = CENTER,
              font = ("Helvetica", 12), fg="gray", height=2, width=50
              )

#date
date = Label(win,
              text="insert the date (with format gg/mm/yyyy e.g. 11/09/2001)",
              bg = "white",
              anchor = CENTER,
              font = ("Helvetica", 12), fg="gray", height=2, width=50
              )

#lista spedizioni
sped = Label(win,
              text="cacca fafad",
              bg = "white",
              anchor = CENTER,
              font = ("Monospace", 14), fg="gray", height=2, width=50
              )

##entry
code_entry = Entry(
    win,
    textvariable=incode,
    font = ("Helvetica", 15),  width=30
    
)
date_entry = Entry(
    win,
    textvariable=indate,
    font = ("Helvetica", 15),  width=30
    
)

diff_entry = Entry(
    win,
    textvariable=different,
    font = ("Helvetica", 15),  width=30
    
)



#submit button
button = Button(win, text = "Submit", font=("Helvetica", 15), command=getorder, height=2, width=8)
save = Button(win, text = "Save all orders", font=("Helvetica", 15), command=saveorder, bg="green", height=2, width=20)
elaborate = Button(win, text = "Elaborate all orders", font=("Helvetica", 15), command=callc, bg="blue", height=2, width=20)
update = Button(win, text = "refresh list", font=("Helvetica", 15), command=show, bg="yellow", height=2, width=20)

#listbox
listbox = Listbox(
                font = ("Helvetica", 14),
                bg = "gray",
)
## this is ugly styling but i will fix it later
getres()

title.pack(pady = 40)
code.pack(pady = 5)
code_entry.pack(pady=5)
date.pack(pady = 5)
date_entry.pack(pady=5)
button.pack(pady=40)
save.pack(pady=30)
elaborate.pack(pady=30)
sped.pack()
diff_entry.pack()
update.pack()



win.mainloop()
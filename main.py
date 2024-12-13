from tkinter import *
from data_manipulation import *

old_data_init()

light_gray = "#f1f0ed"
lilblue = "#f3f5f6"
lighter_gray = "#e9ebec"
dark_gray = "#5a5a5a"



win = Tk()
win.geometry("2000x2000")
win.configure(bg=lilblue)
win.title("orgia_nizer")



indate = StringVar()
incode = StringVar() 
indetails = StringVar() 
different = StringVar() 



def SHOW():
    show(listbox, sped, different, scrollbar)

def GETORDER():
    getorder(incode, indate, indetails, error)

def GETORDER2(event):
    GETORDER()


win.bind("<Return>", GETORDER2)

##labels


title = Label(win,
              text="Insert an order, duplicate code will substitute",
              bg = lilblue,
              anchor = CENTER,
              font = ("verdana", 15),height=1, width=70
              )

error = Label(win,
              text="invalid input, remember to use specified format",
              bg = lilblue,
              fg = "red",
              anchor = CENTER,
              font = ("verdana", 15),height=1, width=60
              )
#err
#code

code = Label(win,
              text="insert the code (a number up to 5000)",
              bg = lilblue,
              anchor = CENTER,
              font = ("verdana", 12), fg=dark_gray, height=1, width=50
              )

#date
date = Label(win,
              text="insert the date (with format gg/mm/yyyy e.g. 11/09/2001)",
              bg = lilblue,
              anchor = CENTER,
              font = ("verdana", 12), fg=dark_gray, height=1, width=50
              )

details = Label(win,
              text="insert text to describe details order",
              bg = lilblue,
              anchor = CENTER,
              font = ("verdana", 12), fg=dark_gray, height=1, width=50
              )

#lista spedizioni
sped = Label(win,
              text="codice     ex. data   sped. data      delay (in days)",
              bg = lighter_gray,
              width=1000,
              justify = CENTER,
              font = ("Monospace", 14), fg=dark_gray, height=2
              )

##entry
code_entry = Entry(
    win,
    textvariable=incode,
    font = ("verdana", 15),
    width=30
)
date_entry = Entry(
    win,
    textvariable=indate,
    font = ("verdana", 15),
    width=30
)
details_entry = Entry(
    win,
    textvariable=indetails,
    font = ("verdana", 15),
    width=30
)

diff_entry = Entry(
    win,
    textvariable=different,
    font = ("verdana", 15),  
    width=30
)

#listbox
listbox = Listbox(
                win,
                justify=CENTER,
                font = ("monospace", 14),
                bg = light_gray,
                width=1000
)
scrollbar = Scrollbar(win,
                      width=30) 
listbox.config(yscrollcommand = scrollbar.set) 
scrollbar.config(command = listbox.yview) 


#submit button
button = Button(win, text = "Submit", font=("verdana", 15), bg=light_gray,command=GETORDER, height=1, width=20)
save = Button(win, text = "Save all orders", font=("verdana", 15), command=saveorder, bg=light_gray, height=1, width=20)
elaborate = Button(win, text = "Elaborate all orders", font=("verdana", 15), command=callc, bg=light_gray, height=1, width=20)
update = Button(win, text = "refresh list", font=("verdana", 15), command=SHOW, bg=light_gray, height=1, width=20)




## this is ugly styling but i will fix it later
title.pack(pady = 60)
code.pack(pady = 5)
code_entry.pack(pady=5)
date.pack(pady = 5)
date_entry.pack(pady=5)
details.pack(pady = 5)
details_entry.pack(pady=5)
button.pack(pady=10)
save.pack(pady=10)
elaborate.pack(pady=10)
diff_entry.pack(pady=10)
update.pack(pady=10)




win.mainloop()
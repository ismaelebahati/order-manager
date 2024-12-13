from tkinter import *
from dateconv import *
import os


data ={} 
details = {}
results = {}


def old_data_init():
    data.clear() 
    details.clear()
    results.clear()

    database = open("./kindabackend/coded_orders.txt", "r")
    detailbase = open("./kindabackend/code_to_details.txt", "r")

    n = int(database.readline().strip())
    m = int(detailbase.readline().strip())

    for i in range (n):
        old = database.readline().strip().split()
        data[int(old[1])] = int(old[0])

    for i in range (m):
        old = detailbase.readline().strip().split(":")
        details[int(old[0])] = old[1]+" "

    database.close()
    detailbase.close()


def saveorder():
    database = open("./kindabackend/coded_orders.txt", "w")
    detailbase = open("./kindabackend/code_to_details.txt", "w")
    database.write(str(len(data)))
    database.write("\n")

    detailbase.write(str(len(data)))
    detailbase.write("\n")

    for key, el in data.items():
        database.write(str(el))
        database.write(" ")
        database.write(str(key)) 
        database.write("\n")

    for key, el in details.items():
        detailbase.write(str(key))
        detailbase.write(":")
        detailbase.write(str(el)) 
        detailbase.write("\n")

    database.close()
    detailbase.close()




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
                results[i][1].append([int(line[j]), int(line[j+1]), int(line[j+2])])
                j+=3
        i += 1


def show(listbox, sped, different, scrollbar):
    print(results)
    print(data)
    sped.pack_forget()
    scrollbar.pack_forget()
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
        listbox.insert(j, str(thing[0]).ljust(11) +
                        convert_back(thing[1]).ljust(11)+ 
                        convert_back(thing[2]).ljust(16)+
                        str(thing[2]-thing[1]).ljust(15)
                        )

        j +=1
    sped.pack()
    scrollbar.pack(side = RIGHT, fill = BOTH) 
    listbox.pack()


def getorder(incode, indate, indetails, error):
    realcode = incode.get()
    realdate = indate.get()
    realdetails = indetails.get()
    incode.set("")
    indate.set("")
    indetails.set("")
    days = convert(realdate)
    if (realcode.isnumeric() and int(realcode) <= 5000 and days !=-1):
        data[int(realcode)] = days
        details[int(realcode)] = realdetails
        error.pack_forget()
    else:
        error.pack()


def callc():
    os.system("g++ ./kindabackend/optimization.cpp -o ./kindabackend/optimization.out")
    os.system("./kindabackend/optimization.out")
    getres()

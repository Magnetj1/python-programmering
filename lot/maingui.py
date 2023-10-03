from tkinter import *
from tkinter import messagebox
import lot

print("funkar")
#create root window.
root = Tk()
root.title
root.geometry("1280x720")

#create listbox object
listbox = Listbox (root,height = 4, width=30, bg="white", activestyle="dotbox", font="helvetica", fg="red")
lotteri = lot.Lotteri()

#vinst = lotteri.get_vinst()
#print(f'vinst={vinst}')

label_antal = Label (root, text="antal lotter, max 3 st: ")
label_antal.grid(row=0,column=0, sticky=E,padx=5,pady=5)

textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1,sticky=W, padx=5,pady=5)

textbox_antal.focus_set()



def update_listbox(antal_lotter):
    #print("update_listbox")
    listbox.delete(0,END)
    listbox.insert(1, "Grattis du vann SEX")

    try:
        int_antal_lotter = int(antal_lotter)
        i=0

        if(int_antal_lotter < 4):
            while i<int_antal_lotter:
                vinst= lotteri.get_vinst()
                listbox.insert((i+2), vinst)
                i= i+1
        else:
            messagebox.showinfo("Du har valt för många latareorad!!!!")
    
    except ValueError:
        messagebox.showinfo("endast siffror tillåtet")

def clickSlumpsaButton():
    
    #print("clickSlumpsaButton")
    
    antal_lot = textbox_antal.get()
    textbox_antal.delete(0, END)
    textbox_antal.focus_set()
    update_listbox(antal_lot)
    #slut på funktioner()
 
button_slumpa = Button (text="tur knapp", command=clickSlumpsaButton)
button_slumpa.grid(row=1,column=0, columnspan=2,padx=15,pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)



root.mainloop()
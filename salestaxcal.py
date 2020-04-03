from tkinter import *

#Creating tkinter window 
root = Tk() 
root.title('Sales Tax Calculator')
root.geometry("300x350")

#Creating heading
lbl_heading = Label(root, text="Sales Tax Calculator", font=("arial",20))
lbl_heading.pack()

#Explain the program
price_lbl = Label(root, text="Price: ")
price_lbl.pack()

price_entry = Entry(root)
price_entry.pack()

tax_lbl = Label(root, text="Tax Rate%: ")
tax_lbl.pack()

tax_entry = Entry(root)
tax_entry.pack()

#Create tax function that takes price and tax_rate as inputs and return total
def calculate_tax():
    price_val= int(price_entry.get())
    tax_val= int(tax_entry.get())
    total = (price_val*tax_val)/100
    lbl = Label(root, text=f"The total price with tax is: {total}")
    lbl.pack()
               
cal_btn = Button(root,text="Calculate Tax", command=calculate_tax)
cal_btn.pack()

root.mainloop()

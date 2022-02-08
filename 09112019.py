from tkinter import *
import random
import time;
import mysql.connector as  sqlcon
mydb=sqlcon.connect(host="localhost",user="root",password="",
                    database="inventory_management")
mycur=mydb.cursor()

root=Tk()
root.geometry("1600x800+10+10")
root.title("Restaurant Management System")

text_Input=StringVar()
operator=""

Tops=Frame(root,width=1600,height=50,bg="blue",relief=FLAT)
Tops.pack(side=TOP)

f1=Frame(width=800,height=100,relief=FLAT)
f1.pack(side=LEFT)


#----------------------------------Time---------------------------------------------------------------------------------------------------------
localtime=time.asctime(time.localtime(time.time())) #Date Time Function
#-------------------------Head------------------------------------------------------------------------------------------------------------------
lblinfo=Label(Tops,font=('Magneto',50,'bold'),text="Restaurant Management System",
              fg="red",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lbldatetime=Label(Tops,font=('showcard gothic',20,'bold'),text=localtime,fg="Steel Blue",
                  bd=10,anchor='w')
lbldatetime.grid(row=1,column=0)

#----------------------------Functions----------------------------------------------------------------------------------------------------------

def Ref():
    x=random.randint(12908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    CoF=float(Fries.get())
    CoD=float(Drinks.get())
    CoFilet=float(Filet.get())
    CoBurger=float(Burger.get())
    CoChicBurger=float(Chicken_Burger.get())
    CoCheese_Burger=float(Cheese_Burger.get())

    CostofFries = CoF * 99
    CostofDrinks = CoD * 49
    CostofFilet = CoFilet * 299
    CostofBurger = CoBurger * 49
    CostChicken_Burger = CoChicBurger * 149
    CostCheese_Burger = CoCheese_Burger * 69

    CostofMeal="Rs.",str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger +CostChicken_Burger + CostCheese_Burger))

    PayTax= ((CostofFries + CostofDrinks + CostofFilet + CostofBurger +CostChicken_Burger + CostCheese_Burger)*0.05)

    TotalCost= (CostofFries + CostofDrinks + CostofFilet + CostofBurger +CostChicken_Burger + CostCheese_Burger)

    Ser_Charge= ((CostofFries + CostofDrinks + CostofFilet + CostofBurger +CostChicken_Burger + CostCheese_Burger)/99)

    Service= "Rs.", str('%.2f' % Ser_Charge)
    OverAllCost= "Rs.", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax= "Rs.", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")


#---------------------------------Entry Variables--------------------------------------------------------------------------
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Filet=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken_Burger=StringVar()
Cheese_Burger=StringVar()
Name=StringVar()
Phno=StringVar()

#---------------------------------Customer Info-----------------------------------------------------------------------------------------------

lblName=Label(f1,font=('showcard gothic',7,'bold'),
              text="Name",bd=7,anchor='w')
lblName.grid(row=0,column=0)
txtName=Entry(f1,font=('showcard gothic',7,'bold'),
              textvariable=Name,bd=10,insertwidth=4,bg="powder blue",justify="right")
txtName.grid(row=0,column=1)

lblPhno=Label(f1,font=('showcard gothic',7,'bold'),
              text="Phone Number",bd=7,anchor='w')
lblPhno.grid(row=0,column=2)
txtPhno=Entry(f1,font=('showcard gothic',7,'bold'),
              textvariable=Phno,bd=10,insertwidth=4,bg="powder blue",justify="right")
txtPhno.grid(row=0,column=3)             
#------------------------Labels and Entry------------------------------------------------------------------------------------------------

lblReference = Label(f1,font=('showcard gothic',7,'bold'),
                     text="Reference", bd=7)
lblReference.grid(row=1,column=0)
txtReference=Entry(f1,font=('showcard gothic',7,'bold'),
                   textvariable=rand, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtReference.grid(row=1,column=1)

lblFries = Label(f1,font=('showcard gothic',7,'bold'),
                 text="Large Fries", bd=7, anchor='w')
lblFries.grid(row=2,column=0)
txtFries=Entry(f1,font=('showcard gothic',7,'bold'),
               textvariable=Fries, bd=10, insertwidth=4 ,bg="powder blue", justify = "right")
txtFries.grid(row=2,column=1)

lblBurger = Label(f1,font=('showcard gothic',7,'bold'),
                  text="Burger Meal", bd=7, anchor='w')
lblBurger.grid(row=3,column=0)
txtBurger=Entry(f1,font=('showcard gothic',7,'bold'),
                textvariable=Burger, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtBurger.grid(row=3,column=1)

lblFilet = Label(f1,font=('showcard gothic',7,'bold'),
                 text="Filet_o_Meal", bd=7, anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet=Entry(f1,font=('showcard gothic',7,'bold'),
               textvariable=Filet, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtFilet.grid(row=4,column=1)

lblChicken = Label(f1,font=('showcard gothic',7,'bold'),
                   text="Chicken Meal", bd=7, anchor='w')
lblChicken.grid(row=5,column=0)
txtChicken=Entry(f1,font=('showcard gothic',7,'bold'),
                 textvariable=Chicken_Burger, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtChicken.grid(row=5,column=1)

lblCheese = Label(f1,font=('showcard gothic',7,'bold'),
                  text="Cheese Meal", bd=7, anchor='w')
lblCheese.grid(row=6,column=0)
txtCheese=Entry(f1,font=('showcard gothic',7,'bold'),
                textvariable=Cheese_Burger, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtCheese.grid(row=6,column=1)

lblDrinks = Label(f1,font=('showcard gothic',7,'bold'),
                  text="Drinks", bd=7, anchor='w')
lblDrinks.grid(row=1,column=2)
txtDrinks=Entry(f1,font=('showcard gothic',7,'bold'),
                textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtDrinks.grid(row=1,column=3)

lblCost = Label(f1,font=('showcard gothic',7,'bold'),
                text="Cost of Meal", bd=7, anchor='w')
lblCost.grid(row=2,column=2)
txtCost=Entry(f1,font=('showcard gothic',7,'bold'),
              textvariable=Cost, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtCost.grid(row=2,column=3)

lblService = Label(f1,font=('showcard gothic',7,'bold'),
                   text="Service Charge", bd=7, anchor='w')
lblService.grid(row=3,column=2)
txtService=Entry(f1,font=('showcard gothic',7,'bold'),
                 textvariable=Service_Charge, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtService.grid(row=3,column=3)

lblStateTax = Label(f1,font=('showcard gothic',7,'bold'),
                    text="State Tax", bd=7, anchor='w')
lblStateTax.grid(row=4,column=2)
txtStateTax=Entry(f1,font=('showcard gothic',7,'bold'),
                  textvariable=Tax, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtStateTax.grid(row=4,column=3)

lblSubTotal = Label(f1,font=('showcard gothic',7,'bold'),
                    text="Sub Total", bd=7, anchor='w')
lblSubTotal.grid(row=5,column=2)
txtSubTotal=Entry(f1,font=('showcard gothic',7,'bold'),
                  textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtSubTotal.grid(row=5,column=3)

lblTotalCost = Label(f1,font=('showcard gothic',7,'bold'),
                     text="Total Cost", bd=7, anchor='w')
lblTotalCost.grid(row=6,column=2)
txtTotalCost=Entry(f1,font=('showcard gothic',7,'bold'),
                   textvariable=Total, bd=10, insertwidth=4, bg="powder blue", justify = "right")
txtTotalCost.grid(row=5,column=3)

#-------------------------------------------------------Database-----------------------------------------------------------------

def insert():
    Reference1=txtReference.get()
    Name1=txtName.get()
    Phno1=txtPhno.get()
    Fries1=txtFries.get()
    Burger1=txtBurger.get()
    Filet1=txtFilet.get()
    Chicken1=txtChicken.get()
    Cheese1=txtCheese.get()
    Drinks1=txtDrinks.get()
    Cost1=txtCost.get()
    Service_charge1=txtService.get()
    Tax1=txtStateTax.get()
    Subtotal1=txtSubTotal.get()
    Total_cost1=txtTotalCost.get()
    
    mycur.execute("""INSERT INTO db VALUES("%s","%s","%s","%s","%s","%s","%s",
"%s","%s","%s","%s","%s","%s","%s")"""%(Reference1,Name1,Phno1,Fries1,Burger1,Filet1,Chicken1,
                                        Cheese1,Drinks1,Cost1,Service_charge1,Tax1,Subtotal1,Total_cost1))
    mydb.commit()
    mydb.close()


#-------------------------------------------------------------------Buttons----------------------------------------------------------

btnTotal=Button(f1,padx=7,pady=8,bd=7,fg="black",font=('showcard gothic',7,'bold'),
                width=10,text="Total",bg="green",command=Ref).grid(row=7,column=0)

btnReset=Button(f1,padx=7,pady=8,bd=7,fg="black",font=('showcard gothic',7,'bold'),
                width=10,text="Reset",bg="green",command=Reset).grid(row=7,column=1)

btnExit=Button(f1,padx=7,pady=8,bd=7,fg="black",font=('showcard gothic',7,'bold'),
               width=10,text="Exit",bg="green",command=qExit).grid(row=7,column=2)

btnsave=Button(f1,padx=7,pady=8,bd=7,fg="black",font=('showcard gothic',7,'bold'),
                width=10,text="Save",bg="green",command=insert).grid(row=7,column=3)




root.mainloop()

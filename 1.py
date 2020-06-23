from tkinter import *
import math,random,os
from tkinter import messagebox


class billing_system:
    def __init__(self, root):
        global photo
        self.root = root
        self.root.geometry("1500x900")
        self.root.title("Bill App")

        
        bg_color = "#203A43"

        frm1 = Frame(self.root, bd=7, relief=SUNKEN,bg=bg_color)
        frm1.place(x=0,y=0, width=1450, height=90)

        lob=Label(frm1, text="Billing System", font=("times new roman", 39, "bold"),
                         fg="white", bg=bg_color).pack()
        
       

        #variable haru store
        ####personalcare
        self.toothpaste = IntVar()
        self.shampoo = IntVar()
        self.handsoap = IntVar()
        self.hairserum = IntVar()
        self.shavingcream = IntVar()
        self.hairgel = IntVar()
        self.deodrant = IntVar()
        self.facewash = IntVar()

        ##groceriesss
        self.coffee = IntVar()
        self.cereal = IntVar()
        self.oliveoil = IntVar()
        self.pasta = IntVar()
        self.peanutbutter = IntVar()
        self.Rice = IntVar()
        self.P_asta = IntVar()
        self.pan_cake = IntVar()

        # snacks
        self.candy = IntVar()
        self.cokies = IntVar()
        self.crackers = IntVar()
        self.dried_fruit = IntVar()
        self.nuts = IntVar()
        self.oatmeal = IntVar()
        self.popcorn = IntVar()
        self.potatochips = IntVar()

        # freshvegetables
        self.broccoli = IntVar()
        self.corn = IntVar()
        self.cucumbers = IntVar()
        self.mushroom = IntVar()
        self.onion = IntVar()
        self.potatol = IntVar()
        self.tomato = IntVar()
        self.spinach = IntVar()

        ###### beverages
        self.beer = IntVar()
        self.champagne = IntVar()
        self.juice = IntVar()
        self.redwine = IntVar()
        self.rum = IntVar()
        self.sportsdrink = IntVar()
        self.whiskey = IntVar()
        self.vodka = IntVar()

        ####costumerdetails
        self.c_name = StringVar()
        self.c_phoneno = StringVar()
      
        self.c_billno = StringVar()
        x=random.randint(1000,9999)
        self.c_billno.set(str(x))

        # total
        self.t_personalcare = StringVar()
        self.t_vgroceries = StringVar()
        self.t_snacks = StringVar()
        self.t_fvegetables = StringVar()
        self.t_beverages = StringVar()

     # totalwithtax
        self.t_wtpersonalcare = StringVar()
        self.t_wtvgroceries = StringVar()
        self.t_wtsnacks = StringVar()
        self.t_wtfvegetables = StringVar()
        self.t_wtbeverages = StringVar()

        frm = LabelFrame(self.root, bd=7, relief=SUNKEN, text="Costumer Details", font=("times new roman", 20, "bold"),
                         fg="yellow", bg=bg_color)
        frm.place(x=0, y=95, relwidth=1)
        Label(frm, text="Costumer Name : ", bg=bg_color, fg="white", font=("times new roman", 19, "bold")).grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=21,
                                                                                                                pady=5)
        Entry(frm, width=20, textvariable=self.c_name, font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=1,
                                                                                                  pady=10, padx=10)

        Label(frm, text="Phone Number.", bg=bg_color, fg="white", font=("times new roman", 19, "bold")).grid(row=0,
                                                                                                             column=2,
                                                                                                             padx=21,
                                                                                                             pady=5)
        Entry(frm, width=20, textvariable=self.c_phoneno, font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=3,
                                                                                                     pady=10, padx=3)

        Label(frm, text="Bill No : ", bg=bg_color, fg="white", font=("times new roman", 19, "bold")).grid(row=0,
                                                                                                          column=4,
                                                                                                          padx=21,
                                                                                                          pady=5)
        Entry(frm, width=20, textvariable=self.c_billno, font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=5,
                                                                                                    pady=5, padx=5)

        Button(frm, width=9, text="Search",command=self.findbill, font="arial 20 bold", bd=20).grid(row=0, column=9, padx=3)

        frm1 = LabelFrame(self.root, bd=7, relief=SUNKEN, text="Personal care", font=("times new roman", 17, "bold"),
                          fg="yellow", bg=bg_color)
        frm1.place(x=3, y=180, width=320, height=470)

        Label(frm1, text="Tooth Paste", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5,
                                                                                                            sticky="w")
        Entry(frm1, width=6, textvariable=self.toothpaste,font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=1, pady=10, padx=3)

        Label(frm1, text="Shampoo/Conditioner", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=2,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm1, width=6, textvariable=self.shampoo, font="arial 15", bd=5, relief=GROOVE).grid(row=2, column=1,
                                                                                                   pady=10, padx=3)

        Label(frm1, text="Hand Soap", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        Entry(frm1, width=6, textvariable=self.handsoap, font="arial 15", bd=5, relief=GROOVE).grid(row=3, column=1,
                                                                                                    pady=10, padx=3)

        Label(frm1, text="Hair Serum", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=4,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=5,
                                                                                                           sticky="w")
        Entry(frm1, width=6, textvariable=self.hairserum, font="arial 15", bd=5, relief=GROOVE).grid(row=4, column=1,
                                                                                                     pady=10, padx=3)

        Label(frm1, text="Razors/shaving cream", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=5,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm1, width=6, textvariable=self.shavingcream, font="arial 15", bd=5, relief=GROOVE).grid(row=5, column=1,
                                                                                                        pady=10, padx=3)

        Label(frm1, text="Hair gel/Spray", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=6,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=5,
                                                                                                               sticky="w")
        Entry(frm1, width=6, font="arial 15", bd=5, relief=GROOVE).grid(row=6, column=1, pady=10, padx=3)

        Label(frm1, text="Deodorant", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=7,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm1, width=6, textvariable=self.deodrant, font="arial 15", bd=5, relief=GROOVE).grid(row=7, column=1,
                                                                                                    pady=10, padx=3)

        Label(frm1, text="Face Wash/Mouthwash", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=8,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm1, width=6, textvariable=self.facewash, font="arial 15", bd=5, relief=GROOVE).grid(row=8, column=1,
                                                                                                    pady=10, padx=3)

        frm2 = LabelFrame(self.root, bd=7, relief=SUNKEN, text="Various groceries",
                          font=("times new roman", 17, "bold"),
                          fg="yellow", bg=bg_color)
        frm2.place(x=300, y=180, width=310, height=470)

        Label(frm2, text="Coffee/Tea", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=5,
                                                                                                           sticky="w")
        Entry(frm2, width=6, textvariable=self.coffee, font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=1,
                                                                                                  pady=10, padx=3)

        Label(frm2, text="Cereal", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=2,
                                                                                                       column=0,
                                                                                                       padx=10,
                                                                                                       pady=5,
                                                                                                       sticky="w")
        Entry(frm2, width=6, textvariable=self.cereal, font="arial 15", bd=5, relief=GROOVE).grid(row=2, column=1,
                                                                                                  pady=10, padx=3)

        Label(frm2, text="Olive oil", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        Entry(frm2, width=6, textvariable=self.oliveoil, font="arial 15", bd=5, relief=GROOVE).grid(row=3, column=1,
                                                                                                    pady=10, padx=3)

        Label(frm2, text="Pasta", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=4,
                                                                                                      column=0,
                                                                                                      padx=10,
                                                                                                      pady=5,
                                                                                                      sticky="w")
        Entry(frm2, width=6, textvariable=self.pasta, font="arial 15", bd=5, relief=GROOVE).grid(row=4, column=1,
                                                                                                 pady=10, padx=3)

        Label(frm2, text="Peanut butter", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=5,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=5,
                                                                                                              sticky="w")
        Entry(frm2, width=6, textvariable=self.peanutbutter, font="arial 15", bd=5, relief=GROOVE).grid(row=5, column=1,
                                                                                                        pady=10, padx=3)

        Label(frm2, text="rice", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=6,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm2, width=6, textvariable=self.Rice, font="arial 15", bd=5, relief=GROOVE).grid(row=6, column=1,
                                                                                                pady=10, padx=3)

        Label(frm2, text="Pasta", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=7,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm2, width=6, textvariable=self.pasta, font="arial 15", bd=5, relief=GROOVE).grid(row=7, column=1,
                                                                                                 pady=10, padx=3)

        Label(frm2, text="Pancake/Waffle mix", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=8,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm2, width=6, textvariable=self.pan_cake, font="arial 15", bd=5, relief=GROOVE).grid(row=8, column=1,
                                                                                                    pady=10, padx=3)

        frm3 = LabelFrame(self.root, bd=7, relief=SUNKEN, text="Snacks",
                          font=("times new roman", 17, "bold"),
                          fg="yellow", bg=bg_color)
        frm3.place(x=580, y=180, width=310, height=470)

        Label(frm3, text="Candy/Gum", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        Entry(frm3, width=6, textvariable=self.candy, font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=1,
                                                                                                 pady=10, padx=3)

        Label(frm3, text="Cookies", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=3,
                                                                                                        column=0,
                                                                                                        padx=10,
                                                                                                        pady=5,
                                                                                                        sticky="w")
        Entry(frm3, width=6, textvariable=self.cokies, font="arial 15", bd=5, relief=GROOVE).grid(row=3, column=1,
                                                                                                  pady=10, padx=3)

        Label(frm3, text="Crackers", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=4,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5,
                                                                                                         sticky="w")
        Entry(frm3, width=6, textvariable=self.crackers, font="arial 15", bd=5, relief=GROOVE).grid(row=4, column=1,
                                                                                                    pady=10, padx=3)

        Label(frm3, text="Dried fruit", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=5,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=5,
                                                                                                            sticky="w")
        Entry(frm3, width=6, textvariable=self.dried_fruit, font="arial 15", bd=5, relief=GROOVE).grid(row=5, column=1,
                                                                                                       pady=10, padx=3)

        Label(frm3, text="Nuts/Seeds", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=6,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=5,
                                                                                                           sticky="w")
        Entry(frm3, width=6, textvariable=self.nuts, font="arial 15", bd=5, relief=GROOVE).grid(row=6, column=1,
                                                                                                pady=10, padx=3)

        Label(frm3, text="Oatmeal", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=7,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm3, width=6, textvariable=self.oatmeal, font="arial 15", bd=5, relief=GROOVE).grid(row=7, column=1,
                                                                                                   pady=10, padx=3)

        Label(frm3, text="Popcorn", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=8,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm3, width=6, textvariable=self.popcorn, font="arial 15", bd=5, relief=GROOVE).grid(row=8, column=1,
                                                                                                   pady=10, padx=3)

        Label(frm3, text="Potato/Corn chips", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=9,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm3, width=6, textvariable=self.potatochips, font="arial 15", bd=5, relief=GROOVE).grid(row=9, column=1,
                                                                                                       pady=10, padx=3)

        frm4 = LabelFrame(self.root, bd=7, relief=SUNKEN, text="Fresh vegetables",
                          font=("times new roman", 17, "bold"),
                          fg="yellow", bg=bg_color)
        frm4.place(x=877, y=180, width=300, height=470)

        Label(frm4, text="Broccoli", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5,
                                                                                                         sticky="w")
        Entry(frm4, width=6, textvariable=self.broccoli, font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=1,
                                                                                                    pady=10, padx=3)

        Label(frm4, text="Corn", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=4,
                                                                                                     column=0,
                                                                                                     padx=10,
                                                                                                     pady=5,
                                                                                                     sticky="w")
        Entry(frm4, width=6, textvariable=self.corn, font="arial 15", bd=5, relief=GROOVE).grid(row=4, column=1,
                                                                                                pady=10, padx=3)

        Label(frm4, text="Cucumbers", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=5,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        Entry(frm4, width=6, textvariable=self.cucumbers, font="arial 15", bd=5, relief=GROOVE).grid(row=5, column=1,
                                                                                                     pady=10, padx=3)

        Label(frm4, text="Mushrooms", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=6,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        Entry(frm4, width=6, textvariable=self.mushroom, font="arial 15", bd=5, relief=GROOVE).grid(row=6, column=1,
                                                                                                    pady=10, padx=3)

        Label(frm4, text="Onions", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=7,
                                                                                                       column=0,
                                                                                                       padx=10,
                                                                                                       pady=5,
                                                                                                       sticky="w")
        Entry(frm4, width=6, textvariable=self.onion, font="arial 15", bd=5, relief=GROOVE).grid(row=7, column=1,
                                                                                                 pady=10, padx=3)

        Label(frm4, text="Potatoes", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=8,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm4, width=6, textvariable=self.potatol, font="arial 15", bd=5, relief=GROOVE).grid(row=8, column=1,
                                                                                                   pady=10, padx=3)

        Label(frm4, text="Tomatoes", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=9,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm4, width=6, textvariable=self.tomato, font="arial 15", bd=5, relief=GROOVE).grid(row=9, column=1,
                                                                                                  pady=10, padx=3)

        Label(frm4, text="Spinach", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=10,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm4, width=6, textvariable=self.spinach, font="arial 15", bd=5, relief=GROOVE).grid(row=10, column=1,
                                                                                                   pady=10, padx=3)

        frm5 = LabelFrame(self.root, bd=7, relief=SUNKEN, text="Beverages",
                          font=("times new roman", 17, "bold"),
                          fg="yellow", bg=bg_color)
        frm5.place(x=1130, y=180, width=310, height=470)

        Label(frm5, text="Beer", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0,
                                                                                                     column=0,
                                                                                                     padx=10,
                                                                                                     pady=5,
                                                                                                     sticky="w")
        Entry(frm5, width=6, textvariable=self.beer, font="arial 15", bd=5, relief=GROOVE).grid(row=-0, column=1,
                                                                                                pady=10, padx=3)

        Label(frm5, text="Champagne", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=5,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="w")
        Entry(frm5, width=6, textvariable=self.champagne, font="arial 15", bd=5, relief=GROOVE).grid(row=5, column=1,
                                                                                                     pady=10, padx=3)

        Label(frm5, text="Juice", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=6,
                                                                                                      column=0,
                                                                                                      padx=10,
                                                                                                      pady=5,
                                                                                                      sticky="w")
        Entry(frm5, width=6, textvariable=self.juice, font="arial 15", bd=5, relief=GROOVE).grid(row=6, column=1,
                                                                                                 pady=10, padx=3)

        Label(frm5, text="Red wine/White wine", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=7,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm5, width=6, textvariable=self.redwine, font="arial 15", bd=5, relief=GROOVE).grid(row=7, column=1,
                                                                                                   pady=10, padx=3)

        Label(frm5, text="Rum", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=8,
                                                                                                    column=0,
                                                                                                    padx=10,
                                                                                                    pady=5,
                                                                                                    sticky="w")
        Entry(frm5, width=6, textvariable=self.rum, font="arial 15", bd=5, relief=GROOVE).grid(row=8, column=1, pady=10,
                                                                                               padx=3)

        Label(frm5, text="Sports drink", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=9,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm5, width=6, textvariable=self.sportsdrink, font="arial 15", bd=5, relief=GROOVE).grid(row=9, column=1,
                                                                                                       pady=10, padx=3)

        Label(frm5, text="Whiskey", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=10,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm5, width=6, textvariable=self.whiskey, font="arial 15", bd=5, relief=GROOVE).grid(row=10, column=1,
                                                                                                   pady=10, padx=3)

        Label(frm5, text="Vodka", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(
            row=11,
            column=0,
            padx=10,
            pady=5,
            sticky="w")
        Entry(frm5, width=6, textvariable=self.vodka, font="arial 15", bd=5, relief=GROOVE).grid(row=11, column=1,
                                                                                                 pady=10, padx=3)

        frm6 = LabelFrame(self.root, bd=7, relief=SUNKEN, text="Bill Menu",
                          font=("times new roman", 17, "bold"),
                          fg="yellow", bg=bg_color)
        frm6.place(x=0, y=650, relwidth=1, height=170)

        label1 = Label(frm6, text="Total Personal Care price", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=0, column=0, padx=5, pady=0, sticky="w")
        en1 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_personalcare, relief=SUNKEN).grid(row=0,
                                                                                                                column=1,
                                                                                                                padx=1,
                                                                                                                pady=5)

        label2 = Label(frm6, text="Total Various groceries price", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=1, column=0, padx=5, pady=0, sticky="w")
        en2 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_vgroceries, relief=SUNKEN).grid(row=1,
                                                                                                              column=1,
                                                                                                              padx=1,
                                                                                                              pady=5)

        label3 = Label(frm6, text="Total Snacks price ", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=2, column=0, padx=5, pady=0, sticky="w")
        en3 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_snacks, relief=SUNKEN).grid(row=2,
                                                                                                          column=1,
                                                                                                          padx=1,
                                                                                                          pady=5)

        label4 = Label(frm6, text=" Personal Care price  tax", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=0, column=2, padx=10, pady=0, sticky="w")
        en4 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_wtpersonalcare, relief=SUNKEN).grid(row=0,
                                                                                                                  column=3,
                                                                                                                  padx=1,
                                                                                                                  pady=5)

        label5 = Label(frm6, text="Various groceries tax", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=1, column=2, padx=15, pady=0, sticky="w")
        en5 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_wtvgroceries, relief=SUNKEN).grid(row=1,
                                                                                                                column=3,
                                                                                                                padx=1,
                                                                                                                pady=5)

        label6 = Label(frm6, text=" Snacks  tax", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=2, column=2, padx=10, pady=0, sticky="w")
        en6 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_wtsnacks, relief=SUNKEN).grid(row=2,
                                                                                                            column=3,
                                                                                                            padx=1,
                                                                                                            pady=5)

        label7 = Label(frm6, text="Total F.Vegetables ", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=0, column=4, padx=10, pady=0, sticky="w")
        en7 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_fvegetables, relief=SUNKEN).grid(row=0,
                                                                                                               column=5,
                                                                                                               padx=1,
                                                                                                               pady=5)

        label8 = Label(frm6, text="Total Beverages ", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=1, column=4, padx=10, pady=0, sticky="w")
        en8 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_beverages, relief=SUNKEN).grid(row=1,
                                                                                                             column=5,
                                                                                                             padx=1,
                                                                                                             pady=0)

        label8 = Label(frm6, text="Fresh vegetables Tax ", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=2, column=4, padx=10, pady=0, sticky="w")
        en8 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_wtfvegetables, relief=SUNKEN).grid(row=2,
                                                                                                                 column=5,
                                                                                                                 padx=1,
                                                                                                                 pady=0)

        label7 = Label(frm6, text="Beverages  Tax", bg=bg_color, fg="white",
                       font=("times new roman", 17, "bold")).grid(row=0, column=8, padx=19, pady=0, sticky="w")
        en7 = Entry(frm6, font="arial 15 bold", width=10, textvariable=self.t_wtbeverages, relief=SUNKEN).grid(row=0,
                                                                                                               column=9,
                                                                                                               padx=5,
                                                                                                               pady=0)

        frm7 = Frame(frm6, bd=2, relief=SUNKEN, bg=bg_color)

        frm7.place(x=1210, width=310, height=400)

        frm8 = Frame(frm6, bd=1, relief=SUNKEN, bg=bg_color)

        frm8.place(x=955, y=65, width=248, height=50)

        bt1 = Button(frm8, text="TOTAL", command=self.total,highlightbackground='#f7b733', fg="black", font="arial 30 bold", width=6,
                     pady=5).place(x=0,y=1)
        bt_3 = Button(frm8, text="CLEAR", command=self.clear_data,highlightbackground='#f7b733', fg="black", font="arial 30 bold", width=6,
                     pady=5).place(x=140,y=1)                          
        bt2 = Button(frm7, text="EXIT",command=self.exit_gar, highlightbackground='#f7b733', fg="black", font="arial 30 bold", width=7,
                     pady=5).place(x=0,y=63)

        def billwindow():
            window=Tk()
            
            window.geometry("370x500")
            window.minsize(370,500)
            window.maxsize(370, 500)
            window.title("billingdetails")

            
            frm6 = Frame(window, bd=7, relief=GROOVE)

            frm6.place(x=10, y=15, width=350, height=470)
            Label(frm6,text="Billing Details",font="arial 17 bold",bd=7,relief=GROOVE).pack(fill=X)
            scrollbar=Scrollbar(frm6,orient=VERTICAL)
            scrollbar.pack(side=RIGHT,fill=Y)
            textarea = Text(frm6, yscrollcommand=scrollbar.set)
            textarea.pack(fill=BOTH,expand=1)
            scrollbar.config(command=textarea.yview)  
            textarea.insert(END,"\t \t  Walkers Mart")
            textarea.insert(END,"\t \t                      ")
            textarea.insert(END,"\t \t Please Visit Us again")
        
            textarea.insert(END,f"\n\n Bill no: {self.c_billno.get()}")
            textarea.insert(END,f"\n Costumer Name: {self.c_name.get()}")
            textarea.insert(END,f"\n Phone No: {self.c_phoneno .get()}")
            textarea.insert(END,"\n============================================")
            textarea.insert(END,"\n\n Products \t \t  Q.T.Y \t\tPrice")
            textarea.insert(END,"\n============================================")





            if self.c_name.get()=="" or self.c_phoneno.get()=="":
                messagebox.showerror("Error","Costumer Details are necessary\n\n So, Here is an empty bill . Please fill the details . ")
            elif self.t_personalcare.get()=="NRs.  0.0"and self.t_vgroceries.get()=="NRs.  0.0" and self.t_snacks.get()=="NRs.  0.0" and self.t_fvegetables.get()=="NRs.  0.0" and self.t_beverages.get()=="NRs.  0.0":
                messagebox.showerror("Error","No items purchased \n \n Bill shall be empty")

            else:

                


                if self.toothpaste.get()!=0:
                    textarea.insert(END,f"\n Tooth Paste \t \t \t{self.toothpaste.get()} \t {self.tooth_paste}" )

                if self.shampoo.get()!=0:
                    textarea.insert(END,f"\n Shampoo \t \t \t{self.shampoo.get()}  \t {self.sham_poo}" )
                
                if self.handsoap.get()!=0:
                    textarea.insert(END,f"\n Hand Soap \t \t \t{self.handsoap.get()} \t {self.hand_soap}" )

                if self.hairserum.get()!=0:
                    textarea.insert(END,f"\n Hair serum\t \t \t{self.hairserum.get()} \t {self.hair_serum}" )

                if self.hairgel.get()!=0:
                    textarea.insert(END,f"\n Hair Gel \t \t \t{self.hairgel.get()} \t {self.hair_gel}" )
                
                if self.deodrant.get()!=0:
                    textarea.insert(END,f"\n Tooth Paste \t \t \t{self.deodrant.get()} \t{self.deod_rant}" )
                
                if self.facewash.get()!=0:
                    textarea.insert(END,f"\n Face Wash  \t \t \t{self.facewash.get()} \t {self.face_wash}" )

                if self.coffee.get()!=0:
                    textarea.insert(END,f"\n Coffee \t \t \t{self.coffee.get()} \t{self.cof_fee}" )
                
                if self.cereal.get()!=0:
                    textarea.insert(END,f"\n Cereal \t \t \t{self.cereal.get()} \t {self.cere_al}" )
                
                if self.oliveoil.get()!=0:
                    textarea.insert(END,f"\n Olive Oil  \t \t \t{self.oliveoil.get()} \t {self.olive_oil}" )
                
                if self.pasta.get()!=0:
                    textarea.insert(END,f"\n Pasta \t \t \t{self.pasta.get()} \t {self.pa_sta}" )
                
                if self.peanutbutter.get()!=0:
                    textarea.insert(END,f"\n Peanut Butter \t \t \t{self.peanutbutter.get()} \t {self.peanut_butter}" )

                if self.Rice.get()!=0:
                    textarea.insert(END,f"\n Rice \t \t \t{self.Rice.get()} \t {self.Ri_ce}" )

                if self.pan_cake.get()!=0:
                    textarea.insert(END,f"\n Pan Cake \t \t \t{self.pan_cake.get()} \t {self.pan_cak_e}" )
                
                if self.candy.get()!=0:
                    textarea.insert(END,f"\n Candy \t \t \t{self.candy.get()} \t{self.can_dy}" )
                
                if self.cokies.get()!=0:
                    textarea.insert(END,f"\n Cookies  \t \t \t{self.cokies.get()} \t {self.coki_es}" )
                
                if self.crackers.get()!=0:
                    textarea.insert(END,f"\n Crackers \t \t \t{self.crackers.get()} \t {self.crack_ers}" )

                if self.dried_fruit.get()!=0:
                    textarea.insert(END,f"\n Dried Fruit \t \t \t{self.dried_fruit.get()} \t {self.dried_fru_it}" )

                if self.nuts.get()!=0:
                    textarea.insert(END,f"\n Nuts \t \t \t{self.nuts.get()} \t{self.nu_ts}" )

                if self.oatmeal.get()!=0:
                    textarea.insert(END,f"\n Oat Meal \t \t \t{self.oatmeal.get()} \t {self.oat_meal}" )

                if self.popcorn.get()!=0:
                    textarea.insert(END,f"\n Pop Corn  \t \t \t{self.popcorn.get()} \t {self.pop_corn}" )
                
                if self.broccoli.get()!=0:
                    textarea.insert(END,f"\n Brocoli \t \t \t{self.broccoli.get()} \t{self.broc_coli}" )

                if self.corn.get()!=0:
                    textarea.insert(END,f"\n Corn \t \t \t{self.corn.get()} \t {self.co_rn}" )

                if self.cucumbers.get()!=0:
                    textarea.insert(END,f"\n Cucumbers \t \t \t{self.cucumbers.get()} \t {self.cucu_mbers}" )

                

                if self.mushroom.get()!=0:
                    textarea.insert(END,f"\n Mushrooms \t \t \t{self.mushroom.get()} \t{self.mush_room}" )

                if self.onion.get()!=0:
                    textarea.insert(END,f"\n Onions \t \t \t{self.onion.get()} \t {self.oni_on}" )

                if self.potatol.get()!=0:
                    textarea.insert(END,f"\n Potato \t \t \t{self.potatol.get()} \t {self.pot_atol}" )
                
                if self.tomato.get()!=0:
                    textarea.insert(END,f"\n Tomato  \t \t \t{self.tomato.get()} \t{self.tom_ato}" )
                
                if self.spinach.get()!=0:
                    textarea.insert(END,f"\n Spinach \t \t \t{self.spinach.get()} \t{self.spin_ach}" )


                if self.beer.get()!=0:
                    textarea.insert(END,f"\n Beer \t \t \t{self.beer.get()} \t{self.be_er}" )

                if self.champagne.get()!=0:
                    textarea.insert(END,f"\n Champagne \t \t \t{self.champagne.get()} \t {self.champ_agne}" )

                if self.juice.get()!=0:
                    textarea.insert(END,f"\n Juice  \t \t \t{self.juice.get()} \t{self.ju_ice}" )


                if self.redwine.get()!=0:
                    textarea.insert(END,f"\n Red Wine \t \t \t{self.redwine.get()} \t {self.red_wine}" )

                if self.rum.get()!=0:
                    textarea.insert(END,f"\n Rum \t \t \t{self.rum.get()} \t {self.ru_m}" )

                if self.sportsdrink.get()!=0:
                    textarea.insert(END,f"\n Sports Drink \t \t \t{self.sportsdrink.get()} \t {self.sports_drink}" )

                if self.whiskey.get()!=0:
                    textarea.insert(END,f"\n Whiskey \t \t \t{self.whiskey.get()} \t{self.whis_key}" )

                if self.vodka.get()!=0:
                    textarea.insert(END,f"\n Vodka \t \t \t{self.vodka.get()} \t {self.vod_ka}" )

                textarea.insert(END,"\n--------------------------------------------")
                if self.t_wtpersonalcare.get()!="NRs.  0.0":
                    textarea.insert(END,f"\n\n Personal Care Tax \t \t\t\t {self.t_wtpersonalcare.get()}")
                
                
                
                if self.t_wtvgroceries.get()!="NRs.  0.0":
                    textarea.insert(END,f"\n\n Various Groceries Tax \t \t\t\t {self.t_vgroceries.get()}")
                
                if self.t_wtsnacks.get()!="NRs.  0.0":
                    textarea.insert(END,f"\n\n Snacks Tax \t \t\t\t {self.t_wtsnacks.get()}")
                
                if self.t_wtfvegetables.get()!="NRs.  0.0":
                    textarea.insert(END,f"\n\n Fresh Vegetables Tax \t \t\t\t {self.t_wtfvegetables.get()}")
                
                if self.t_wtbeverages.get()!="NRs.  0.0":
                    textarea.insert(END,f"\n\n Beverages Tax \t \t\t\t {self.t_wtbeverages.get()}")
                
                textarea.insert(END,"\n-----------------------------------------------")

                textarea.insert(END,f"\n\n Total Bill  \t \t\t NRs.  {self.total_bill}")

                
                
                textarea.insert(END,"\n------------------------------------------")


                op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
                if op>0:
                    bill_data=textarea.get("1.0",END)
                    f1=open("costumerdetails/"+str(self.c_billno.get())+".txt ","w")
                    f1.write(bill_data)
                    f1.close
                    messagebox.showinfo("Saved", f"Bill No  : {self.c_billno.get()} Saved Sucessfully")
                else:
                    return
                
        bt3 = Button(frm7, text="GENERATE BILL", command=billwindow,highlightbackground='#f7b733', fg="black", font="arial 26 bold",
                     width=14,
                     pady=5, padx=0).place(x=0,y=0)
    
    def total(self):
        self.tooth_paste=self.toothpaste.get()*85
        self.sham_poo=self.shampoo.get()*455
        self.hand_soap=self.handsoap.get()*45
        self.hair_serum=self.hairserum.get()*505
        self.shaving_cream=self.hairserum.get()*385
        self.hair_gel=self.hairgel.get()*385
        self.deod_rant=self.deodrant.get()*485
        self.face_wash=self.facewash.get()*305
                                                


        


        self.total_personaluse=float(
                                                self.tooth_paste+
                                                self.sham_poo+
                                                self.hand_soap+
                                                self.hair_serum+
                                                self.shaving_cream+
                                                self.hair_gel+
                                                self.deod_rant+
                                                self.face_wash
                                                )


        self.t_personalcare.set("NRs.  "+str(self.total_personaluse))  
        self.t_pc= round((self.total_personaluse*0.05),2)
        self.t_wtpersonalcare.set("NRs.  "+str(self.t_pc))


        self.cof_fee=self.coffee.get()*765
        self.cere_al=self.cereal.get()*500
        self.olive_oil=self.oliveoil.get()*515
        self.pas_ta=self.pasta.get()*115
        self.peanut_butter=self.peanutbutter.get()*285
        self.Ri_ce=self.Rice.get()*1555
        self.pa_sta=self.pasta.get()*385
        self.pan_cak_e=self.pan_cake.get()*105

        self.total_variousgrocery=float(
                                                self.cof_fee+
                                                self.cere_al+
                                                self.olive_oil+
                                                self.pas_ta+
                                                self.peanut_butter+
                                                self.Ri_ce+
                                                self.pa_sta+
                                                self.pan_cak_e
                                                )     

        self.t_vgroceries.set("NRs.  "+str(self.total_variousgrocery)) 
        self.t_vg=round((self.total_variousgrocery*0.04),2)
        self.t_wtvgroceries.set("NRs.  "+str(self.t_vg))

        self.can_dy=self.candy.get()*85
        self.coki_es=self.cokies.get()*115
        self.crack_ers=self.crackers.get()*55
        self.dried_fru_it=self.dried_fruit.get()*305
        self.nu_ts=self.nuts.get()*305
        self.oat_meal=self.oatmeal.get()*385
        self.pop_corn=self.popcorn.get()*225
        self.potato_chips=self.potatochips.get()*85
        
        self.total_snacks=float(
                                                self.can_dy+
                                                self.coki_es+
                                                self.crack_ers+
                                                self.dried_fru_it+
                                                self.nu_ts+
                                                self.oat_meal+
                                                self.pop_corn+
                                                self.potato_chips
                                                )     

        self.t_snacks.set("NRs.  "+str(self.total_snacks)) 
        self.t_sn=round((self.total_snacks*0.06),2)
        self.t_wtsnacks.set("NRs.  "+str(self.t_sn))      


        self.broc_coli=self.broccoli.get()*85
        self.co_rn=self.corn.get()*105
        self.cucu_mbers=self.cucumbers.get()*75
        self.mush_room=self.mushroom.get()*605
        self.oni_on=self.onion.get()*45
        self.pot_atol=self.potatol.get()*45
        self.tom_ato=self.tomato.get()*55
        self.spin_ach=self.spinach.get()*105








        self.total_freshvegetables=float(
                                                self.broc_coli+
                                                self.co_rn+
                                                self.cucu_mbers+
                                                self.mush_room+
                                                self.oni_on+
                                                self.pot_atol+
                                                self.tom_ato+
                                                self.spin_ach
                                                )     

        self.t_fvegetables.set("NRs.  "+str(self.total_freshvegetables))  
        self.t_fv=round((self.total_freshvegetables*0),2)
        self.t_wtfvegetables.set("NRs.  "+str(self.t_fv))

        self.be_er=self.beer.get()*280
        self.champ_agne=self.champagne.get()*4300
        self.ju_ice=self.juice.get()*115
        self.red_wine=self.redwine.get()*2000
        self.ru_m=self.rum.get()*1600
        self.sports_drink=self.sportsdrink.get()*115
        self.whis_key=self.whiskey.get()*1400
        self.vod_ka=self.vodka.get()*1620





        
        
        
        
        self.total_beverages=float(
                                                self.be_er+
                                                self.champ_agne+
                                                self.ju_ice+
                                                self.red_wine+
                                                self.ru_m+
                                                self.sports_drink+
                                                self.whis_key+
                                                self.vod_ka
                                                )     

        self.t_beverages.set("NRs.  "+str(self.total_beverages)) 
        self.t_br=round((self.total_beverages*0.1),2)
        self.t_wtbeverages.set("NRs.  "+str(self.t_br))

        self.total_bill=round(float(self.total_personaluse+
                                        self.total_variousgrocery+
                                        self.total_snacks+
                                        self.total_freshvegetables+
                                        self.total_personaluse+
                                        self.t_pc+
                                        self.t_sn+
                                        self.t_vg+
                                        self.t_fv+
                                        self.t_br
                                         ),2) 
    
    def findbill(self):
        self.root1=Tk()
        self.root1.geometry("370x500")
        self.root1.minsize(370,500)
        self.root1.title("billingdetails")
        
        frm7 = Frame(self.root1, bd=7, relief=GROOVE)

        frm7.place(x=10, y=15, width=350, height=470)
        Label(frm7,text="Billing Details",font="arial 17 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrollbar=Scrollbar(frm7,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        textarea = Text(frm7, yscrollcommand=scrollbar.set)
        textarea.pack(fill=BOTH,expand=1)
        scrollbar.config(command=textarea.yview)

       
        present="no"
        for i in os.listdir("costumerdetails/"):
            if i .split(".") [0]==self.c_billno.get():
                f1=open(f"costumerdetails/{i}","r")
                
                for d in f1:
                    textarea.insert(END,d)
                f1.close()
                present="yes"
        if  present=="no":
            messagebox.showerror("Error","Invalid bill no \n \n So, Here you have an empty bill")
    
    def clear_data(self):
        msg=messagebox.askyesno("Clear Data","Do you really want to clear  your data ?")
        if msg>0:
            self.toothpaste.set(0)
            self.shampoo.set(0) 
            self.handsoap.set(0)
            self.hairserum.set(0)
            self.shavingcream.set(0) 
            self.hairgel.set(0) 
            self.deodrant.set(0) 
            self.facewash.set(0)

            ##groceriesss
            self.coffee.set(0) 
            self.cereal.set(0)
            self.oliveoil.set(0)
            self.pasta.set(0) 
            self.peanutbutter.set(0) 
            self.Rice.set(0)
            self.P_asta.set(0) 
            self.pan_cake.set(0) 

            # snacks
            self.candy.set(0)
            self.cokies.set(0)
            self.crackers.set(0)
            self.dried_fruit.set(0) 
            self.nuts.set(0) 
            self.oatmeal.set(0)
            self.popcorn.set(0) 
            self.potatochips.set(0) 

            # freshvegetables
            self.broccoli.set(0)
            self.corn.set(0)
            self.cucumbers.set(0) 
            self.mushroom.set(0)
            self.onion.set(0)
            self.potatol.set(0)
            self.tomato.set(0) 
            self.spinach.set(0)

            ###### beverages
            self.beer.set(0) 
            self.champagne.set(0)
            self.juice.set(0)
            self.redwine .set(0)
            self.rum.set(0) 
            self.sportsdrink.set(0) 
            self.whiskey.set(0) 
            self.vodka.set(0) 

            ####costumerdetails
            self.c_name.set("") 
            self.c_phoneno.set("") 
            self.c_billno.set("  ")
            x=random.randint(1000,9999)
            self.c_billno.set(str(x))

            # total
            self.t_personalcare.set("")
            self.t_vgroceries.set("")
            self.t_snacks.set("")
            self.t_fvegetables.set("") 
            self.t_beverages.set("") 

        # totalwithtax
            self.t_wtpersonalcare.set("") 
            self.t_wtvgroceries.set("") 
            self.t_wtsnacks.set("")
            self.t_wtfvegetables.set("") 
            self.t_wtbeverages.set("")
    
    def exit_gar(self):
        msg=messagebox.askyesno("Exit","Do you really want to exit?")
        if msg>0:
            self.root.destroy() 
                                                
root=Tk()


ob1=billing_system(root)


root.mainloop()





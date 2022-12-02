
from tkinter import *
import sqlite3

#create tkinter window
root = Tk()
root.title('Car Rental DB')
root.geometry("400x400")

#connect to the DB
#conn is an object that holds the connection for the DB
conn = sqlite3.connect('carrental.db')
print("Connected to DB Successfully")


#create a cursor
carrental_cursor = conn.cursor()

def insert_customer():
    inC = sqlite3.connect('carrental.db')
	inC_cur = inC.cursor()

	inC_cur.execute("INSERT INTO CUSTOMER VALUES(:Name, :Phone)", 
		{
			'Name': customer_name.get(),
			'Phone': customer_phone.get()
		})

	inC_cur.commit()
	inC_cur.close()

def insert_vehicle():
    inV = sqlite3.connect('carrental.db')
	inV_cur = inC.cursor()

	inV_cur.execute("INSERT INTO VEHICLE VALUES(:VehicleID, :Description, :Year, :Type, :Category)", 
		{
			'VehicleID': vehicle_vehicleID.get(),
			'Description': vehicle_description.get(),
            'Year': vehicle_year.get(),
			'Type': vehicle_type.get(),
            'Category': vehicle_category.get()
		})

	inV_cur.commit()
	inV_cur.close()

def insert_rental():
    #TODO: process for inserting some stuff into the DB

def input_query():
    #TODO: process for using a select query






#TODO: define all GUI components (using a grid)

#define all textboxes
#Customer text boxes
customer_name = Entry(root, width = 30)
customer_name.grid(row=0, column=1, padx=20)
#note that padx is only needed once
customer_phone = Entry(root, width = 30)
customer_phone.grid(row=1, column=1)

#row 3 is skipped for beauty reasons
#Vehicle text boxes
vehicle_vehicleID = Entry(root, width = 30)
vehicle_vehicleID.grid(row=4, column=1)

vehicle_description = Entry(root, width = 30)
vehicle_description.grid(row=5, column=1)

vehicle_year = Entry(root, width = 30)
vehicle_year.grid(row=6, column=1)

vehicle_type = Entry(root, width = 30)
vehicle_type.grid(row=7, column=1)

vehicle_category = Entry(root, width = 30)
vehicle_category.grid(row=8, column=1)


#TODO: labels
#customer labels
customer_name_label = Label(root, text= 'Customer Name: ')
customer_name_label.grid(row=0, column=0)

customer_phone_label = Label(root, text= 'Customer Phone: ')
customer_phone_label.grid(row=1, column=0)

#vehicle labels
vehicle_vehicleID_label = Label(root, text= 'Vehicle ID: ')
vehicle_vehicleID_label.grid(row=4, column=0)

vehicle_description_label = Label(root, text= 'Vehichle Description: ')
vehicle_description_label.grid(row=5, column=0)

vehicle_year_label = Label(root, text= 'Vehicle Year: ')
vehicle_year_label.grid(row=6, column=0)

vehicle_type_label = Label(root, text= 'Vehichle Type: ')
vehicle_type_label.grid(row=7, column=0)

vehicle_category_label = Label(root, text= 'Vehichle Category: ')
vehicle_category_label.grid(row=8, column=0)






#TODO: submit button and their locations
insert_customer_btn = Button(root, text = 'Add Customer', command = insert_customer)
insert_customer_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

insert_vehicle_btn = Button(root, text = 'Add Vehicle', command = insert_customer)
insert_vehicle_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()

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
			'CustID': customer_id.get(),
			'Name': customer_name.get(),
			'Phone': customer_phone.get()
		})

	inC.commit()
	inC.close()

def insert_vehicle():
	inV = sqlite3.connect('carrental.db')
	inV_cur = inV.cursor()

	inV_cur.execute("INSERT INTO VEHICLE VALUES(:VehicleID, :Description, :Year, :Type, :Category)", 
		{
			'VehicleID': vehicle_vehicleID.get(),
			'Description': vehicle_description.get(),
            'Year': vehicle_year.get(),
			'Type': vehicle_type.get(),
            'Category': vehicle_category.get()
		})

	inV.commit()
	inV.close()

def insert_rental():
	inV = sqlite3.connect('carrental.db')
	inV_cur = inC.cursor()
    #TODO: process for inserting some stuff into the DB
	inV.commit()
	inV.close()

def input_query():
	inV = sqlite3.connect('carrental.db')
	inV_cur = inC.cursor()
    #TODO: process for inserting some stuff into the DB
	inV.commit()
	inV.close()

def list_view_customer_rental():
	liV = sqlite3.connect('carrental.db')
	liV_cur = liV.cursor()

	#PLEASE NOTE THAT PYTHON AND SQL DOES NOTHING WITH dropping the views on exit, so we have to manually do this ourselves
	liV_cur.execute("DROP VIEW vRentalInfo")

	#TODO: FInd total amount, fix task 1 part 2
	liV_cur.execute("CREATE VIEW vRentalInfo AS SELECT Re.OrderDate, Re.StartDate, Re.ReturnDate, Re.Qty * 7 as TotalDays, Ve.VehicleID as VIN, Ve.Description as Vehicle, Ve.Type, Ve.Category, Cu.CustID as CustomerID, Cu.Name as CustomerName, Re.TotalAmount as OrderAmount, Re.PaymentDate FROM RENTAL AS Re, CUSTOMER AS Cu, VEHICLE AS Ve, RATE AS Ra WHERE Re.CustID=Cu.CustID AND Re.VehicleID=Ve.VehicleID ORDER BY Re.StartDate")
	
	#liV_cur.execute("SELECT * FROM vRentalInfo")
	liV_cur.execute("SELECT SUM(OrderAmount) FROM vRentalInfo WHERE (CustomerID=? OR CustomerName=?) AND PaymentDate='NULL'", (customer_id.get(), customer_name.get(),))
	
	output_records = liV_cur.fetchall()
	print_record = ''
	for output_record in output_records:
		print_record += str(str(output_record[0])+"\n")
	#TODO: fix the formatting
	liV_label = Label(root, text = print_record)
	liV_label.grid(row=12, column=0, columnspan=2)

	liV.commit()
	liV.close()

def list_view_vehicle():
	liVV = sqlite3.connect('carrental.db')
	liVV_cur = liVV.cursor()

	#PLEASE NOTE THAT PYTHON AND SQL DOES NOTHING WITH dropping the views on exit, so we have to manually do this ourselves
	liVV_cur.execute("DROP VIEW vRentalInfo")

	liVV_cur.execute("CREATE VIEW vRentalInfo AS SELECT Re.OrderDate, Re.StartDate, Re.ReturnDate, Re.Qty * 7 as TotalDays, Ve.VehicleID as VIN, Ve.Description as Vehicle, Ve.Type, Ve.Category, Cu.CustID as CustomerID, Cu.Name as CustomerName, Re.TotalAmount as OrderAmount, Re.PaymentDate FROM RENTAL AS Re, CUSTOMER AS Cu, VEHICLE AS Ve WHERE Re.CustID=Cu.CustID AND Re.VehicleID=Ve.VehicleID ORDER BY Re.StartDate")
	
	liVV_cur.execute("SELECT VIN, Vehicle FROM vRentalInfo WHERE (Vehicle=? OR VIN=?)",(vehicle_description.get(),vehicle_vehicleID.get(),))

	output_records = liVV_cur.fetchall()
	print_record = ''
	for output_record in output_records:
		print_record += str(str(output_record[0])+" "+str(output_record[1])+"\n")
	#TODO: fix the formatting
	liVV_label = Label(root, text = print_record)
	liVV_label.grid(row=13, column=0, columnspan=2)

	liVV.commit()
	liVV.close()



#TODO: define all GUI components (using a grid)

#define all textboxes
#Customer text boxes
customer_name = Entry(root, width = 30)
customer_name.grid(row=0, column=1, padx=20)
#note that padx is only needed once
customer_phone = Entry(root, width = 30)
customer_phone.grid(row=1, column=1)

customer_id = Entry(root, width = 30)
customer_id.grid(row=2, column=1)

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

customer_id_label = Label(root, text= 'Customer ID: ')
customer_id_label.grid(row=2, column=0)

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
insert_customer_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

insert_vehicle_btn = Button(root, text = 'Add Vehicle', command = insert_vehicle)
insert_vehicle_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

list_view_btn = Button(root, text = 'List Customer Balance', command = list_view_customer_rental)
list_view_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

list_view_vehicle_btn = Button(root, text = 'List Vehicle', command = list_view_vehicle)
list_view_vehicle_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()

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

def submit():
    #TODO: process for inserting some stuff into the DB

def input_query():
    #TODO: process for using a select query

#TODO: define all GUI components (using a grid)

#TODO: labels

#TODO: submit button and their locations
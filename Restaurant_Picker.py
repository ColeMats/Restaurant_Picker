import os.path
import random
import tkinter
from tkinter import *

#resources:
#https://stackoverflow.com/questions/3704568/tkinter-button-command-activates-upon-running-program
#https://www.geeksforgeeks.org/python-gui-tkinter/

restaurants = ["Marukame Udon", "Raising Cane's", "Subway", "Burger King", "Gyukaku", "Panda Express", "California Pizza Kitchen", "Zippy's"]

def add_restaurant(restaurant, file_name):
    try: 
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i in lines:
                if (i.strip('\n') == restaurant):
                    print('Restaurant is already stored')
                    t = True
                    break
                else:
                    t = False
            if (t == False):
                f = open(file_name, 'a')
                f.write(restaurant + '\n')
                f.close()
    except:
        f = open(file_name, 'a')
        f.write(restaurant + '\n')
        f.close()


def delete_restaurant(restaurant, file_name):
    if (os.path.exists(file_name)):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            with open(file_name, 'w') as file:
                for line in lines:
                    if (line.strip("\n") != restaurant):
                        file.write(line)
    else:
        print("File does not exist")

def view_all_restaurants(file_name):
    if(os.path.exists(file_name)):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip('\n'))
    else:
        print("File does not exist")

def Pick_Rand_Rest(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        rand_rest = random.choice(lines)
    file.close()
    print(rand_rest)
    restaurant = str(rand_rest)
    return restaurant


def home():
    #user can choose to generate a random restaurant from the stored restaurants

    user_input = input('Welcome to Restaurant Picker! \n Please type the number for the following: \n 1 - Generate a random restaurant \n 2 - Add a restaurant \n 3 - Delete a restaurant \n 4 - View all Restaurants \n')
    if (user_input == '1'):
        Pick_Rand_Rest('restaurant.txt')

    #user can add a restaurant
    elif (user_input == '2'):
        user_rest = input("Which restaurant(s) would you like to add (seperated by commas)? \n")
        rests = user_rest.split(', ')
        for i in rests:
            add_restaurant(i, 'restaurant.txt')

    #user can delete a restaurant
    elif (user_input == '3'):
        user_rest = input("Which restaurant(s) would you like to delete (seperated by commas)? \n")
        rests = user_rest.split(', ')
        for i in rests:
            delete_restaurant(i, 'restaurant.txt')

    #user can view all stored restaurants
    elif (user_input == '4'):
        view_all_restaurants('restaurant.txt')
    
    else:
        print("Error, Please enter a number corresponding to an option. \n")
        home()

def raise_frame(frame):
    frame.tkraise()

def generate_random_button(master,  win):
    button = tkinter.Button(master, text = 'Generate Random Resaurant', width = 30, highlightbackground = '#38DB73', command = lambda : random_button_press(master, win))
    button.place(x = 500, y = 100, anchor = CENTER)

def random_button_press(master, win):
    win.config(text = Pick_Rand_Rest('restaurant.txt'))
    win.place(x = 500, y = 50, anchor = CENTER)

def generate_adddelete_button(master, frame):
    button = tkinter.Button(master, text = 'Add or Delete Restaurant', width = 30, command = lambda : raise_frame(frame))
    button.place(x = 500, y = 150, anchor = CENTER)

def generate_exit_button(frame):
    button = tkinter.Button(frame, text = 'Exit', width = 20, command = frame.destroy, highlightbackground = '#CC2400')
    button.place(x = 500, y = 500, anchor = CENTER)

def generate_home_frame(home_frame, add_delete_frame):
    home_frame = Frame(width = 1000, height = 600)
    home_frame.pack()
    label = Label(home_frame)
    generate_random_button(home_frame, label)
    generate_adddelete_button(home_frame, add_delete_frame)
    generate_exit_button(home_frame)


def generate_add_delete_frame(add_delete_frame):
    add_delete_frame = Frame(width = 1000, height = 600)
    add_delete_frame.pack()
    generate_exit_button(add_delete_frame)
    raise_frame(add_delete_frame)

    #for i in view_all_restaurants('restaurant.txt'):
        #Checkbutton(master, text = i)


def home_window():
    master = Tk()
    home_frame = Frame(master)
    add_delete_frame = Frame(master)
    generate_home_frame(home_frame, add_delete_frame)
    #generate_add_delete_frame(master)
    master.title('Restaurant Picker')

    #generate_adddelete_button(master, add_delete_frame)
    #generate_exit_button(master)
    master.mainloop()


home_window()
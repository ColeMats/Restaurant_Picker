import os.path
import random

restaurants = ["Marukame Udon", "Raising Cane's", "Subway", "Burger King", "Gyukaku", "Panda Express", "California Pizza Kitchen", "Zippy's"]

def add_restaurant(restaurant, file_name):
    try: 
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i in lines:
                if (i.strip('\n') != restaurant):
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

def Pick_Rand_Rest(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        rand_rest = random.choice(lines)
    file.close()
    print(rand_rest)


def home():
    #user can choose to generate a random restaurant from the stored restaurants
    #Pick_Rand_Rest('restaurant.txt')

    #user can add a restaurant
    add_restaurant('Subway', 'restaurant.txt')
    #add_restaurant('Panda Express', 'restaurant.txt')
    #add_restaurant('Zippys', 'restaurant.txt')

    #user can delete a restaurant
    #delete_restaurant('Burger King', 'restaurant.txt')
    #user can view all stored restaurants


home()
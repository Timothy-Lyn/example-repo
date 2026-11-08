from tabulate import tabulate # Importing tabulate for use in view_all() function
#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity): # country, code, product, cost and quantity variables initialised.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass


    def get_cost(self): 
        
        return int(self.cost) # Function will return the cost of a shoe when called


    def get_quantity(self):
        return int(self.quantity) # Function will return the quantity of a shoe when called


    def __str__(self):

        return f"[{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}]" # str method used to define layout of Shoe class


#=============Shoe list===========


shoe_list = [] # Empty Shoe_list created


#==========Functions outside the class==============


def read_shoes_data(file):
    shoe_list.clear() # shoe_list.clear() used to clear shoe_list every time while loop runs again.
    try:
        with open(f'{file}', 'r') as f:
            next(f)
            for line in f:
                temp = line.strip()
                temp = temp.split(',')

                shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4])) # appends country, code, product, cost and quantity values for each line in txt file to shoe_list

            return shoe_list
    except FileNotFoundError as e: # except FileNotFoundError used to eliminate error
            print("The file you have selected doesn't exist")


def capture_shoes():
    try:
        country = input('Enter the country of origin: ')
        code = input('Enter the shoe code: ')
        product = input('Enter the product: ')
        cost = int(input('Enter the shoe cost: ')) # int() used to convert input for cost and quantity to int values
        quantity = int(input('Enter the quantity of shoes: ')) 

        confirm = input('Are you sure you want to make these changes: ') # Confirmation step added in case wrong option was selected in while loop

        if confirm.lower() == 'yes': # tests confirm result, .lower() used to test for 'Yes, YES and yes'
            shoe_list.append(Shoe(country, code, product, cost, quantity)) # Only if confirm = yes will this function append to shoe_list

            with open('inventory.txt', 'a') as f:
                f.write(f'\n{country},{code},{product},{cost},{quantity}') # writes newly captured shoe to original inventory list

    except ValueError as e:
        print('Please enter a valid character type.')   # except ValueError and except FileNotFoundError used to eliminate possible errors

    except FileNotFoundError as e:
        print('Please enter a valid filename.')

def view_all():
    table = []
    for i in shoe_list:
        table.append([i.country, i.code, i.product, i.cost, i.quantity]) # tabulate takes 'list of lists' as input data
    head = ('Country','Code','Product', 'Cost','Quantity') # head = ... gets table headings
    print(tabulate(table,head,tablefmt = 'pretty')) # tablefmt changes tbale layout


def re_stock():
    try:

        small = min(shoe_list, key = lambda x: x.get_quantity()) # returns shoe with minimum quantity value
        print(f'The shoe with the least amount of stock is {small.code} with {small.get_quantity()} shoes. It should be restocked.')

    except TypeError as e: # except TypeError used to eliminate a wrong character type in min() function
        print('Check character types')

    def s_index(): # s_index used to determine at which line in inventory.txt the minimum quantity value is found
        for i in range(len(shoe_list)): 
            if shoe_list[i].code == small.code:
                return i

    restock = input('Do you want the shoes to be restocked? ') # Confirmation if the shoe is to be restocked
    
    if restock.lower() == 'yes':

        updated_stock = input('Please enter the amount you want to update the stock to: ') # Input to get value to which the quantity value of minimum quantity shoe is changed

        confirm = input('Are you sure you want to make these changes: ') # Confirmation that th changes are to be made.

        try:
            if confirm.lower() == 'yes':
                with open('inventory.txt','r') as f:
                    lines = f.readlines()
                lines[s_index() + 1] = f'{small.country},{small.code},{small.product},{small.cost},{updated_stock}\n' # lines[s_index() + 1] = ... replaces the line in the original file with a new line that keeps the country, code, product and cost but changes the quantity

                with open('inventory.txt', 'w') as f:
                    f.writelines(lines)
        except FileNotFoundError as e: #FIleNotFoundError used to eliminate error if incorrect filename is given in line 108
            print("Please enter a valid file name")
    pass


def search_shoe(x): # Simple linear searching algorithm used.
    for i in shoe_list:
        if i.code == x:
            print(f"\nThe shoe with code {x} is {i.product} \n") 
    pass


def value_per_item():
    try:
        for i in shoe_list: 
            print(f'The value of {i.code} is {i.get_cost() * i.get_quantity()}')
    except ValueError as e: # except ValueError used to eliminate error of non-int values used in cost/quantity
        print('Incorrect character type.')
    pass


def highest_qty():
    try:
        largest_q = max(shoe_list, key= lambda k: k.get_quantity())
        print(f'The shoe with the highest quantity is {largest_q.code} with {largest_q.quantity} shoes','\n',
            'It is currently on sale')
    except TypeError as e: # except TypeError used to eliminate error in case of incorrect type used in max() function.
        print('Check character types')


#==========Main Menu=============

while True:
    read_shoes_data('inventory.txt')
    options = int(
        input(
            '''            Please select what you want to do: 
            1) Capture a new shoe.
            2) View all available shoes.
            3) Restock shoes.
            4) Search for a shoe.
            5) View value of shoes
            6) View which shoe is on sale.
            7) Close application
            \n
            '''
         )
    )

    if options == 1:
        capture_shoes()
        pass

    elif options == 2:
        view_all()
        print('\n')

    elif options == 3:
        re_stock()

    elif options == 4:
        s_code = input("Please enter the code of the shoe you're looking for: ") # s_code gets shoe code of shoe that wants to be found, from user.
        search_shoe(s_code)

    elif options == 5:
        value_per_item()

    elif options == 6:
        highest_qty()

    elif options == 7:
        print('Thank you for your time')
        break
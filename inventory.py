
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass


    def get_cost(self):
        
        return int(self.cost)
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return int(self.quantity)
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):

        return f"({self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity})" 
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    with open('inventory.txt', 'r') as f:
        next(f)
        for line in f:
            temp = line.strip()
            temp = temp.split(',')

            shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

        return shoe_list
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    country = input('Enter the country of origin: ')
    code = input('Enter the shoe code: ')
    product = input('Enter the product: ')
    cost = int(input('Enter the shoe cost: '))
    quantity = int(input('Enter the quantity of shoes: '))
    shoe_list.extend(Shoe(country, code, product, cost, quantity))
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    for i in shoe_list:
        print(i)
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe(shoe_list, x):
    for i in shoe_list:
        if i.code == x:
            return f"The shoe with code {x} is {i.product}"
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    for i in shoe_list[1:]:
        print(f'The value of {i.code} is {i.get_cost() * i.get_quantity()}')
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    largest_q = max(shoe_list, key= lambda k: k.get_quantity)
    print(f'The shoe with the highest quantity is {largest_q.code} with {largest_q.quantity} shoes')
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()
highest_qty()
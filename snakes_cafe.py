print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('** To quit at any time, type "quit" **')
print('**************************************')

print(
    '''
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    '''
    )
print('**************************************')
print('What would you like to order?')
print('**************************************')
order=input('>')
x = 0
while order != 'quit':
    x = x + 1 
    print(f'** {x} order of {order} have been added to your meal **')
    order=input('>')    
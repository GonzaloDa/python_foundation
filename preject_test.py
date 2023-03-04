
dict_1 = {'boulder outdoor': {'x_3447777': 'y_5799956'}, 'boulderhalls': 'Ostblock', 'ux_meetsup': 'Factory', 'party': 'Suicide_circus'}



def event_finder():
    user_input = input('What would you like to do in Berlin? ')
    if user_input == 'boulder outdoor':
        print('x_3447777' ' y_5799956')
    elif user_input == 'boulderhalls':
        print('Ostblock')
    elif user_input == 'ux_meetsup':
        print("Factory")
    elif user_input == 'party':
        print("Suicide circus")
    else:
        print("Not found")
        
event_finder()

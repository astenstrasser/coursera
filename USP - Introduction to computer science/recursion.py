## Recursive Methods

def sum_elements(list_of_elements, position = 0, sum_result = 0):
    sum_result += list_of_elements[position]
    if position == (len(list_of_elements)-1):
        return sum_result
    else:
        return sum_elements(list_of_elements, position+1, sum_result)
    
def find_odds(list_of_elements, position = 0, odds = None):
    if odds == None:
        odds = []
    if position == (len(list_of_elements)):
        print(odds)
        return odds
    elif list_of_elements[position] % 2 == 0:
        return find_odds(list_of_elements, position+1, odds)
    else:
        odds.append(list_of_elements[position])
        return find_odds(list_of_elements, position+1, odds)
    
def incomodam(times, time_check=0, my_string=''):
    if times < 0:
        return ''
    elif time_check == times:
        return my_string
    else:
        my_string += 'incomodam '
        return incomodam(times, time_check+1, my_string)

def elefantes(times, time_check=0, my_string=''):
    if times < 0:
        return ''
    elif time_check == times:
        return my_string
    elif time_check == 0:
        my_string += str(time_check+1) + ' elefante incomoda muita gente'
        return elefantes(times, time_check+1, my_string)   
    else:
        add_words = incomodam(time_check+1)
        my_string += '\n' + str(time_check+1) + ' elefantes '+ add_words +'muito mais'
        if time_check+1 != times:
            my_string += '\n'+str(time_check+1) + ' elefantes incomodam muita gente'    
        return elefantes(times, time_check+1, my_string)
    

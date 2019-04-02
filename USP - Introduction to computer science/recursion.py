## Recursive Methods

def sum_elements(list_of_elements, position = 0, sum_result = 0):
    sum_result += list_of_elements[position]
    if position == (len(list_of_elements)-1):
        return sum_result
    else:
        return sum_elements(list_of_elements, position+1, sum_result)
    
def encontra_impares(list_of_elements, position = 0, odds = []):
    if position == (len(list_of_elements)):
        return odds
    elif list_of_elements[position] % 2 == 0:
        print(odds)
        return encontra_impares(list_of_elements, position+1, odds)
    else:
        print(odds)
        odds.append(list_of_elements[position])
        return encontra_impares(list_of_elements, position+1, odds)
    

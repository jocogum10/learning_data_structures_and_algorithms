def countdown(number):
    print(number)
    if number == 0:         # base case
        pass
    else:
        countdown(number-1)
    
countdown(10)
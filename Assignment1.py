# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    return max(num1, num2, num3) #simple max() test

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    return min(num1, num2, num3) #simple min() test

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:
        return("Positive") #checks pos
    elif number < 0:
        return("Negative") #checks neg
    else:
        return("Zero")  #the only other condition is 0 so it checks that

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    shape = "" # empty string
    for i in range(1, rows + 1):  
        shape += "*" * i + "\n" #this makes the lines one by one with a new line opp
    
    return shape.rstrip() #removes the last new line opp

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = ""
    num = 1
    while num <= limit: 
        if num % 3 == 0: #checks modulo for 3 (so basically checks that there's no remainder)
            result += ("Multiple of 3" + "\n") #if mult of 3
        else:
            result += (str(num) + "\n") #if NOT mult of 3
        num += 1

    return result.strip() #removes last new line opp

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    currentnumb = start

    while currentnumb <= end: #basic while loop nothing too complicated
        if currentnumb % 2 == 0:
            total += currentnumb 
        
        currentnumb += 1 #makes sure it doesn't continue doing the same thing

    return(total) #tbh this was easier than the last two

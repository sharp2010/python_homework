# Write your code here.
# task 1:
def hello ():
    return "Hello!"


# task 2:
def greet(name):
    return f"Hello, {name}!"

greet("Tracy")

# task 3:
def calc(val1, val2, operation="multiply"):
    try:    
        match operation:
            case "add":
                return val1 + val2
            case "subtract":
                return val1 - val2
            case "multiply":
                return val1 * val2
            case "divide":
                if val2 == 0:
                    raise ZeroDivisionError  # raise will trigger an exception
                return val1 / val2
            case "modulo":
                return val1 % val2
            case "int_divide":
                if val2 == 0:
                    raise ZeroDivisionError 
                return val1 // val2 # will round down
            case "power":
                return val1 ** val2 # will raise number to a power
            case _:
                return "Invalid operation"
    except ZeroDivisionError: # except will tell the program what to do if an error occurs
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    

 # Task 4





# task 5
def grade(*args):
    try:
        
        for x in args: #loop to validate each argument
            if not isinstance(x, (int, float)):
                 return "Invalid data was provided."
            
            
        num_grade = sum(args) # sum of the numbers
        total_num = len(args) # count of the numbers

        avg = num_grade / total_num  # will calculate the average


        if avg >= 90:
            grade_result = "A"
        elif avg >= 80:
            grade_result = "B"
        elif avg >= 70:
            grade_result = "C"
        elif avg >= 60:
            grade_result = "D"
        else:
            grade_result = "F"
    
        return grade_result

    except Exception:
        return "Invalid data was provided."
    
# task 6:
def repeat(string, count):
    result = ""

    for x in range(count):
        result += string

    return result

# task 7:
def student_scores(option, **kwargs):
    if option == "best": # check option for best
        best_student = max(kwargs, key=kwargs.get)  # finds the student with best score using max with the score as key
        return best_student
    
    elif option == "mean":
        if kwargs:
            ave_score = sum(kwargs.values())/ len(kwargs)
            return ave_score
        
# task 8
def titleize(str):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
       
    words = str.split() # this will split the string into words

    for i, word in enumerate(words): # iterate through the words 
        if i == 0 or i == len(words) - 1: # first and last words capitalized
            words[i] = word.capitalize()
        elif word.lower() not in little_words: # will capitalized if not a little word
            words[i] = word.capitalize()
        else:
            words[i] = word.lower() # keeps little words lower case

    return " ".join(words)

# task 9
def hangman(secret, guess):
    result = []  # start an empty list to store the results

    for letter in secret: # will loop through the letters in secret
        if letter in guess:
            result.append(letter) # if correct guess, it's append it to result
        else:
            result.append('_') # if wrong _ will be appended

    return ''.join(result)  # returns the list as a string

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

    def data_type_conversion():
        
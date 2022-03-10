# The Honest Calculator
msg_0 = "Enter an equation \n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n" 
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"
msg_ =["none", msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
oper_list = ["+", "-", "*", "/"]
memory = float(0)


def continue_calculator():
    answer_1 = input(msg_5)
    if answer_1 == "y":
        calculator()
    elif answer_1 == "n":
        quit()

def commit_memory():
    answer = input(msg_4)
    if answer == "y":
        global memory
        if is_one_digit(result) == True:
            msg_index = 10
            while msg_index <= 12:
                answer_2 = input(msg_[msg_index])
                if answer_2 == "y":
                    msg_index += 1
                elif answer_2 == "n":
                    continue_calculator()
            
            memory = result
        elif is_one_digit(result) == False:
            memory = result
            continue_calculator()
    elif answer == "n":
        continue_calculator()
    else:
        commit_memory()
    

def is_one_digit(v):
    while v > -10 and v < 10 and v.is_integer():
        output = True
        return output
    else:
        output = False
        return output

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
        msg = msg + msg_6
        
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
        
    if (v1== 0 or v2 == 0) and (v3 == "*" or "+" or "-"):
        msg = msg + msg_8
    
    if  msg != "":
        msg = msg_9 + msg
    
    print(msg)

def calculator(): 
    calc = input(msg_0)
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    
    if y == "M":
        y = memory

    while True: 
        if type(x) == str:
            try:
                x = float(x)
            except ValueError:
                print(msg_1)
                calculator()
                
        if type(y) == str:
            try:
                y = float(y)
            except ValueError:
                print(msg_1)
                calculator()
                
        if oper not in oper_list: 
            print(msg_2)
            calculator()
        check(x, y, oper)
        if oper == "+":  # Stage 2 - calculating 
            result = x + y
            print(result)
            commit_memory()
            continue_calculator()
        elif oper == "-":
            result = x - y
            print(result)
            commit_memory()
            continue_calculator()
        elif oper == "*":
            result = x * y
            print(result)
            commit_memory()
            continue_calculator()
        elif oper == "/" and y != 0:
            result = x / y
            print(result)
            commit_memory()
            continue_calculator()
        else:
            print(msg_3)
            calculator()

calculator()  # initial call

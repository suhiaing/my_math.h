def otherBase_to_decimal(num, u_type):
    d_value = 0
    idx = len(num) - 1
    i = 0
    while idx >= 0:
        if ord(num[idx]) >= 65:
            adding = ord(num[idx]) - 55
            digit = adding
        else:
            digit = int(num[idx])
        d_value += digit * (u_type ** i)
        idx -= 1
        i += 1
    return d_value

def decimal_to_otherBase(num, u_type):
    my_list = []
    while int(num) > 0:
        remin = int(num) % u_type
        if remin > 9:
            change = remin - 10
            my_list.append(chr(ord('A') + change))
        else:
            my_list.append(remin)
        num = (int(num) / u_type)
    my_list.reverse()
    num = "".join(str(i) for i in my_list)
    return num


def num_log_check(num, u_type):
    num_type_right = 1
    if u_type == 2:
        for i in range(len(num)):
            if num[i] not in ['0', '1']:
                num_type_right = 0
                print("invalid number of base 2")
                break
    elif u_type == 8:
        for i in range(len(num)):
            if num[i] not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                num_type_right = 0
                print("invalid number of base 8")
                break
    elif u_type == 10:
        for i in range(len(num)):
            if num[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num_type_right = 0
                print("invalid number of base 10")
                break
    elif u_type == 16:
        for i in range(len(num)):
            if num[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']:
                num_type_right = 0
                print("invalid number of base 16")
                break
    return num_type_right
  
while True:
    u_input = int(input("what do you want to do?\nPress 1. to change otherBase_to_decimal\nPress 2. to change decimal_to_otherBase\nEnter: "))
    if u_input == 1:
        num_type = 0
        while num_type not in [2, 8, 10, 16]:
            print("Which kind of number system do you want to change?")
            num_type = int(input("(Type 2, 8, 10, or 16) Enter: "))
       
        num_type_right = 0
        while num_type_right != 1:
            num = input("Enter any base number to change into decimal: ")
            num_type_right = num_log_check(num, num_type)
        result = otherBase_to_decimal(num,num_type)
        print("base",num_type,num,"==> to decimal",result)
    elif u_input == 2:
        num_type = 0
        while num_type not in [2, 8, 10, 16]:
            print("Which kind of number system do you want to change?")
            num_type = int(input("(Type 2, 8, 10, or 16) Enter: "))
        
        # num_type_right = 0
        # while num_type_right != 1:
        num2 = input("enter decimal number to change into other base: ")
            # num_type_right = num_log_check(num2, num_type)
        result2 = decimal_to_otherBase(num2,num_type)
        print("base 10",num2,"==>to base",num_type,"is",result2)
    
    
    
    
    

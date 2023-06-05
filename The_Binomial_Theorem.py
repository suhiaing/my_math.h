# my_ls = [2,3]
power = 4
def get_coefficient(power):
    coefficient = [1]
    divisor = 1
    multiplication = 1
    for i in reversed(range(1, power+1)):
        multiplication = multiplication * i
        coefficient.append(multiplication)
    print("Before division, coefficient be like:",coefficient)
    
    
    for i in range(1,power+1):
        divisor = divisor * i
        print("dividing",coefficient[i],"with",divisor)
        coefficient[i] = coefficient[i] / divisor
    print("After all coefficient are:",coefficient)

get_coefficient(power)

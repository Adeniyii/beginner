def add(a,b):
    print(f"This adds {a} and {b}.")
    return a+b

def sub(a,b):
    print(f"This subtracts {b} from {a}.")
    return a - b

def multi(a,b):
    print(f"This multiplies {b} and {a}.")
    return a * b

def divide(a,b):
    print(f"this divides {a} by {b}.")
    return a/b

age = add(20,5)
height = sub(20,14)
weight = multi(15,10)
iq = divide(200,2)

print(f"Age: {age}, height: {height}, weight: {weight}, and iq: {iq}.")
print("extra puzzle.")
what = add(age, sub(height, multi(weight, divide(iq, 2))))
print(f"magic number is: {what}!")

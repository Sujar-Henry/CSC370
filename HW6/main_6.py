#Arithmetic operations
def main():
    a = 5
    b = 3.5
    result = a + b
    print("Result: ", result)
    return 0
print("Arithmetic operations")
print(main())

# Assignment Compatibility
def main():
    a = 5
    b = float(a)
    a = b
    print("Value of b: ", b)
    return 0
print("Assignment Compatibility")
print(main())

#Function Calls

def printMessage(num):
    print("Integer:",num)

def main():
    num = 3.5
    printMessage(num)
    return 0

print("Function Calls")
print(main())

#Comparison Operations
def main():
    a = 5
    b = 3.5
    if a == b:
        print("Equal")
    else:
        print("Not Equal")
    return 0
    
print("Comparison Operations")
print(main())

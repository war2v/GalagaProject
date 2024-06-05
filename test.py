a = 1 
b = 2

print("****************SIMPLE CALCULATOR****************")

while True:
    a = input("Enter a Number: ")
    b = input("Enter a Number: ")
    op = input("Enter Operation(+, -, *, /, %): ")

    match(op):
        case "+":
            c = int(a) + int(b)
        case "-":
            c = int(a) - int(b)
        case "*":
            c = int(a) * int(b)
        case "/":
            c = int(a) / int(b)
        case "%":
            c = int(a) % int(b)

    print(c)
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

        






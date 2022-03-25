def print_hi(name):
    print(f'Hello {name}')


if __name__ == '__main__':
    print_hi('Glasgow!')
    print("finding the average of two numbers: ")
    x = float(input("number x: "))
    y = float(input("number y: "))
    av = (x + y) / 2
    print(f'average of these two numbers: {av}')

    mod_code = input("Enter module code: ")
    match mod_code:
        case "CSC1009":
            print("Object-Oriented Programming")
        case "CSC1008":
            print("Data-struct and algo")
        case "CSC1010":
            print("Computer networks")
        case "CSC1007":
            print("Operating Systems")
        case _:
            print("Something is wrong")

    print("=== starting to count down odd numbers ===")
    for x in range(102, 65, -1):
        if x % 2 != 0:
            print(x, end=" ")

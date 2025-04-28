def methodss():
    number = input("Enter the number")
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    elif number % 3 == 0 and number % 5 == 0:
        return "fizzBuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"

    else:
        return f"Invalid {number}"

if __name__ == "__main__":
    print(methodss)
    try:
         number = int(input("Enter a number: "))
         print(methodss(number))
    except ValueError:
        print("Invalid input! Please enter an integer.")
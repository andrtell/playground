def ask_amount():
    while 1:
        try:
            return float(input("Enter amount: "))
        except ValueError:
            print("Please enter a number!")
    else:
        return 0

def ask_tax():
    while 1:
        try:
            return float(input("Enter tax (%): "))
        except ValueError:
            print("Please enter a number!")
    else:
        return 0

if __name__ == "__main__":
    amount = ask_amount()
    tax = ask_tax()
    total = amount * (1 + tax / 100)
    print(f"Total is {total}")

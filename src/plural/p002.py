def ask_age():
    while 1:
        try:
            return int(input("How old are you?\n"))
        except ValueError:
            print("Please enter an integer...")
    else:
        return 0


if __name__ == "__main__":
    age = ask_age()
    decades = age // 10
    years = age % 10
    print(f"You are {decades} decades and {years} years old.")

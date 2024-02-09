import itertools as it
import random
import pyperclip


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

characters = {
    "Uppercases": 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    "Lowercases": 'abcdefghijklmnopqrstuvwxyz',
    "Numbers": '0123456789',
    "Symbols": '!@#$&*?_-',
}

def get_password_length():
    while True:
        try:
            return int(input("\tLength of Password: "))
        except ValueError:
            print(bcolors.FAIL + "Entered value should be an integer.")
            print("Restarting the program...")
            print(bcolors.OKBLUE + "")

def get_character_type():
    print(bcolors.OKGREEN + "Select character type number from the list: ")
    arr = ["Numbers", "Uppercases", "Lowercases", "Symbols"]
    l1 = list(it.combinations(arr, 1))
    l2 = list(it.combinations(arr, 2))
    l3 = list(it.combinations(arr, 3))
    l4 = list(it.combinations(arr, 4))
    l = l1 + l2 + l3 + l4  # list of all possible combinations of characters

    for i, combination in enumerate(l, start=1):
        print(f"\t{i} --- {combination}")

    print(bcolors.OKBLUE + "")
    while True:
        try:
            c_type = int(input("Type any serial number from the above list of combinations: "))
            if c_type in range(1, len(l) + 1):
                return l[c_type - 1]
            else:
                print(bcolors.HEADER + f"Serial number should be from 1 to {len(l)}...")
                print(bcolors.OKBLUE + "")
        except ValueError:
            print(bcolors.FAIL + "Entered value should be an integer.")
            print("Restarting the program...")
            print(bcolors.OKBLUE + "")

def gen_pass(length, char_combination):
    print(char_combination)
    c_per_pass = length // len(char_combination)
    extra_c = length - (c_per_pass * len(char_combination))
    password_l = []
    all_char = []

    for char_set in char_combination:
        all_char.extend(characters[char_set])
        password_l.extend(random.choices(characters[char_set], k=c_per_pass))

    e_c = random.choices(all_char, k=extra_c)
    password_l.extend(e_c)
    random.shuffle(password_l)
    password = "".join(password_l)
    print(bcolors.HEADER + "Your password: ", password)
    pyperclip.copy(password)
    print(bcolors.OKCYAN + "Your password is copied to your clipboard.")

def main():
    while True:
        print(bcolors.OKBLUE + "Starting Password Generator...")
        print("")
        password_length = get_password_length()
        char_combination = get_character_type()
        gen_pass(password_length, char_combination)

        another_pass = input("Do you want to generate another password? (yes/no): ").lower()
        if another_pass != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()

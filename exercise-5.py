import random

def guessing_number(r_nmr= random.randint(1, 5), g_nmr = int(input("enter a number between 1 and 100: "))):
    
    if r_nmr == g_nmr:
        print(f"Correct!")
    else:
        print(f"Not Correct! \nyou entered: {g_nmr} \nthe correct answer is: {r_nmr}")

guessing_number()

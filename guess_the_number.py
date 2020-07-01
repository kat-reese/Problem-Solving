import random
class guess_the_number:
    def __init__(self):
        print("Guess a number!")
        n = 0
        randnum = random.randint(1, 199)
        num_tries = 0
        while(n != randnum):
            n = int(input("Enter a number between 0 and 200 >>> "))
            num_tries += 1
            if n < randnum:
                print("Too small")
            elif n > randnum:
                print("Too large")

        print("You got it!!! The number was %d." % randnum)
        print("\nNumber of Tries: %d" % num_tries)


def main():
    number = guess_the_number()

if __name__ == "__main__":
    main()

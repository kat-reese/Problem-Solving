class greetings:
    def __init__(self):
        name = input("Hello! What is your name? >>> ")
        print("Nice to meet you %s!" % (name))

def main():
    get_greetings = greetings()

if __name__ == "__main__":
    main()
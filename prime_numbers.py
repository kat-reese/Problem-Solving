class prime_numbers:
    def __init__(self):
        n = int(input("Enter a whole number >>> "))
        prime = True
        print("Prime numbers up to %d: " % n)
        for i in range(1, n + 1):
            # print("i: %d" % i)
            for j in range(2, i + 1):
                # print("j: %d" % j)
                if i % j == 0 and i != j:
                    prime = False
            if i == 1:
                prime = False
            if prime == True:
                print("%d " % i, end='')
            prime = True
        print()



def main():
    prime = prime_numbers()

if __name__ == "__main__":
    main()
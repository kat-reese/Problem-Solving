class sum_or_product:
    def __init__(self):
        try:
            n = int(input("Please enter a whole number: "))
            pors = input("Please enter (s) or (p) for sum or product of the numbers up to your number: ")
            sum = 0
            product = 1
            for i in range(1, n + 1):
                if pors == "s":
                    sum += i
                elif pors == "p":
                    product *= i
                else:
                    print("invalid answer please enter p or s")
            if pors == "s":
                print("Total sum: %d" % sum)
            elif pors == "p":
                print("Total Product: %d" % product)      

        except:
            print("Enter a whole number!")

def main():
    sorp = sum_or_product()

if __name__ == "__main__":
    main()
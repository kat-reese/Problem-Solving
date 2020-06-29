class sum_to_n:
    def __init__(self):
        try:
            n = int(input("Enter a whole number: >>> "))
            print("Your number is %d." % n)
            sum = 0
            for i in range(1, n + 1):
                sum += i
            print("The sum of 1 to %d is %d" % (n , sum))
        except:
            print("Please enter a whole number!")
        

def main():
    one_to_n = sum_to_n()

if __name__ == "__main__":
    main()
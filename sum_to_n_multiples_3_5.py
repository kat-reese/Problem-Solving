class sum_to_n_mult_3_5:
    def __init__(self):
        try:
            n = int(input("Please Enter a whole number: >>> "))
            print("Your number is %d" % n)
            sum = 0
            for i in range(1, n + 1):
                if i % 3 == 0 or i % 5 == 0:
                    sum += i
            
            print(sum)


        except:
            print("Please enter a whole number!")

def main():
    mult_3_5 = sum_to_n_mult_3_5()

if __name__ == "__main__":
    main()

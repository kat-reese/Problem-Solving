class multiplication_table:
    def __init__(self):
        print(" _____________________________________________________________________________________________________________________________")
        print("|\t\t\t\t\t\t\tMultiplication Table\t\t\t\t\t\t      |")
        print("|_____________________________________________________________________________________________________________________________|")
        print("|\t", end="")
        for i in range(0, 13):
            print("\t%d" % i, end = "")    
        print("\t      |")  
        print("|_____________________________________________________________________________________________________________________________|")

        for i in range(0, 13):
            print("\t%d" %i, end= "")
            for j in range(0, 13):
                print("\t%d" % (j * i), end= "")
            print("")

def main():
    mult_table = multiplication_table()

if __name__ == "__main__":
    main()
class leap_years:
    def __init__(self):
        last_leap_year = 2020
        num_leaps = 0
        print("Next 20 leap years: ", end = "")
        while num_leaps != 20:
            last_leap_year += 4
            print(last_leap_year, end = " ")
            num_leaps += 1
        print()

def main():
    leap = leap_years()

if __name__ == "__main__":
    main()

#!/usr/bin/python3
import sys

def banner():
    print("*"*50)
    print("\t\t\tLeap Year Finder")
    print("*"*50)

def leapYearFinder(year:int):
    try:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("[+] {} is a leap year".format(year))
                else:
                    print("[-] {} is not a leap year".format(year))
            else:
                print("[+] {} is a leap year".format(year))
        else:
            print("[-] {} is not a leap year".format(year))
    except Exception as e:
        print("Error: ",e)
        sys.exit()


if __name__ == "__main__":
    banner()
    try:
        year = int(input("\nEnter Year: "))
        leapYearFinder(year)

    except :
        print("Please Enter intiger value as an Year.")
        sys.exit()
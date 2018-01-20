print ("*****FIZZBUZZ*****")
print ''
print ("Hi! This is a simple game named FizzBuzz")
print ("You will enter a number from 1 to 100")
print("The program will count to the number you entered.")
print("- If the number is divisible with 3 it will display fizz")
print("- If the number is divisible with 5 it will display buzz")
print("- if both it will display fizzbuzz")
print ''

while True:

    numbers = raw_input("Please enter a number from 1 to 100:")
    numbers = int(numbers)

    for choice in range(1, numbers+1):
        if choice % 3 == 0 and choice % 5 == 0:
            print "fizzbuzz"
        elif choice % 3 == 0:
            print "fizz"
        elif choice % 5 == 0:
            print "buzz"
        else:
            print choice

    print ""
    repeat = raw_input("Repeat game? Y/N")
    if repeat.upper() == "Y":
        print numbers
    else:
        print("Thank you and goodbye!")
        break

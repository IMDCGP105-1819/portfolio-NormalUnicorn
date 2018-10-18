def fizzbuzz(low, high):
    i = low
    for i in range(low, high+1):
        # high + 1 so that it includes the high value
        output = ""
        if i % 3 == 0:
            output += "Fizz"

        if i % 5 == 0:
            output += "Buzz"

        print(output, i)
        # print out i so that you can check if the value is fizz buzz or not

def inputs():
    low_val = int(input("Please enter a lower value to start searching from"))
    high_val = int(input("Please enter a high value to search up to"))
    fizzbuzz(low_val, high_val)

inputs()

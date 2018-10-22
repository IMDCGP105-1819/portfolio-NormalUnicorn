def fizzbuzz(low, high):
    ''' This function takes the range specified and looks at each number
    it will then add fizz/buzz to the output depening on the number '''
    i = low
    for i in range(low, high+1):
        # high + 1 so that it includes the high value
        output = ""
        if i % 3 == 0:
            output += "Fizz"

        if i % 5 == 0:
            output += "Buzz"

        print(i, output)
        # print out i so that you can check if the value is fizz buzz or not

def inputs():
    '''This function takes in inputs for the range to find fizzbuzz between'''
    low_val = int(input("Please enter a lower value to start searching from"))
    high_val = int(input("Please enter a high value to search up to"))
    fizzbuzz(low_val, high_val)

inputs()

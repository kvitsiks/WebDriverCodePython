# To get number inputs:
    print 'Enter the numbers.'
    read = sys.stdin.readline()
    # Getting the String input (...numbers of type String, not Integer!) into an array
    array = read.split()
    # Converting String content of array into an Integer.
    firstNumber = int(array[0])
    secondNumber = int(array[1])
    thirdNumber = int(array[2])
# etc. etc.
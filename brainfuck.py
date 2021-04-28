def interpret(code):
    # initialize the array
    array = [0]
    # start from zero location
    Location = 0
    i = 0
    while i < len(code):
        if code[i] == '<':
            if Location > 0:
                Location -= 1
        elif code[i] == '>':
            Location += 1
            if len(array) <= Location:
                array.append(0)
        elif code[i] == '+':
            array[Location] += 1
        elif code[i] == '-':
            if array[Location] > 0:
                array[Location] -= 1
        elif code[i] == '.':
            # output the value in the array
            print(array[Location])
        elif code[i] == ',':
            x = input("Input:")
            array[Location] = x
        elif code[i] == '[':
            if array[Location] == 0:
                while code[i] != ']':
                    i += 1
        elif code[i] == ']':
            if array[Location] != 0:
                while code[i] != '[':
                    i -= 1
        i += 1
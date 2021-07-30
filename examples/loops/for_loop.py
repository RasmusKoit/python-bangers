def looper(letsLoopThis):
    for element in letsLoopThis:
        print(element)


def doubleLooper(letsLoopThisHarder):
    for firstElement in letsLoopThisHarder:
        print("Our first loop is looping: ")
        print(firstElement)
        for secondElement in firstElement:
            print("Our second loop is looping: ")
            print(secondElement)

if __name__ == "__main__":
    ######################################

    name = "Rasmus Koit"
    numbers = [10, 20, 30, 40, 50]
    matrix = [ # 3 x 3 matrix
        ['x', 'y', 'f'],
        ['a', 'b', 'c'],
        ['k', 'h', 'l']
    ]
    fruits = ["lemon", "apple", "orange", 
            "mandarin", "banana"]

    #######################################
    # One loop examples
    print("Single loop: NAME")
    looper(name)
    print("Single loop: NUMBERS")
    looper(numbers)
    print("Single loop: MATRIX")
    looper(matrix)
    print("Single loop: FRUITS")
    looper(fruits)
    
    # Double loop examples
    print("Double loop: NAME")
    doubleLooper(name)
    # doubleLooper(numbers)
    print("Double loop: MATRIX")
    doubleLooper(matrix)
    print("Double loop: FRUITS")
    doubleLooper(fruits)
test =int(input("Enter a number: "))

def test_is_valid(test):
    number = isinstance(test, int)  and  (1< test< 3)
    return number


print(test_is_valid(test))


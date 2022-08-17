def isFloatingPointNumber(testNumber):
    try:
        float(testNumber)
        return True
    except:
        ValueError
        return False


def validate(textNumbers, isHappyCase):
    for testNumber in textNumbers:
        if isFloatingPointNumber(testNumber) == isHappyCase:
            print("Test Passed")
        else:
            print("Test Failed")


validate(["1234567890.10", "0.1", "-0.1"], True)
validate([".0", "0.", "1a1", "0.0.0", "", "-0.a"], False)

def raiseToPower(baseNumber, powerNumber):
    result = 1
    for index in range(powerNumber):
        result = result * baseNumber

    return result


print(raiseToPower(3, 3))
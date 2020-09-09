'''
Write a program for converting weight from Pound to Kilo grams.
       a)  Use assertion for the negative weight.
       b) Use assertion to weight more than 100 KG
'''


# a
def PoundToKg(pound):
    try:
        assert (pound >= 0), "Negative weight not allowed"
        return pound * 0.453592
    except AssertionError as e:
        return e


print(PoundToKg(1233))
print(PoundToKg(-123))


# b
def PoundToKg(pound):
    try:
        assert (pound >= 100), "Weight should be more than or equal to 100"
        return pound * 0.453592
    except AssertionError as e:
        return e


print(PoundToKg(98))
print(PoundToKg(231))
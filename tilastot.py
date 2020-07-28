import numpy
from scipy import stats

def statistics():

    numbers = input("Anna numerosarja: ")
    list_numbers = numbers.split()

    #biggest
    max_num = max(list_numbers)

    #smallest
    min_num = min(list_numbers)

    #mean value
    mean = numpy.mean(list_numbers)

    #median value
    median = numpy.median(list_numbers)

    #mode value
    mode = stats.mode(list_numbers)

    print(f"Suurin luku: {max_num}, pienin luku: {min_num}, keskiarvo: {mean}, mediaani {median}, moodi {mode}")

statistics()
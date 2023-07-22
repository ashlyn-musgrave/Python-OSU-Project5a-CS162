# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/21/2023
# Description:This program takes the numerical values of a .txt file, adds them together, then outputs
# the sum into a new .txt called sum.txt

def file_sum(filename_txt):
    """A function that takes as a parameter a txt file that contains a list of numbers, adds them
    then writes the sum to a separate txt file"""
    sum = 0
    with open(filename_txt, 'r') as sum_find:
        for line in sum_find:
            numbers = line.split(',')
            for num in numbers:
                sum += float(num)
    with open('sum.txt', 'w') as outfile:
        outfile.write(str(sum))

    sum_find.close()
    outfile.close()
    return sum


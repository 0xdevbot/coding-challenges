def is_perf_square(num):
    '''
    Instead of doing a simple cmath.sqrt(num) to find out. I decided to make it a little more challenging and use
    Digital Roots to solve the problem.
    :param num: input number
    :return: returns a boolean True if perf square, False if otherwise
    '''
    snum = str(num)
    result = 11
    perf_square_array = ['1', '4', '5', '6', '9', '0']
    non_square = ['2', '3', '7', '8']
    if snum[-1] in non_square or num < 0:
        return False
    for x in perf_square_array:
        snum = snum.replace(x, '')
    array = list(snum)
    while int(result) > 10:
        for i in array:
            result = 0
            result += int(i)
        array = list(str(result))
    if array[0] in perf_square_array:
        return True



print(is_perf_square(64))
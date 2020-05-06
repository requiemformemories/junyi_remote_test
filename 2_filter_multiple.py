def filter_multiple(i):
    if i % 15 == 0:
        return True
    if (i % 3 == 0) or (i % 5 == 0):
        return False
    return True

number = input('Input：')
result = [str(i) for i in range(1, int(number)) if filter_multiple(i)]
result = ', '.join(result)
print('所有的數字是：', result)

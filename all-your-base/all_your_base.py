def rebase(input_base, digits, output_base):
    if len(digits) == 0:
        return [0]
    newList = []

    if len(digits) > 1:
        for index,element in enumerate(digits):
            if element < 0:
                return
            item = element * input_base ** index
            newList.append(item)
    else:
        for index,element in enumerate(digits):
            if element < 0:
                return
            item = element * input_base ** index
            newList.append(item)
    return newList


# [2,10]
print(rebase(3, [1, 1, 2, 0], 16))
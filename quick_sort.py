def quick_sort(data_list):
    if len(data_list) <= 1 :
        return data_list
    pivot = data_list[0]
    left, right = list(), list()
    for i in range(1,len(data_list)):
        if pivot > data_list[i]:
            left.append(data_list[i])
        else:
            right.append(data_list[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

"""
def quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[0]
    left = [data_list[i] for i in data_list[1:] if pivot > data_list[i]]
    right= [data_list[j] for j in data_list[1:] if pivot <= data_list[j]]
    return quick_sort(left) + [pivot] + quick_sort(right)
"""
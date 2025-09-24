def insertion_sort(arr):
    for i in range(1, len(arr)):
        # 选择当前索引作为关键字
        key = arr[i]
        # 插入到[1,i-1]的有序子数组中
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
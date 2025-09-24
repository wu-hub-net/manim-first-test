import time
import random
from InsertionSort import insertion_sort
from MergeSort import merge_sort
# 生成长度为n的随机序列count个
def generate_random_sequences(n, count=20):
    sequences = []
    for _ in range(count):
        # 生成1到n的随机排列
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        sequences.append(numbers.copy())
    return sequences
# 比较插入排序和归并排序在随机序列上的性能
def compare_sorting_algorithms_with_random(n, sequence_count=20):
    
    # 生成随机序列
    sequences = generate_random_sequences(n, sequence_count)
    # 总计算时间
    insertion_total = 0
    merge_total = 0
    # 对每个序列进行测试
    for i, seq in enumerate(sequences):
        # 插入排序
        arr1 = seq.copy()
        start_time = time.perf_counter()
        insertion_sort(arr1)
        insertion_time = time.perf_counter() - start_time
        insertion_total += insertion_time
        
        # 归并排序
        arr2 = seq.copy()
        start_time = time.perf_counter()
        merge_sort(arr2, 0, len(arr2) - 1)
        merge_time = time.perf_counter() - start_time
        merge_total += merge_time
    return n,insertion_total, merge_total ,insertion_total / merge_total

def main():
    for n in range(0, 20):
        m,insertion_total, merge_total ,speedup = compare_sorting_algorithms_with_random(n * 10)
        print(f"n={m}: 插入排序总时间={insertion_total:.6f}秒, 归并排序总时间={merge_total:.6f}秒, 加速比={speedup:.2f}")

if __name__ == "__main__":
    main()

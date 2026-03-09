import random

def fisher_yates_shuffle(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)  # chọn vị trí ngẫu nhiên
        arr[i], arr[j] = arr[j], arr[i]  # hoán đổi

    return arr


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Danh sách ban đầu:", numbers)

shuffled = fisher_yates_shuffle(numbers)

print("Danh sách sau khi trộn:", shuffled)
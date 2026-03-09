import random

# Danh sách số
numbers = [3, 7, 1, 9, 5, 8, 2, 6, 4]

# Số cần tìm
target = 5

# Thuật toán tìm kiếm ngẫu nhiên
found = False
attempt = 0

while not found:
    attempt += 1
    index = random.randint(0, len(numbers) - 1)
    
    print("Lần thử", attempt, "- Kiểm tra vị trí:", index)

    if numbers[index] == target:
        found = True
        print("Đã tìm thấy số", target, "tại vị trí", index)
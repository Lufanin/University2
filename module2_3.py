b = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while b<len(my_list):
    if my_list[b] > 0:
        print(my_list[b])
        b += 1
    elif my_list[b] == 0:
        b += 1
        continue
    elif my_list[b] < 0:
        break

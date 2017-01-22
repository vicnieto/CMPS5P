def h(k, i):
    return (k%11 + i * (1 + k%10)) % 11

nums = []

def insert_num(ls):
    for i in range(20):
        ls.append(i + 1)

insert_num(nums)
print(nums)

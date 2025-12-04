LIST = []

def simp(n, LIST):
    if n == 1:
        return LIST
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                LIST.append(i)
                return simp(int(n/i), LIST)
            
print(simp(666, LIST))
list = [1]

def simp(n, i, list):
    if list[-1] == n:
        return list
    if i <=n:
        if n % i == 0:
            for t in range(2, i):
                if t % i == 0:
                    pass
                else:
                    list.append(i)
        else: 
            print(list)
    return simp(n, i+1, list)
    

simp(666, 2, list)

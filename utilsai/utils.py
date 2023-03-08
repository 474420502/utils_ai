def get_approximation(h):
    """
    获取数值的所有约数
    """
    a_h = []

    is_loop = True
    while is_loop:
        for i in range(2,h+1):
            if h % i == 0:
                a_h.append(i)
                if h == i:
                    is_loop = False
                h = h // i 
                break

    return a_h
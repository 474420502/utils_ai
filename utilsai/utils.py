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

def get_max_approximation(h,w):
    """
        获取所有最大约数. 总乘积就是最大
    """
    hl = get_approximation(h)
    wl = get_approximation(w)

    hl_del_list = []
    for i in range(len(hl)):
        a = hl[i]
        for b in iter(wl):
            if a == b:
                hl_del_list.append(a)
                wl.remove(b)
                break

    return hl_del_list
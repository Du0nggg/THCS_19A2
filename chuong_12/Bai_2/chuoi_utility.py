def dao_nguoc_chuoi(chuoi):
    dao_nguoc = ""
    i = len(chuoi) - 1
    while i >= 0:
        dao_nguoc += chuoi[i]
        i -= 1
    return dao_nguoc    
def dem_so_tu(chuoi):
    return len(chuoi.split())




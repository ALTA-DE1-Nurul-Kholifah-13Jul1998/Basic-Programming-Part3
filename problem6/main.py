def full_prima(N):
    if N<=1:
        return False
        
    def cekprima(N):
        if N<=1:
            return False
        for i in range(2, N):
            if N%i==0:
                return False
        return True
        
    perdigit = str(N)
    for e in perdigit:
        if cekprima(int(e)) == False:
            return False
    return cekprima(N)

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True
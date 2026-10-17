import sys

def main():
    data = sys.stdin.buffer.read().split()
    n,M = int(data[0]),int(data[1])
    inv = [(int(data[2+2*i]),int(data[3+2*i])) for i in range(n)]


    def check(d):
        s = 0
        for p,c in inv:
            g = p*d - c
            if g > 0:
                s += g
                if s >= M:
                    return True


        return False

    lo,hi = 1, 2*10**9
    while lo < hi:
        mid = (lo+hi)//2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1

    print(lo)

main()
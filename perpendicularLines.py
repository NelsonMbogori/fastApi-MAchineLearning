def perpendicular(n):
    if (n==0 or n==1):
        return 0
    else:
        if n % 2 == 0:
            x = n/2
            y = n-x
            return x*y
        else:
            x = (n-1)/2
            y = n-x
            return x*y
perpendicular(8)
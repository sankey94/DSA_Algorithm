def closest_number(n,m):
    r = n % m
    n1 = n - r
    n2 = n1 + m if n * m > 0 else n1-m
    if abs(n-n1) < abs (n-n2):
        return n
    elif abs(n-n2)< abs(n-n1):
        return n2
    else:
        return n1 if abs(n1) > abs(n2) else n2

 
 
result= closest_number(18,4)
print(result)
 
 

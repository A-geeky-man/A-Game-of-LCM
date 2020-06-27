# My code goes here
'''You are given an integer N.
You have to find 4 integers i,j,k,l less than equal to N such that lcm(i,j,k,l) is maximum.'''


def find_gcd(num1, num2):
    if num1 > num2:
        a = num1
        b = num2
    else:
        a = num2
        b = num1
    while b:
        a, b = b, a % b
    return a


def find_lcm(n):
    lcm = n
    ctr = 1
    for num in reversed(range(2, n)):
        if find_gcd(lcm, num) == 1:
            lcm *= num
            ctr += 1
        if ctr >= 4:
            break
    return lcm


for t in range(int(input().strip())):
    n = int(input().strip())
    ans = find_lcm(n)
    print(ans)

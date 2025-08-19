# https://www.codewars.com/kata/54d512e62a5e54c96200019e/solutions

def prime_factors(n):
    i = 2
    ans = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            pow = 0
            while n % i == 0:
                pow += 1
                n //= i
            if pow == 1:
                ans.append(f'({i})')
            elif pow > 1:
                ans.append(f'({i}**{pow})')
    if n > 1:
        ans.append(f'({n})')
    return ''.join(ans)


print(prime_factors(n))
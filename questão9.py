def primo(n):
    
    for d in range (2, n):
        if n % d == 0:
            return False
        
    return True 

n = int(input())

primos = [x for x in range(2, n+1) if primo(x)]

print(primos)
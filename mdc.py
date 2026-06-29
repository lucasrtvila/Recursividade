def mdcRecursivo (a,b):
    if b == 0:
        return a
    return mdcRecursivo(b, a%b)

a = int(input("Digite o número A: "))
b = int(input("Digite o número B: "))

if a <= 0 or b <= 0:
    print("Os números devem ser maiores do que zero.")
else:
    mdc = mdcRecursivo(a,b)
    print(f"O máximo divisor comum entre {a} e {b} é {mdc}.")
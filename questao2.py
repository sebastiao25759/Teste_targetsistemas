numerosFibonacci = [0, 1]
sequenciaFibonacci = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
for i in range(2, sequenciaFibonacci):
    numerosFibonacci.append(numerosFibonacci[i-1] + numerosFibonacci[i-2])
print(numerosFibonacci)
for sequencia in numerosFibonacci:
    print(f"{sequenciaFibonacci} faz parte da sequência de Fibonacci!")
    break
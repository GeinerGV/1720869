from os import system
system("cls")
nums = []

def minNumber(numeros):
    if len(numeros)>0:
        min = numeros[0]
        for num in numeros:
            if min > num:
                min = num
        return min
while len(nums)<5:
    try:
        num = int(input("Ingrese el valor del número "+ str(len(nums)+1) + " >> "))
        nums.append(num)
    except Exception:
        pass
    finally:
        system("cls")
        for i in range(len(nums)):
            print("Número "+str(i+1)+":", nums[i])

print("\nEl número menor de la lista es:", minNumber(nums), "\n")
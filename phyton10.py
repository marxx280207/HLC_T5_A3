def eliminar_pares(nums):
    return [num for num in nums if num % 2 != 0]

print(eliminar_pares([1, 2, 3, 4, 5, 6]))
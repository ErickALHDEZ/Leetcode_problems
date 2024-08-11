import random

nums = [random.randint(1,31) for i in range(random.randint(3,13))]

digito1_suma = random.choice(nums)

nums_sin_digito1 = [num for num in nums if num != digito1_suma]

digito2_suma = random.choice(nums_sin_digito1)

target = digito1_suma + digito2_suma

print(nums)
print(target)

def twoSum(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

resultado = twoSum(nums,target)
print(resultado)

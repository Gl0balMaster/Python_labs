x = (input("Веедите числа: "))
nums = x.split()
numstyped = dict()
for num in nums:
    numstyped[float(num)] = 1

max1 = max(numstyped)
nums = sorted(numstyped)
print(nums[len(nums) - 2])
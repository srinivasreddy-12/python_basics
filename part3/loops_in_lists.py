nums = [1,3,5,6,78,3]
#finding 6th value index
k = 0
for i in nums:
    if nums[i] == 6:
        k = i
        break
print(k)

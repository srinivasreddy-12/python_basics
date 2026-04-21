nums = [1,2,3,4,5,6]
#adding one element at end
nums.append(39)
print(nums)

#inserting value at second index 
nums.insert(2,23)
print(nums)

#sorting in increasing order in original list
nums.sort()
print(nums)

#sorting in decreasing order in orginal list
nums.sort(reverse = True)
print(nums)

#reversing the list
nums.reverse()
print(nums)

#sorting in updated list in decreasing order
sorted_nums = sorted(nums,reverse = True)
print(sorted_nums)
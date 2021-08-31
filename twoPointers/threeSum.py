def threeSum(nums):
  res = []
  nums.sort()
  
  if len(nums) < 3:
      return []
  
  for i in range(len(nums)-2):
    fnum = nums[i]
    for j in range(i+1, len(nums)-1):
      snum = nums[j]
      for k in range(j+1, len(nums)):
        tnum = nums[k]
        
        if fnum + snum + tnum == 0:
          res.append(tuple([fnum,snum,tnum]))
          
                  
  print(list(set(res)))
                  
  print(res)

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

'''
set operation, requires passing in hashable objects 
lists are not hashable

sort => save it into a tuple => use set => convert it to list
'''

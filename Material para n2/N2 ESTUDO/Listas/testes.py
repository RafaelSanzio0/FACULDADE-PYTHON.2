k = 0
sum = 0
nums = range(100)
while k < len(nums) and sum < 100:
    sum = sum + nums[k]
    k = k + 1
    print(nums[k],sum,k)

print('Os primeiros', k, 'inteiros somam 100 ou mais')


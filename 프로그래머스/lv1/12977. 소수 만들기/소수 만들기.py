def solution(nums):
    count = 0
    answer = 0
    prime = []
    nums.sort()
    
    for i in range(0, len(nums) - 2):
        # print(i)
        for j in range(i+1, len(nums) - 1):
            # print(j)
            for k in range(j+1, len(nums)):
                prime.append(nums[i]+nums[j]+nums[k])
                # print(k)
                # pass
    for l in range(len(prime)):
        for m in range(1, prime[l]+1):
            if prime[l] % m == 0:
                count += 1

        if count == 2:
            answer += 1
            count = 0
        else:
            count = 0
    
    return answer
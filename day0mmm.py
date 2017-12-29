import sys
count = 0
nums = []

def mean():
    print(sum(nums)/count)
def median():
    nums.sort()
    if count % 2 == 1:
        print(nums[count/2])
    else:
        print(sum(nums[int(count/2-1):int(count/2+1)])/2)
def mode():
    num_count = {}
    # count occurences 
    for i in nums:
        if i in num_count:
            num_count[i] += 1
        else:
            num_count[i] = 1 
    # merge occurences
    counts = {}
    highest = 0
    for n in num_count:
        i = num_count[n]
        if i > highest:
            highest = i
        if i in counts:
            counts[i] += [n]
        else:
            counts[i] = [n]
    # get mode
    print(min(counts[highest]))
    
    
for line in sys.stdin:
    x = [int(x) for x in line.split()]
    if len(x) == 1:
        count = x[0]
    else:
        nums = x
mean()
median()
mode()

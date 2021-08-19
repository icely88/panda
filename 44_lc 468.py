nums=[1,5,2]
n=len(nums)
mem=[[0]* n for i in range(n)]
print(mem)
def select_number (l,r):
    if l ==r:
        return nums[l]
    if mem[l][r]>0:
        return mem[l][r]
    mem[l][r]=max(nums[l]-select_number(l+1, r),nums[r]-select_number(l, r-1))
    return mem[l][r]
print(select_number(0, 2))
print(mem)

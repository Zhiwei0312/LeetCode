# sort the array, the majority one will for sure be the one in the center
class Solution:
# time, storage
# O(nlogn), O(1)
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort();

        N = len(nums);
        nb = floor(N/2);
        return nums[nb]

    
# Boyer-Moore投票算法
# 多数元素和非多数元素可以两两滴小，最后剩下的一定是多数元素
# 因为多数元素数量>其他所有元素数量之和

# O(n), O(1)
    def majorityElement_BoyerMoore(self, nums: List[int]) -> int:
        candidate = None;
        count = 0;

        for num in nums:
            if count == 0:
                candidate = num;
            
            if num == candidate:
                count = count + 1;
            else:
                count = count - 1;
        return candidate

# nums = [2,2,1,1,1,2,2]

# num   candidate   count   解释
# 2        2          1     新候选
# 2        2          2     支持
# 1        2          1     抵消
# 1        2          0     抵消完
# 1        1          1     新候选
# 2        1          0     抵消
# 2        2          1     新候选

# Hash table: 建立key和value之间的映射，实现高效的元素查询
# 要让键值对应到内存中的位置，就要为键值计算索引，
# 也就是计算这个数据应该放到哪里．
# 这个根据键值计算索引的函数就叫做哈希函数，也称散列函数．
# 举个例子，如果键值是一个人的身份证号码，哈希函数就可以是号码的后四位，
# 当然也可以是号码的前四位．生活中常用的「手机尾号」也是一种哈希函数．

# O(n), O(n)
    def majorityElement_HashTable(self, nums: List[int]) -> int:
        freq = {}; # this defines a dictionary, i.e., a Hash table
        n = len(nums); 

        for x in nums:
            # dict.get(key, default):
            # if x is in the dict, return dict[x]
            # else, return 0
            freq[x] = freq.get(x,0) + 1;
            if freq[x] > n // 2:
                return x
        
        return None;
                

class Solution:
# O(nlogn), O(logn)
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        N = len(citations)
        h = 0

        for i in range(N):
            if citations[i] >= i+1:
                h += 1;
        
        return h
    
# 把所有论文按“引用次数”分桶统计
# 只关心 0 ~ n 次（超过 n 的全部算 n）
    def hIndex_hash(citations):
        N = len(citations)
        table = []

        for c in citations:
            # bin the h index within N, as h cannot be larger than N
            if c >= N:
                table[n] += 1
            else:
                table[c] += 1

        total = 0

        for h in range(n,-1,-1):
            total += table[h]
            if total >= h:
                return h
            
# 把所有论文按“引用次数”分桶统计
# 只关心 0 ~ n 次（超过 n 的全部算 n）
# O(N), O(N)
    def hIndex_counter(self, citations: List[int]) -> int:
        n = len(citations); tot = 0
        counter = [0] * (n+1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0
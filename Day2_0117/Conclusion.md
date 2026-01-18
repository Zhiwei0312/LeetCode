1. majorityElement:
   1. sort后中心点一定是majorityElement
   2. Boyer-Moore: 两两对消，majority数〉其他所有频次相加
   3. Hash Table: dictionary
2. rotate:
   1. backup array
   2. 3 reverse
   3. cycle pop
3. maxProfit:
   1. griddy search O(n2)
   2. find the min price before day i, update min price, update max profit
4. maxProfit multiple purchase:
   1. griddy search with all upward lope
   2. dynamic programming: transition state clarification and calculate current status based only on the previous status
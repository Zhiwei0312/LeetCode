1. canJump:
   1. maximum covered steps >= length?
2. Jump:
   1. 把每一次跳跃看成“一层覆盖范围”
   2. 在当前跳跃范围内，尽量把下一跳能覆盖的最远位置推到最大
   3. 当扫描到当前范围的边界时，必须跳一次
3. hIndex:
   1. sort
   2. O(n): 用类似hash table的list记录每一个citation的数目，citation大于等于N的记作N
   3. 回看记录的list sum up来找到h因子
4. randomizedSet:
   1. list: insert O(1), getRandom O(1), remove - x
   2. Hash table: insert O(1), remove O(1), getRandom - x
   3. combine List with Hash table
   4. 数据结构
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False;
        else:
            self.hash[val] = len(self.list)
            self.list.append(val)
            return True;

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        
        index = self.hash[val]
        self.list[index] = self.list[-1]
        self.hash[self.list[-1]] = index
        
        self.list.pop()
        del self.hash[val]

        return True
    
    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
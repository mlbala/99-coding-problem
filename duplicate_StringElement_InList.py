class Solution(object):
    def isDuplicate(self, mylist):
        mylist = ["python","pandas","numpy","pandas"] # the original input list with repeated elements.
        dup = {x for x in mylist if mylist.count(x) > 1}
        dup = list(dup)
        mylist = set(mylist)
        for i in mylist:
            if i in dup:
                print(f"{i} is a duplicate")
            else:
                print(f"{i} is not a duplicate")
        
print(Solution().isDuplicate(["python","pandas","numpy","pandas"]))
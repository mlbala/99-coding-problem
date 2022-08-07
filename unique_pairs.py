# Input String => ["U1,U2","U3,U4","U2,U1","U1,U5","U4,U3"]
# Output String => ["U1,U2","U1,U5","U3,U4"]











class Solution(object):
    def uniique_array_pair(self, mylist):
        print(mylist)
        unique_list = []
        for i in mylist:
            unique_list.append(i.split(','))
        unique_list=list(set(tuple(sorted(i)) for i in unique_list))
        return unique_list
    
print(Solution().uniique_array_pair(["U1,U2","U3,U4","U2,U1","U1,U5","U4,U3"]))
# [('U1', 'U5'), ('U1', 'U2'), ('U3', 'U4')]

class Solution(object):
    def solution_function(self, mystring1, mystring2):
        
        output1 = [i for i in input1 if i not in input2]
        output2 = [i for i in input2 if i not in input1]
        
        #return ''.join(output1), ''.join(output2)
        print(f"output 1 : {''.join(output1)}")
        print(f"output 2 : {''.join(output2)}")

input1 = input("Snter string 1 :: ") #ABC
input2 = input("Snter string 2 :: ") #BC

print(Solution().solution_function(input1, input2))
# o/p-1 :: A, o/p-2 :: null

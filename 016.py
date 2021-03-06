# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list = [[1],[1,1]]
        if numRows > 2:
            for z in range(numRows - 2):
                list.append([1])
                for i in range(z+1):
                    list[z+2].append(list[z+1][i] + list[z+1][i+1])
                list[z+2].append(1)
                i -= 1
            return list
        if numRows == 2:
            return [[1],[1,1]]
        elif numRows == 1:
            return [[1]]
        elif numRows == 0:
            return []
        else:
            return [[1]]
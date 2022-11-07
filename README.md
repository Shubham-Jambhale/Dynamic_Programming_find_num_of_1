# Dynamic_programming_find_num_of_1

# Question
Given an integer n(1 <= n <= 105), find the minimum number of 1’s required to obtain n if
you are allowed to hit the following three functions in any order any number of times . Desired
time Complexity (O(n^2)), desired space complexity (O(n)).

i. def function1(a,b):
      return a+b
      
ii. def function2(a,b):
      return a*b

iii.def function3(a,b):
      return int(str(a)+str(b))
      
# Example 1: 
Input:22

Output:4

Explanation: On function3(1,1) we obtain 11(say a).
On function1(1,1) we obtain 2(say b).
Now we can hit function2(a,b) to obtain 22 which is the desired value.
Here the number of 1’s used are 4

# Example 2:
Input: 9

Output: 6

Explanation: function2(function1(function1(1,1),1),function1(1,function1(1,1)))

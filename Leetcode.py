        #1 problem --  "Two Pointers" or "String Manipulation"      date: 03-02-2026

'''
Why this works well:
    Time Complexity: $O(n + m)$, where $n$ and $m$ are the lengths of the two strings.
    We visit every character exactly once.
    Space Complexity: $O(n + m)$ to store the final merged string.
    Efficiency: Using a list (result) and then joining it at the end is more efficient in Python
    than repeated string concatenation, which creates a new string object every time.
'''

class Solution(object):

    def mergeAlternately(self, word1, word2):
        result = []
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i < len(word1):
                result.append(word1[i])

            if i < len(word2):
                result.append(word2[i])

        return"".join(result)

sol = Solution()
##print(sol.mergeAlternately("abcd", "xyz"))
##print(sol.mergeAlternately("Mne  uf", "okyDLfy"))
'''
word1="Mne  uf"
word2="okyDLfy"
max_len = max(len(word1), len(word2))
print(max_len)
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #2 problem -- "Merge Strings"                                date: 04-02-2026

'''
Why this works:
 Time Complexity: $O(n)$, where $n$ is the length of the string. We look at each character once.
 Space Complexity: $O(1)$, because we only store two integer sums regardless of how long the strings are.
 ord() and chr(): ord() converts a character to its number (e.g., 'a' -> 97), and chr() converts it back.

'''

class solution(object):
    def findTheDifference(self, s, t):

        sum_s=0
        sum_t=0

        for char in s:
            sum_s += ord(char)

        for char in t:
            sum_t += ord(char)

        return chr(sum_t - sum_s)   # for here logic is t-s
    
sol = solution()
##print(sol.findTheDifference("abc", "abcd")) # have to range t>s

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  #3 problem -- Substring Search                                date: 05-02-2026

'''

The Logic (Sliding Window)
Calculate the length of the needle (let's call it n) and haystack (let's call it h).

1.Loop through the haystack from index 0 up to h - n.

2. At each step i, check if the "slice" haystack[i : i+n] is equal to needle.

3. If yes, return i.

4. If the loop finishes without finding it, return -1.

'''

class solution(object):
    def strStr(self, haystack, needle):
        
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # if needle is longer than haystack, it can't fit

        if len(needle) > len(haystack):
            return -1

        # we only need to check up to the point where
        # the needle can fit into the haystack

        for i in range(len(haystack) - len(needle) + 1):

            #check the slice of haystack against the needle
            if haystack[i : i+ len(needle)] == needle:
                return i
            
        return -1
           

sol = solution()
##print(sol.strStr("sadbutsad", "sad"))
##print(sol.strStr("leetcode", "leeto"))
##print(sol.strStr("sad", "sadd"))
'''                       
           
h="sadbutsad"
n="sad"
for i in range(len(h) - len(n) + 1):   # means in list last value not be print so +1 needed
    
    print(h[i : i+ len(n)])  # for here to print full sad     if not op will sa
'''       
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



  #4 problem --  Valid Anagram                              date: 06-02-2026
'''This is the preferred solution for interviews. We count the frequency of every character.
  If s has three 'a's, t must also have three 'a's.
  Time Complexity: $O(N)$ (faster than sorting).
  Space Complexity: $O(1)$ (since there are only 26 lowercase letters).
'''

class solution(object):
    def isAnagaram(self, s, t):

        if len(t) != len(s):
            return False
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        return count_t == count_s
sol = solution()
##print(sol.isAnagaram("anagram", "nagaram"))
##print(sol.isAnagaram("cat", "tar"))


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


       #5 problem --   Repeated Substring pattern                            date: 07-02-2026
'''
The "Clever" Approach (String Math)If a string s is made of a repeating pattern (like "abab"), then s is essentially P + P.
  If we create a new string by adding s to itself (s + s), we get P + P + P + P.
  If we remove the very first and very last characters of this new doubled string,
  the original s (P + P) should still be visible somewhere in the middle.If s is not a pattern (like "aba"), this trick won't work.
    Time Complexity: $O(N)$ (very fast).
    Space Complexity: $O(N)$ (to store the doubled string).
'''
class solution(object):
    def repeatedSubstringPattern(self, s):
        doubled = s+s
        trimmed = doubled[1:-1]
        return s in trimmed
        
##print(solution().repeatedSubstringPattern("abab"))

##s="abab"        
##doubled = s+s
##trimmed = doubled[1:-1]
##print(doubled)
##print(trimmed)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

       #6 problem --   Move Zeroes                             date: 08-02-2026
'''
This is a classic "Two Pointer" problem. The requirement to do this in-place (without creating a new array) is the tricky part.

We use two pointers, let's call them L (Left) and R (Right).

L keeps track of where the next non-zero number should go.

R scans through the array looking for non-zero numbers.

The Algorithm
Initialize L = 0.

Iterate through the array with R from 0 to the end.

If nums[R] is not zero:

Swap nums[L] and nums[R].

Move L forward (L += 1).

If nums[R] is zero, just do nothing and let R move forward.

By the end, all non-zero numbers are pushed to the left (maintained in order), and all zeros are naturally pushed to the right.


'''

class solution(object):
    def moveZeroes(self, nums):
        
        L = 0
        for R in range(len(nums)):
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
      # return nums          #for seeing op in op but not needed this question
sol = solution()    
##print(sol.moveZeroes([0,1,0,3,12]))        
 


    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

       #7 problem --    Plus One                            date: 09-02-2026
'''
This problem is all about handling the "Carry" operation in math.

Think about how you do addition on paper:

You start from the last digit (the right side).

If the digit is 0-8, you just add 1 and stop.

If the digit is 9, it becomes 0, and you carry the 1 to the next left digit.

If you run out of digits (like 99 becoming 100), you add a 1 at the front.

'''

                                        # addtion but the core rules and op == [1,0,0]
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i]=0
        return [1] + digits
sol=Solution()
##print(sol.plusOne([9,9]))


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

       #8 problem --  sighn of the product of an array                  date: 10-02-2026
   
'''
This problem has a trap! You might be tempted to actually multiply all the numbers together, but if the array is large, the product becomes huge and can cause overflow errors (or just be very slow).

Instead, we just need to track the sign.

The Logic (No Math Required)
Check for Zero: If we see a 0, the entire product becomes 0. We can stop and return 0 immediately.

Count Negatives:

If there is an even number of negatives (e.g., -2 * -3 = 6), the result is Positive (1).

If there is an odd number of negatives (e.g., -2 * -3 * -4 = -24), the result is Negative (-1).
'''

class Solution():
    def arraySign(self,nums:List[int]) -> int:
        sign = 1
        for i in nums:
            if i==0:
                return 0
            if i<0:
                sign = -sign
        return sign

##print(Solution().arraySign([-1,-1,-1,-1]))
##print(Solution().arraySign([-1,-1,-1]))
##print(Solution().arraySign([-1,-2,0,1,2,3,4]))





#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


      #9 problem --   Can Make Arithmetic Progression From Sequence                              date: 11-02-2026

class Solution():
    def canMakeAP(self,arr: List[int]) -> bool:
        
          #1. sorting array
        
        arr.sort()

           # 2. get the difference between array 1st element and 0th element

        diff = arr[1] - arr[0]
            # 3. do the same to rest and compare to diff 
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True

##print(Solution().canMakeAP([1,3,5,7]))
##print(Solution().canMakeAP([1,3,5,8]))
##print(Solution().canMakeAP([0,5,10,15]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #10 problem --  Monotonic array                              date: 12-02-2026

class Solution():
    def isMonotonic(self,nums:List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                increasing = False
            if nums[i] > nums[i-1]:
                decreasing = False
        return increasing or decreasing

##print(Solution().isMonotonic([1,2,3]))
##print(Solution().isMonotonic([6,5,4,4]))
##print(Solution().isMonotonic([1,3,2]))


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


      #11 problem --  Roman to Integer                              date: 13-02-2026

class Solution():
    def romanToInt(self,s :str) -> int:
        
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C":100, "D" : 500, "M" : 1000}

        Total=0

        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                Total -= roman[s[i]]
            else:
                Total += roman[s[i]]
        return Total
    
##print(Solution().romanToInt("IV"))
##
##print(Solution().romanToInt("MM"))

    


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #12 problem --   Length of Last Word                             date: 14-02-2026

class Solution():
    def lengthOfLastWord(self,s:str) -> int:
        count=0
        for i in range(len(s)-1,-1,-1):     # len(s)-1 means [] index starts at 0,1,2,3 so len(s) means out of range 
            if s[i] == " ":
                if count > 0:
                    return count
            
            else:
                count+=1
                
        return count

##print(Solution().lengthOfLastWord("luffy is sill joyboy"))
##print(Solution().lengthOfLastWord("joyboy"))

# Another Method:

'''            
class Solution():
    def lengthOfLastWor(self,s:str) -> int:
        return len(s.strip().split()[-1])
print(Solution().lengthOfLastWor("luffy is sill joyboy"))
'''
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         # sunday Holiday but Monday did two                date: 15-02-2026


 #13 problem --   To Lower case                            date: 16-02-2026

class Solution:
    def toLowerCase(self, s: str) -> str:
        l = s.lower()
        return l

##print(Solution().toLowerCase("Luffy"))

    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #14 problem --    Base Ball Game                          date: 16-02-2026

class Solution():
    def callPoints(self, operations : List[str]) -> int:
        record = []

        for op in operations:

            if op == "+":
                new_score = record[-1] + record[-2]
                record.append(new_score)

            elif op == "D":
                new_score = record[-1] * 2
                record.append(new_score)

            elif op == "C":
                record.pop()

            else:
                record.append(int(op))
        return sum(record)

##print(Solution().callPoints(["5", "2","C","D","+"]))



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #15 problem --   Robot retur to origin                             date: 17-02-2026

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0

        for i in moves:
            if i == "R":
                x+=1
            elif i == "L":
                x-=1
            elif i == "U":
                y+=1
            elif i == "D":
                y-=1
        return x == 0 and y ==0
            
##print(Solution().judgeCircle("R,L,U,D"))
##print(Solution().judgeCircle("R,L")) 
##print(Solution().judgeCircle("R,U,D"))  
##print(Solution().judgeCircle("R,L,U"))       
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #16 problem --     Find Winner on a Tic Tac Toe Game                           date: 18-02-2026

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows=[0]*3
        cols=[0]*3
        daig1=0
        daig2=0

        for i, (r,c) in enumerate(moves):
            val =1 if i%2 == 0 else -1

            rows[r] += val
            cols[c] += val

            if r==c:
                daig1 += val
            if r+c == 2:
                daig2 += val
                
        if abs(rows[r])==3 or abs(cols[c])==3 or abs(daig1)==3 or abs(daig2)==3:
                return "A" if val == 1 else "B"

        if len(moves) == 9:
            return "Draw"
    
        return "Pending"

##print(Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
            

    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #17 problem --   Robot bound in circle                             date: 19-02-2026

class Solution():
    def isRobotBounded(self, instructions : str) -> bool:

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        x=0
        y=0

        facing = 0

        for move in instructions:
            if move == 'L':
                facing = (facing - 1)%4
            elif move == 'R':
                facing = (facing + 1)%4
            elif move == 'G':
                x += directions[facing][0]
                y += directions[facing][1]
        return (x == 0 and y == 0) or facing !=0
        
##print(Solution().isRobotBounded("GGLLGG"))
##print(Solution().isRobotBounded("GG"))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #18 problem -- Richest Customer Wealth                               date: 20-02-2026

class Solution():
    def maxWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            current_wealth = sum(i)
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return max_wealth

##print(Solution().maxWealth([[1,2,3],[3,2,1]]))

    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #19 problem --    saturday i am leave   and forgot                        date: 21-02-2026

               #  Matrix Diagonal Sum
                               
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]
            if i != n-1-i:
                total += mat[i][n-1-i]
        return total

##print(Solution().diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
##print(Solution().diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #20 problem --                      sunday hoiday but did it monday                            date: 22-02-2026

 ### Spiral Matrix  

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        # 1. Define the 4 boundaries
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        # 2. Keep going as long as the boundaries haven't crossed
        while left <= right and top <= bottom:
            
            
            # Step A: Go Left to Right along the Top row
            for i in range (left,right+1):
                result.append(matrix[top][i])
            top += 1  # The top row is done, shrink boundary down
            
            # Step B: Go Top to Bottom along the Right column
            for i in range(top,bottom+1):
                refult.append(mtrix[i][right])
            right -= 1 # The right col is done, shrink boundary left
            
            # THE TRAP: For non-square matrices, we might have already crossed boundaries.
            # We must check if we still have a valid row and column before going backwards.
            if left > right or top > bottom:
                break
                
            # Step C: Go Right to Left along the Bottom row
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom -= 1 # The bottom row is done, shrink boundary up
            
            # Step D: Go Bottom to Top along the Left column
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left += 1  # The left col is done, shrink boundary right
            
        return result        


    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #21 problem --       Set Matrix Zeroes                         date: 23-02-2026

'''    Imagine this matrix:
[1, 1, 1]                                               op:      [1, 0, 1]          
[1, 0, 1]                                                           [0, 0, 0]
[1, 1, 1]                                                           [1, 0, 1]
 '''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False # Tracks if the first row needs to be zeroed
        
        # STEP 1: Determine which rows/cols need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0]
                    else:
                        rowZero = True   # Special flag for the first row
                        
        # STEP 2: Zero out the matrix based on our marks in the first row/col
        # We start at index 1 so we don't overwrite our flags yet!
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] == 0
                    
        # STEP 3: Handle the first column
        # If the top-left is 0, the whole first column must be 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # STEP 4: Handle the first row
        # If our special variable is True, the whole first row must be 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
#----------------------

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowZero = False

        for r in range (rows):
            for c in range (cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        rowZero = True
        for r in range (1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c]=0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0]=0

        if rowZero:
            for c in range(cols):
                matrix[0][c]=0
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #22 problem --    Count Odd Numbers in an Interval Range        date: 24-02-2026

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd= (high - low) //2

        if low % 2 != 0 or high % 2 !=0:
            odd +=1
        return odd


##odd= (9 - 8) //2
##print(odd)





    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #23 problem --     Average Salary Excluding the Minimum and Maximum Salary                           date: 25-02-2026

class Solution:
    def average(self, salary: List[int]) -> float:
        s=0
        salary.sort()
        salary.pop(0)
        salary.pop(len(salary)-1)
        for i in salary:
            s+=i
        return s/len(salary)
##print(Solution().average([20,10,30,40]))
    
####   for large datasets respect to the time complexity
'''
class Solution:
    def average(self, salary: List[int]) -> float:
        # 1. Get the sum of the middle elements
        total_sum = sum(salary) - min(salary) - max(salary)
        
        # 2. Get the count of the middle elements
        count = len(salary) - 2
        
        # 3. Return the average (Total / Count)
        return total_sum / count
'''    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







 #24 problem --                                date: 26-02-2026




    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




 #25 problem --                                date: 27-02-2026




    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 #26 problem --                                date: 28-02-2026




    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



 #27 problem --                                date: 01-03-2026




    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



 #28 problem --                                date: 02-03-2026




    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 #29 problem --                                date: 03-03-2026




    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 #30 problem --                                date: 04-03-2026




    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





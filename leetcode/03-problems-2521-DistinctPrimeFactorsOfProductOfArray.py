from collections import deque
import math

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def is_prime(n):
            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    return False
            return True


        def decompose_prime_factors(n):
            if n <= 1:
                raise Exception("unreachable.")
            if n == 2:
                return {2}

            if is_prime(n):
                return {n}
            else:
                result = set()
                for i in range(2, math.isqrt(n) + 1):
                    if n % i == 0:
                        result.update(decompose_prime_factors(i))
                        result.update(decompose_prime_factors(n // i))
                return result

        
        # nums.sort()
        q = deque()
        q.extend(nums)
        result = set()
        while q:
            n = q.popleft()
            if n <= 1:
                continue

            if is_prime(n):
                for j in range(len(q)):
                    while q[j] % n == 0:
                        q[j] //= n
                
                # q 길이가 for loop 도중에 바뀌면 안 되니까 for loop를 마치고 원소 값이 1인 것들을 한 번에 제거한다.
                new_q = deque()
                new_q.extend([e for e in list(q) if e != 1])
                q = new_q
                result.add(n)
            else:
                prime_factors = decompose_prime_factors(n)
                # print("prime_factors: ", prime_factors)
                for p in prime_factors:
                    for j in range(len(q)):
                        while q[j] % p == 0:
                            q[j] //= p

                    # q 길이가 for loop 도중에 바뀌면 안 되니까 for loop를 마치고 원소 값이 1인 것들을 한 번에 제거한다.
                    new_q = deque()
                    new_q.extend([e for e in list(q) if e != 1])
                    q = new_q
                    result.add(p)

        return len(result)
    
    
"""

Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

    A number greater than 1 is called prime if it is divisible by only 1 and itself.
    An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.

 

Example 1:

Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.

Example 2:

Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.

 

Constraints:

    1 <= nums.length <= 104
    2 <= nums[i] <= 1000





"""
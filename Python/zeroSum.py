"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000
"""
import random

def sumZero(n):
    """
    This is my solution.
    :type n: int
    :rtype: List[int]
    """
    return_list = []
    random_number = random.randint(-n, 1)

    if n == 1:
        return_list.append(0)

    elif n == 2 or n == 3:
        for num in range(n):
            if n == 2:
                if num == 0:
                    return_list.append(random_number)
                else:
                    return_list.append(random_number * -1)
            if n == 3:
                if num == 0:
                    return_list.append(random_number)
                elif num == 1:
                    return_list.append(0)
                else:
                    return_list.append(random_number * -1)

    # If n is greater than 3...
    else:
        for num in range(n):
            if num == 0:
                return_list.append(random_number)
            elif n > 0 and num < n - 1:
                if num % 2 == 0:
                    return_list.append(random.randint(-n, 1))
                else:
                    return_list.append(random.randint(1, n))
            else:
                return_list.append(sum(return_list) * -1)


    return return_list

            
def sumZeroAccepted(n):
    """
    This is the accepted solution.
    :type n: int
    :rtype: List[int]
    """
    return_list = []
    for num in range(1, n // 2 + 1):
        return_list.append(num)
        return_list.append(-num)

    if n % 2 == 1:
        return_list.append(0)

    return return_list


num = 73
output = sumZero(num)
accepted_output = sumZeroAccepted(num)
print(f'The list is: {output}')
print(f'Sum is {sum(output)}')
print(f'The list is: {accepted_output}')
print(f'Sum is {sum(accepted_output)}')
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 
Test: "))", "){", "()

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s):
    stack = []
    dict = {
        "]" : "[",
        "}" : "{",
        ")" : "(",
    }
    for char in s:  
        if char in dict.values(): 
            stack.append(char)
        elif char in dict.keys(): 
            if stack == [] or dict[char] != stack.pop():
                return False
    return stack == []

def main():
    tcase = {
        "()": True,
        "()[]{}": True,
        "(]": False,
        "()))": False,
        "){": False
    }
    for k,v in tcase.items():
        print("Test:",k,"\tExpected: ",v, "\tGot:", isValid(k))

if __name__=="__main__":
    main()
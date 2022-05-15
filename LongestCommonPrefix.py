"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

def longestCommonPrefix(strs):
    sub_str = strs[0]

    for i in range(1, len(strs)):
        # print("i:", i, "sub:", sub_str, "actual:",strs[i], "lensub:",len(sub_str), "mod:", strs[i][0:len(sub_str)])
        while(strs[i][0:len(sub_str)] != sub_str):
            sub_str = sub_str[0:len(sub_str)-1]
            if (len(sub_str)==0):
                return ""
    return sub_str

def main():
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))

if __name__=="__main__":
    main()
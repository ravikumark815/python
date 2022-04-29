def twoSum(nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i==j:
                    continue
                elif ((nums[i] + nums[j]) == target):
                    result.append(i)
                    result.append(j)
                    return result

def main():
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))

if __name__=="__main__":
    main()
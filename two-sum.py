def main():
    nums = [3, 2, 4]
    target = 6
    for i in range(len(nums)):
        for j in range(i + 1):
            if (nums[i] + nums[j]) == target:
                if i != j:
                    print(j, i)


if __name__ == "__main__":
    main()

# OPTIMIZE: Algorithm that is less than O(n^2) time complexity

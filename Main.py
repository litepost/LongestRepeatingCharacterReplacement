def character_replacement(s: str, k: int) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    letter_count = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        letter_count[s[right]] = letter_count.get(s[right], 0) + 1

        while right - left + 1 - max(letter_count.values()) > k:
            letter_count[s[left]] -= 1
            left += 1

        print(f"right - left = {right - left}")
        print(letter_count)
        max_len = max(max_len, right - left + 1)
        print(f"max_len = {max_len}")

    return max_len

        # while right < len(s) and right - left - letter_count.get(char, 0) <= k:



    # i = 0
    # max_len = 1
    # while i < len(s):
    #     k_count = 0
    #     k1_index = i
    #     j = i + 1
    #     while k_count < k + 1 and j < len(s):
    #         if s[i] != s[j]:
    #             k_count += 1
    #             if k_count == 1:
    #                 k1_index = j
    #         j += 1
    #
    #     if j == len(s) and k_count < k + 1:
    #         max_len = max(max_len, j - i)
    #     else:
    #         max_len = max(max_len, (j-1) - i)
    #
    #     i = max(i+1, k1_index)
    #
    # return max_len


# input_str = "ABAB"
# k = 2
# input_str = "AABABBA"
# k = 1
# input_str = "AAAAA"
# k = 2
# input_str = "BBBB"
# k = 0
input_str = "AABBBBBB"
k = 0
# input_str = "ABBB"
# k = 1
print(f"input_str: \"{input_str}\"")
print(f"k: {k}")

ans = character_replacement(s=input_str, k=k)

print("-----------")
print(f"The answer is {ans}")

def largest_odd_substring(s: str) -> str:
    """
    Given a string s representing a large integer, return the largest-valued odd integer
    (as a string) that is a substring of s.
    """
    largest_odd = ""
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            # Check if the substring is odd and does not have leading zeros
            if int(substring[-1]) % 2 == 1 and (substring[0] != '0' or len(substring) == 1):
                if largest_odd == "" or int(substring) > int(largest_odd):
                    largest_odd = substring

    print(largest_odd)


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)

        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # 2. Read optional sign
        sign = 1
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. Read digits manually
        result = 0
        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")

            # 4. Clamp before result * 10 + digit goes out of range
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result

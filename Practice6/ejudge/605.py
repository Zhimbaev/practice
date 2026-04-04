s = input().lower()
vowels = "aeiou"

x = any(ch in vowels for ch in s)
print("Yes" if x else"No" )
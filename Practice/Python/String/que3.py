'Count how many vowels are present in a string.'

s = "programing"
vowels = "aeiouAEIOU"
count = 0

for i in s:
    if i in vowels:
        count += 1

print("Vowel count : ",count)
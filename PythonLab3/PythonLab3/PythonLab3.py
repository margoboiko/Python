import string

d = {}
text = input().split()

for word in text:
    if word in d:
       d[word] += 1
    else:
        d[word] = 1
         
max_count = max(d.values())
most_frequent = [k for k, v in d.items() if v == max_count]
print(min(most_frequent))

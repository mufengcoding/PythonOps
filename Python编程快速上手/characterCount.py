# count character
import pprint

message = "china is no 1"
count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] += 1

print(count)
pprint.pprint(count)
print(pprint.pformat(count))

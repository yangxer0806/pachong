import re

li = re.findall(r"\d+", "今天是20230317")
print(li)

it = re.finditer(r"\d+", "今天是20230317")
for i in it:
    print(i)
    print(i.group())

s = re.search(r"\d+", "今天是20230317")
print(s.group())

st = re.match(r"\d+", "120230317")
print(st.group())


# 预加载正则
obj = re.compile(r"\d+")
re = obj.finditer("今天是220230317")
for i1 in re:
    print(i1.group())

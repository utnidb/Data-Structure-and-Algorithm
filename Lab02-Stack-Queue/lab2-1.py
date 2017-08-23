from stack import Stack

s = Stack()

name = input()
for i in name:
    s.push(i)
    print("push : ", i)
    print(s.items)

print()
print("items : ", s.items)
print("size : ", s.size())
print("empty : ", s.empty())
print("full : ", s.full())
print("top : ",s.peek())
print()

while not s.empty():
    print("pop : ", s.pop())
    print(s.items)

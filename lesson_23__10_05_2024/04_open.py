# writing

f = open("example.txt", "w", encoding="utf-8")
print(type(f))
f.write("1 hello world\n2 hello world\n3 hello world\n")
print("success!")
f.close()


# reading readline
f = open("example.txt", "r", encoding="utf-8")
print(f.readline(10))
f.close()

# reading readlines
f = open("example.txt", "r", encoding="utf-8")
print(f.readlines())
f.close()

# reading read
print("=========== reading read ==============")
f = open("example.txt", "r", encoding="utf-8")
print(f.read())
f.close()


# context manager
print("=========== reading read ==============")
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.read())

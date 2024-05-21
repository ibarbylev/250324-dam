"""  tuple create  """

lst: list = [1, 2, 3]

t = tuple(lst)
print(type(t))  # <class 'tuple'>
print(t)   # (1, 2, 3)


""" ============ How to crate tuple? ============ """
t = tuple()
print(type(t))  # <class 'tuple'>
print(t)   # ()

t = tuple("Hello world!")
print(type(t))  # <class 'tuple'>
print(t)   # ('H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!')


t = (5)
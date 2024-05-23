from collections import deque

queue = deque()
print(queue)
queue.append(1)
print(queue)
queue.append(2)
print(queue)
first_element = queue.popleft()  # Извлечение первого элемента из очереди (первого слева)
print(first_element)  # 1
print(queue)


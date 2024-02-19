# Lista de alta performance.

from collections import deque

# criando deque
deq = deque('geek')

print(deq)

# Adicionando elementos no deque
deq.append('y') # Adiciona no final
print(deq)

deq.appendleft('k')
print(deq)

#remover elementos
print(deq.pop()) # Remove e retorna o último elemento

print(deq)

print(deq.popleft())

print(deq)

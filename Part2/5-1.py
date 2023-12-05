#기본라이브러리에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다
# append - 가장 뒤쪽에 데이터 삽입. pop - 가장 뒤쪽에서 데이터 꺼냄

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력
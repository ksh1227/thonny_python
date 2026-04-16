class Node:
    def __init__(self):
        self.data = None
        self.link = None

# 노드 연결하기
node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5


# 새 노드 삽입하기
newNode = Node()
newNode.data = "재남"
newNode.link = node2.link
node2.link = newNode

# 연결된 노드 삭제하기
node2.link = node3.link
del(node3)

# 노드 간편 출력 방법
current = node1
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')



# 클래스 함수 선언
class Node:
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


def makeSimpleLinkedList(nameEmail):
    global memory, head, current, pre
    printNodes(head)
    
    node = Node()
    node.data = nameEmail
    memory.append(node)
    if head == None:                      #첫번째 노드
        head = node
        return
    
    if head.data[1] > nameEmail[1]:     #첫번째 노드보다 작을때
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:         #중간 노드 삽입
        pre = current
        current = current.link
        if current.data[1] > nameEmail[1]:
            pre.link = node
            node.link = current
            return
    
    current.link = node                #삽입한 노드가 가장 클 경우


# 전역 변수 선언
memory = []
head, current, pre = None, None, None

# 메인 코드 부분
if __name__ == "__main__":
    
    while True:
        name = input("이름--> ")
        if name == "" or name == None:
            break
        nameEmail = input("이메일--> ")
        data = [name,nameEmail]
        makeSimpleLinkedList(data)
        printNodes(head)
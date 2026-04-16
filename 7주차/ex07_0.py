class Node:
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current is None: return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, inserData):
    global head
    
    if head.data == findData:           # 첫 번째 노드 삽입
        node = Node()
        node.data = inserData
        node.link = head
        last = head                     # 수정 포인트!
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    
    current = head
    while current.link != head:         # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = inserData
            node.link = current
            pre.link = node
            return
            
    node = Node()                       # 마지막 노드 삽입
    node.data = inserData
    current.link = node
    node.link = head

def deleteNode(deleteData):
    global head
    
    if head.data == deleteData:         # 첫 번째 노드 삭제
        current = head
        head = head.link
        last = current                  # 수정 포인트! (삭제될 노드부터 시작해 꼬리 찾기)
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return
    
    current = head
    while current.link != head:         # 중간/마지막 노드 삭제
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global head
    current = head
    if current.data == findData: return current
    while current.link != head:
        current = current.link
        if current.data == findData: return current
    return Node()

# --- 실행 부분 ---
memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0] 
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
        
    printNodes(head)
    
    insertNode('다현','화사')
    insertNode('사나','솔라')
    insertNode('재남','문별')
    printNodes(head)
    
    deleteNode("화사")
    deleteNode("문별")
    printNodes(head)

    print(findNode("다현").data)
    print(findNode("솔라").data)
    print(findNode("지효").data)
    print(findNode("재남").data) # 찾는 데이터가 없으면 None 출력
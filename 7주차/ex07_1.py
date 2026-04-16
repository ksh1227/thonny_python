# 클래스 함수 선언 #
class Node:
    def __init__(self):
        self.data = None
        self.link = None
        
def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()
  
    
#노드 삽입#
def insertNode(findData,inserData):
    global memory, head, current, pre
    
    if head.data == findData:           #첫번째 노드 삽입
        node = Node()
        node.data = inserData
        node.link = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    
    current = head
    while current.link != head:         #중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = inserData
            node.link = current
            pre.link = node
            return
        
    node = Node()                   #마지막 노드 삽입
    node.data = inserData
    current.link = node
    node.link = head
    
    
#노드 삭제#
def deleteNode(deleteData):
    global memory, head, current, pre       
    
    if head.data == deleteData:         #첫번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return
    
    
    current = head                      #첫번째 외 노드 삭제
    while current.link != head:      
        pre = current
        current = current.link
        if current.data == deleteData:  #중간 노드를 찾았을때
            pre.link = current.link
            del(current)
            return
        
#노드 찾기#
def findNode(findData):
    global memory, head, current, pre
    
    current = head
    if current.data == findData:        #노드 리턴
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            return current
    return Node()                   #빈 노드 반환
    
    
# 전역 변수 선언 #
memory = []
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효']
        
        
# 메인 코드 부분 #
if __name__ == "__main__":
    
    node = Node()              # 첫번째 노드
    node.data = dataArray[0] 
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]: # 두번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
        
    printNodes(head)
        
    ##
    insertNode('다현','화사')       #노드 삽입
    printNodes(head)
    
    insertNode('사나','솔라')
    printNodes(head)
    
    insertNode('재남','문별')
    printNodes(head)
        
    ## 
    deleteNode("화사")
    printNodes(head)
    
    deleteNode("문별")
    printNodes(head)

    ##
    fNode = findNode("다현")      #노드 찾기
    print(fNode.data)
    
    fNode = findNode("솔라")
    print(fNode.data)
    
    fNode = findNode("지효")
    print(fNode.data)
    
    fNode = findNode("재남")
    print(fNode.data)
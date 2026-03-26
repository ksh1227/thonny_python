mylist = [30,10,20]
print("현재리스트 : %s" % mylist)

mylist.append(40)
print("append(40) 후의 리스트 : %s" % mylist)

print("pop()으로 추출한 값 : %s" % mylist.pop())
print("pop()으로 후의 리스트 : %s" % mylist)

mylist.sort()
print("sort() 후의 리스트 : %s" %mylist)

mylist.reverse()
print("reverse() 후의 리스트 : %s" %mylist)

print("20 값의 위치 : %d" %mylist.index(20))

mylist.insert(2, 222)
print("insert(2,222) 후의 리스트 : %s" %mylist)
mylist.remove(222)
print("remove(222) 후의 리스트 : %s" %mylist)

mylist.extend([77,88,77])
print("extend([77,88,77]) 후의 리스트 : %s" %mylist)

print("77 값의 개수 : %d" %mylist.count(77))
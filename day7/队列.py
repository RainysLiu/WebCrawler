from queue import Queue

#创建一个队列对象
q= Queue(5)

#向队列中添加元素
q.put('嘻嘻')
q.put('哈哈')
q.put('渣渣')
q.put('娜娜')
q.put('呜呜')

#阻塞，等待
# q.put('咪咪',False))
# q.put('鸡鸡',True,5)

#其他方法
print(q.full())
print(q.empty())
print(q.qsize())



print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

'''
print(q.get(False))  #立马抛出异常
print(q.get(True,5),)  #过五秒抛出异常

'''

print(q.full())
print(q.empty())
print(q.qsize())


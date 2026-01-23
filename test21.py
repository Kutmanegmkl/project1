# def get_numbers():
#     yield 1
#     yield 2
#     yield 3

# num=get_numbers()
# print(num)

# l=list(num)
# print(l)

# def test(*arggs):
#     for i in arggs:
#         if isinstance(i,int):
#             yield i**2
#         else:
#             yield i

# a=test('a','b',1,2,3,4,5,6,7,8,9,10,'c','d')
# print(list(a))


class Orders:
    def __init__(self, data):
        self.data=data
    def __iter__(self):
        return OrdersIterator(self.data)

class OrderIterator:
    def __init__(self,data):
        self.data=data
        self.index=0

    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        
        value=self.data[self.index]
        self.index+=1
        return value
    
orders=Orders([100,200,300,400])
    



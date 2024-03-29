class dice:
    def __init__(self,label):
        self.top, self.front, self.right, self.left, self.rear, self.bottom \
                = label
  
    def roll(self,odr):
        if   odr=='N': self.top, self.front, self.bottom, self.rear = \
                                self.front, self.bottom, self.rear , self.top
        elif odr=='E': self.top, self.left , self.bottom, self.right = \
                                self.left , self.bottom, self.right, self.top
        elif odr=='W': self.top, self.right, self.bottom, self.left = \
                                self.right, self.bottom, self.left , self.top
        elif odr=='S': self.top, self.rear , self.bottom, self.front = \
                                self.rear , self.bottom, self.front, self.top
  
    def print_top(self): print(self.top)
    def print_right(self): print(self.right)
  
    def get_label(self):
        return [self.top, self.front, self.right, self.left, self.rear, self.bottom]
 
    def compare(self, label):
        for odr in 'EEENEEENEEESEEESEEENEEEN':
            if self.get_label() == label:
                return True
            self.roll(odr)
        else:
            return False
   
if __name__=='__main__':
    n = int(input())
    L = []
    for i in range(n):
        label = list(map(int,input().split()))
        for d in L:
            if d.compare(label): break
        else:
            L.append(dice(label))
            continue
        print('No')
        break
    else:
        print('Yes')
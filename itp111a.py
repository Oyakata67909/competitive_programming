class dice:
    def __init__(self, lable):
        self.top, self.front, self.right, self.left, self.rear, self.bottom = label
    
    def roll(self, odr):
        if odr == 'N': self.top, self.front, self.bottom, self.rear = \
            self.front, self.bottom, self.rear, self.top
        elif odr == 'E': self.top, self.left, self.bottom, self.right = \
            self.left, self.bottom, self.right, self.top
        elif odr == 'W': self.top, self.right, self.bottom, self.left = \
            self.right, self.bottom, self.left, self.top
        elif odr == 'S': self.top, self.rear, self.bottom, self.front = \
            self.rear, self.bottom, self.front, self.top
    def print_top(self): print(self.top)
label = list(map(int, input().split()))
odr_list = list(input())
d = dice(label)
for odr in odr_list:
    d.roll(odr)
d.print_top()
        

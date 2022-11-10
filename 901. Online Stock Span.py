class StockSpanner:

    def __init__(self):
        self.items = []

    def next(self, price: int) -> int:
        count = 1

        while self.items and self.items[-1][0] <= price:
            count += self.items[-1][1]
            self.items.pop()
        self.items.append((price,count))
        # print(self.items)
        return count
        


inp1 = ["next", "next", "next", "next", "next", "next", "next"]
inp2 = [[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]

s1 = StockSpanner()
for i in inp2:
    print(s1.next(i))
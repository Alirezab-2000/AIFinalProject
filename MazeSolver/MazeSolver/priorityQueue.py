from MazeSolver.state import State


# [(node , pathCost , manhatanDistance) , (node , pathCost , manhatanDistance) , ...]
class PriorityQueue:
    items : list[State] = []

    def size(self):
        return len(self.items)
    
    def enqueue(self , item : State):
        c = item
        while c.stateFather:
            c = c.stateFather
            if c.node.column == item.node.column and c.node.row == item.node.row:
                return
        self.items.append(item)

    def multipleEnqueue(self ,items : list[State]):
        self.items.extend(items)

    def dequeue(self):
        if(len(self.items) == 0): return
        minF = self.items[0]

        for successor in self.items:
            if successor < minF:
                minF = successor
        self.items.remove(minF)
        return minF

# return heapq.heappop(self.items)
# heapq.heappush(self.items, item)
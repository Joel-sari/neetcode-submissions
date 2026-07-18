class ListNode: 
    def __init__(self, key, next=None):
        self.key = key 
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for node in range(1000)]

        

    def add(self, key: int) -> None:
        index_key = key % len(self.set)
        current_pointer = self.set[index_key]
        


        while current_pointer.next:
            if current_pointer.next.key == key: 
                return
            current_pointer = current_pointer.next 

        current_pointer.next = ListNode(key)


  

    def remove(self, key: int) -> None:
        index_key = key % len(self.set)
        current_node = self.set[index_key]

        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        return
        

    def contains(self, key: int) -> bool:
        index_key = key % len(self.set)
        current_node = self.set[index_key]

        while current_node.next:
            if current_node.next.key == key:
                return True 
            current_node = current_node.next 
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
      next = 'empty'

      if self.next is not None:
        next = self.next.key

      return f"Current: {self.key} : {self.value}\nNext: {next}\n"

    def print_list(self, index):
      current = self

      while current is not None:
        current = current.next

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        def hash(key):
            index = 0
            salt = 1701

            for char in key:
                 index += (salt << 13) + salt + ord( char )

            return index

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        
        node = LinkedPair(key, value)
        index = self._hash_mod(key)

        list_start = self.storage[index]
  
        if not list_start: 
          self.storage[index] = node

        else:
          current_node = list_start

          while current_node is not None:
            if current_node.key == key:
              current_node.value = value
              return
            
            if current_node.next is None:
              current_node.next = node
              node.prev = current_node
              return

            current_node = current_node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if node == None: 
          print( "Error_Code::404::Key Not Found" )
          return

        while node is not None:
          if node.key == key:
            temp = node.prev

            if node.prev is None and node.next is None:
              self.storage[index] = None
              return

            if node.prev is None and node.next is not None:
              node.next.prev = None
            elif node.prev is not None and node.next is None:
              node.prev.next = None
            else:
              node.prev.next = node.next
              node.next.prev = temp.prev
            return

          node = node.next

        print( "Error_Code::404::Key Not Found" )
        return  
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if node == None: return None
        
        while node is not None:
          if key == node.key:
            return node.value

          node = node.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for i in range( len( old_storage ) ):
          current_list_node = old_storage[i]

          while current_list_node is not None:
            self.insert(current_list_node.key, current_list_node.value)

            current_list_node = current_list_node.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

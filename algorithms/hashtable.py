class HashTable(object):
    data: list
    maxsize: int

    def __init__(self, maxsize: int = 10):
        # In the Java example it shows a LinkedList; I wonder if arrays are
        # the same thing and is good enough
        self.data = [[]] * maxsize
        self.maxsize = maxsize

    def put(self, key: str, value: str) -> bool:
        hashCode: int = self.__class__.getHashCode(key)
        index: int = self.getIndex(hashCode)
        # import pdb; pdb.set_trace()
        currentValues: list = self.data[index]
        currentValues.append((key, value))
        # This block takes care of preventing duplicates
        # We could use binary search if the list was sorted
        inserted: bool = False
        for _index, key_value in enumerate(currentValues):
            if (key_value[0] == key):
                currentValues[_index] = (key, value)
                inserted = True
                break
        if not inserted:
            currentValues.append((key, value))
        self.data[index] = currentValues
        return True

    def get(self, key: str) -> str:
        hashCode: int = self.__class__.getHashCode(key)
        index: int = self.getIndex(hashCode)
        currentValues: list = self.data[index]
        found = None
        for _index, key_value in enumerate(currentValues):
            if (key_value[0] == key):
                found = currentValues[_index]
                break

        if not found:
            raise ValueError('Key not found in hash table.')

        return found[1]

    @classmethod
    def getHashCode(cls, key: str) -> int:
        return hash(key)

    def getIndex(self, hashCode: int) -> int:
        return hashCode % self.maxsize - 1


if __name__ == "__main__":
    ht = HashTable()
    ht.put("foo", "Super")
    print(ht.get("foo"))
    ht.put("foo", "Duper")
    print(ht.get("foo"))

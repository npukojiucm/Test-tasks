class TreeStore:
    def __init__(self, items: list):
        self.items = items

    def getAll(self):
        return self.items

    def getItem(self, id_elem):
        try:
            assert id_elem > 0
            return self.items[id_elem - 1]
        except IndexError:
            return None
        except AssertionError:
            return None

    def getChildren(self, id_elem):
        result = []
        max_id = self.items[-1]['id']

        if id_elem == 1:
            return self.items[1:]
        elif id_elem == 2:
            result.append(self.getItem(4))
            id_elem = 4

        while True:
            id_elem *= 2

            if id_elem - max_id > 1:
                break
            elif id_elem - 1 == max_id:
                result.append(self.getItem(max_id))
                break
            else:
                result.append(self.getItem(id_elem - 1))
                result.append(self.getItem(id_elem))

        return result

    def getAllParents(self, id_elem):
        result = []
        while id_elem > 1:
            if id_elem == 3:
                result.append(self.items[0])
                break

            if id_elem % 2 == 1:
                id_elem += 1

            id_elem //= 2
            result.append(self.getItem(id_elem))

        return result


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

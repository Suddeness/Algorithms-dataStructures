
class Branch:
    def __init__(self,value, name, number):
        self.value = value
        self.left = None
        self.right = None
        self.name = name
        self.number = number

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value, number, name):
        new_branch = Branch(value, name, number)
        if self.root is None:
            self.root=new_branch
        else:
            self._insert_val(self.root, new_branch)

    def _insert_val(self, current, new):
        if current.value > new.value:
            if current.left is None:
                current.left = new
            else:
                self._insert_val(current.left, new)
        elif current.value < new.value:
            if current.right is None:
                current.right = new
            else:
                self._insert_val(current.right, new)

    def find(self, value):
        return self._search_val(self.root,value)

    def _search_val(self,current, new):
        if current is None:
            return None
        if current.value == new:
            return (current.name, current.number)
        elif current.value > new:
            return self._search_val(current.left, new)
        elif current.value < new:
            return self._search_val(current.right, new)

    def travel_by_direction(self, direction):
        result = []
        if direction.lower() == "left":
            self._travelLeft(self.root, result)
            print(result)
            return
        elif direction.lower() == "right":
            self._travelRight(self.root, result)
            print(result)
            return result
        return result

    def delete(self, value):
        self.root = self._delete_val(self.root, value)

    def _delete_val(self, current, value):
        if current is None:
            return None
        if value < current.value:
            current.left = self._delete_val(current.left, value)
        elif value > current.value:
            current.right = self._delete_val(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            min_larger_node = self._find_min(current.right)
            current.value = min_larger_node.value
            current.name = min_larger_node.name
            current.number = min_larger_node.number
            current.right = self._delete_val(current.right, min_larger_node.value)
        return current

    def _find_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def _travelLeft(self, root, res):
        if root is not None:
            res.append([root.name, root.number])
            self._travelLeft(root.left, res)

    def _travelRight(self, root, res):
        if root is not None:
            res.append([root.name, root.number])
            self._travelRight(root.right, res)

directory = Tree()

def Directory_add(number, name):
    value = hash(name.lower())
    directory.add(value, number, name)

def Directory_find(name):
    value = hash(name.lower())
    result = directory.find(value)
    if result:
        print(f"Found: Name={result[0]}, Number={result[1]}")
    else:
        print("Not found")

def Directory_delete(name):
    value = hash(name.lower())
    directory.delete(value)


Directory_add(73295295,"Name")
Directory_find("Name")
Directory_delete("name")
Directory_find("Name")

class Spine:
    def __init__(self, root):
        self.path = [root]

    def push(self, node):
        self.path.append(node)

    def first(self):
        if self.path:
            return self.path[0]

        raise Exception("Can't call first on empty Spine.")

    def peek(self):
        if self.path:
            return self.path[-1]

        raise Exception("Can't call peek on empty Spine.")

    def pop(self):
        if self.path:
            return self.path.pop()

        raise Exception("Can't call pop on empty Spine.")

    def __len__(self):
        return len(self.path)

    def __bool__(self):
        return len(self) > 0

    def search(self, value):
        if self:
            while 1:
                last = self.peek()

                if value < last.value:
                    if last.left:
                        self.push(last.left)
                    else:
                        break
                elif value > last.value:
                    if last.right:
                        self.push(last.right)
                    else:
                        break
                else:
                    return True

        return False

    def min_leaf(self):
        if self:
            while 1:
                last = self.peek()

                if last.left:
                    self.push(last.left)
                else:
                    break

            return True

        return False

    def max_leaf(self):
        if self:
            while 1:
                last = self.peek()

                if last.right:
                    self.push(last.right)
                else:
                    break

            return True

        return False

    def successor(self):
        if self:
            child = self.peek()

            if child.right:
                self.push(child.right)

                return self.min_leaf()

            self.pop()

            while self:
                parent = self.peek()

                if child is parent.right:
                    child = self.pop()
                else:
                    break

            return bool(self)

        return False

    def predecessor(self):
        if self:
            child = self.peek()

            if child.left:
                self.push(child.left)

                return self.max_leaf()

            self.pop()

            while self:
                parent = self.peek()

                if child is parent.left:
                    child = self.pop()
                else:
                    break

            return bool(self)

        return False

    def insert(self, node):
        if self:
            found = self.search(node.value)

            if found:
                return False

            parent = self.peek()

            if node.value < parent.value:
                parent.left = node
            else:
                parent.right = node

            self.push(node)
        else:
            self.push(node)

        return True

    def delete(self, value):
        found = self.search(value)

        if not found:
            return False, None

        node = self.peek()

        wipe = node

        if node.left and node.right:
            self.push(node.right)
            self.min_leaf()
            wipe = self.peek()
            node.value = wipe.value

        self.pop()

        new_child = wipe.left or wipe.right

        if self:
            parent = self.peek()

            if parent.left is wipe:
                parent.left = new_child
            else:
                parent.right = new_child

        return True, new_child

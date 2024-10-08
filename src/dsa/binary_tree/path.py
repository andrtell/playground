class Path:
    @classmethod
    def find(cls, root, value):
        if not root:
            raise Exception("Can't call find if root is None.")

        path = [root]

        while 1:
            cur = path[-1]

            if value < cur.value:
                if cur.left:
                    path.append(cur.left)
                else:
                    break
            elif value > cur.value:
                if cur.right:
                    path.append(cur.right)
                else:
                    break
            else:
                return True, path

        return False, path

    @classmethod
    def min_leaf(cls, root):
        if not root:
            raise Exception("Can't call min_leaf if root is None.")

        path = [root]

        while 1:
            cur = path[-1]
            if cur.left:
                path.append(cur.left)
            else:
                break

        return path

    @classmethod
    def max_leaf(cls, root):
        if not root:
            raise Exception("Can't call max_leaf if root is None.")

        path = [root]

        while 1:
            cur = path[-1]
            if cur.right:
                path.append(cur.right)
            else:
                break

        return path

    @classmethod
    def next(cls, path):
        if not path:
            raise Exception("Can't call next if path is [].")

        chi = path[-1]

        if chi.right:
            path.extend(Path.min_leaf(chi.right))
            return True, path

        path.pop()

        while path:
            par = path[-1]
            if chi is par.right:
                chi = path.pop()
            else:
                break

        return bool(path), path

    @classmethod
    def previous(cls, path):
        if not path:
            raise Exception("Can't call previous if path is [].")

        chi = path[-1]

        if chi.left:
            path.extend(Path.max_leaf(chi.left))
            return True, path

        path.pop()

        while path:
            par = path[-1]
            if chi is par.left:
                chi = path.pop()
            else:
                break

        return bool(path), path

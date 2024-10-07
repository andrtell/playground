import collections


class Iter:
    @classmethod
    def pre_order(cls, root):
        if not root:
            return
        cur = root
        stk = []
        path = []
        while True:
            if cur:
                stk.append(cur)
                path.append(cur)
                yield path
                cur = cur.left
            elif stk:
                par = stk.pop()
                cur = par.right
                while path[-1] is not par:
                    path.pop()
            else:
                break

    @classmethod
    def in_order(cls, root):
        if not root:
            return
        cur = root
        stk = []
        path = []
        while True:
            if cur:
                stk.append(cur)
                path.append(cur)
                cur = cur.left
            elif stk:
                par = stk.pop()
                cur = par.right
                while path and path[-1] is not par:
                    path.pop()
                yield path
            else:
                break

    @classmethod
    def post_order(cls, root):
        if not root:
            return
        cur = root
        stk = []
        path = []
        while True:
            if cur:
                stk.append(cur)
                path.append(cur)
                cur = cur.left
            elif stk:
                par = stk.pop()
                cur = par.right
                while path and path[-1] is not par:
                    yield path
                    path.pop()
            else:
                break
        while path:
            yield path
            path.pop()

    # TODO: path
    @classmethod
    def level_order(cls, root):
        if not root:
            return
        cnt = 1
        que = collections.deque([root])
        while cnt:
            while cnt > 0:
                cnt -= 1
                node = que.popleft()
                yield node
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            cnt = len(que)

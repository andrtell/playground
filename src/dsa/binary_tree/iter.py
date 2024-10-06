import collections


class Iter:
    @classmethod
    def pre_order(cls, root):
        if not root:
            return
        cur = root
        his = []
        pth = []
        while True:
            if cur:
                yield cur, pth
                his.append(cur)
                pth.append(cur)
                cur = cur.left
            elif his:
                par = his.pop()
                cur = par.right
                while pth and par is not pth[-1]:
                    pth.pop()
            else:
                break

    @classmethod
    def in_order(cls, root):
        if not root:
            return
        cur = root
        his = []
        pth = []
        while True:
            if cur:
                his.append(cur)
                pth.append(cur)
                cur = cur.left
            elif his:
                par = his.pop()
                cur = par.right
                while pth and pth[-1] is not par:
                    pth.pop()
                if pth:
                    pth.pop()
                yield par, pth
                pth.append(par)
            else:
                break

    @classmethod
    def post_order(cls, root):
        if not root:
            return
        cur = root
        his = []
        pth = []
        while True:
            if cur:
                his.append(cur)
                pth.append(cur)
                cur = cur.left
            elif his:
                par = his.pop()
                cur = par.right
                while pth and pth[-1] is not par:
                    yield pth.pop(), pth
            else:
                break
        while pth:
            yield pth.pop(), pth

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

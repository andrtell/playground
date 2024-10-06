from dsa.binary_tree.iter import Iter


class Format:
    @classmethod
    def horizontal(cls, tree):
        stem = []
        lines = []
        for node, path in Iter.pre_order(tree.root):
            while len(stem) > len(path):
                stem.pop()
            if len(stem) < len(path):
                tmp = ""
                if len(path) > 1:
                    pp, p = path[-2:]
                    if pp.left is p and pp.right:
                        tmp = "│   "
                    else:
                        tmp = "    "
                stem.append(tmp)
            ans = "".join(stem)
            if path:
                if path[-1].left is node:
                    if path[-1].right:
                        ans += "├── "
                    else:
                        ans += "└── "
                else:
                    ans += "└── "
            ans += str(node.value)
            lines.append(ans)
        return "\n".join(lines)

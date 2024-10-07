from dsa.binary_tree.iter import Iter


class Format:
    @classmethod
    def horizontal(cls, tree):
        lines = []
        for node, path in Iter.pre_order(tree.root):
            ans = ""
            for j in range(0, len(path) - 1):
                s = ""
                p0 = path[j]
                p1 = path[j + 1]
                if p0.left is p1 and p0.right:
                    s = "│   "
                else:
                    s = "    "
                ans += s
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

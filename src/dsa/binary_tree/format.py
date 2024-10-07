from dsa.binary_tree.iter import Iter


class Format:
    @classmethod
    def horizontal_1(cls, root):
        for path in Iter.pre_order(root):
            end = ["", str(path[-1].value)]
            if len(path) > 1:
                if path[-2].left is path[-1]:
                    if path[-2].right:
                        end[0] = "├── "
                    else:
                        end[0] = "└── "
                else:
                    end[0] = "╘══ "
            buff = []
            for j in range(1, len(path) - 1):
                if path[j - 1].left is path[j] and path[j - 1].right:
                    buff.append("│   ")
                else:
                    buff.append("    ")
            buff.extend(end)
            yield "".join(buff)

    @classmethod
    def horizontal_2(cls, root):
        for path in Iter.in_order(root):
            end = ["", str(path[-1].value)]
            if len(path) > 1:
                if path[-2].left is path[-1]:
                    end[0] = "┌── "
                else:
                    end[0] = "╘══ "
            buff = []
            for j in range(1, len(path) - 1):
                p0, p1, p2 = path[j - 1 : j + 2]
                if p0.left is p1 and p1.right is p2:
                    buff.append("│   ")
                elif p0.right is p1 and p1.left is p2:
                    buff.append("│   ")
                else:
                    buff.append("    ")
            buff.extend(end)
            yield "".join(buff)

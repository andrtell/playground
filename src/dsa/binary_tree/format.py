from dsa.binary_tree.iter import Iter


class Format:
    @classmethod
    def horizontal(cls, root):
        lines = []
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

            lines.append("".join(buff))
            
        return "\n".join(lines)

from dsa.binary_tree.iter import Iter

class Format:
    @classmethod
    def horizontal(cls, tree):
        lines = []
        stem = []

        for node, info in Iter.pre_order(tree.root):
            line = ""

            if info.depth:
                line += "   " * (info.depth - 1)
                line += (info.last and "└──") or "├──"

            line += str(node.value)
            
            lines.append(line)

        return "\n".join(lines)

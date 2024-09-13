from ds.binary_tree.node import Node


def test_isolated_node():
    node = Node(None)
    assert node.is_leaf()
    assert not node.is_child()
    assert not node.is_left()
    assert not node.is_right()


def test_node_left():
    left = Node(None)

    parent = Node(None, left=left)

    assert parent.left is left

    assert parent.degree() == 1
    assert not parent.is_leaf()
    assert parent.first_child() is left

    assert left.degree() == 0
    assert left.is_leaf()
    assert left.is_child()
    assert left.is_left()
    assert not left.is_right()

    parent.set_left(None)

    assert parent.is_leaf()
    assert parent.first_child() is None
    assert parent.degree() == 0

    parent.set_left(left)

    assert parent.degree() == 1
    assert not parent.is_leaf()
    assert parent.first_child() is left

    assert left.degree() == 0
    assert left.is_leaf()
    assert left.is_child()
    assert left.is_left()
    assert not left.is_right()


def test_node_right():
    right = Node(None)

    parent = Node(None, right=right)

    assert parent.right is right

    assert parent.degree() == 1
    assert not parent.is_leaf()
    assert parent.first_child() is right

    assert right.degree() == 0
    assert right.is_leaf()
    assert right.is_child()
    assert right.is_right()
    assert not right.is_left()

    parent.set_right(None)

    assert parent.is_leaf()
    assert parent.first_child() is None
    assert parent.degree() == 0

    parent.set_right(right)

    assert parent.degree() == 1
    assert not parent.is_leaf()
    assert parent.first_child() is right

    assert right.degree() == 0
    assert right.is_leaf()
    assert right.is_child()
    assert right.is_right()
    assert not right.is_left()


def test_node_left_right():
    left = Node(None)
    right = Node(None)

    parent = Node(None, left=left, right=right)

    assert parent.left is left
    assert parent.right is right

    assert parent.degree() == 2
    assert not parent.is_leaf()
    assert parent.first_child() is left

    assert left.is_child()
    assert left.is_left()
    assert not left.is_right()
    assert left.degree() == 0

    assert right.is_child()
    assert right.is_right()
    assert not right.is_left()
    assert right.degree() == 0

    parent.set_left(None)

    assert parent.first_child() == right
    assert parent.degree() == 1
    assert parent.left is None
    assert parent.right is right

    parent.set_left(left)

    assert parent.first_child() == left
    assert parent.degree() == 2
    assert parent.left is left
    assert parent.right is right

    assert left.is_child()

    parent.set_right(None)

    assert parent.first_child() == left
    assert parent.degree() == 1
    assert parent.left is left
    assert parent.right is None

    parent.set_right(right)

    assert parent.first_child() == left
    assert parent.degree() == 2
    assert parent.left is left
    assert parent.right is right

    assert right.is_child()

    parent.set_left(None)
    parent.set_right(None)

    assert parent.first_child() is None
    assert parent.degree() == 0
    assert parent.left is None
    assert parent.right is None

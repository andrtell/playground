from ds.binary_tree.bst import BSNode


def test_rotate_left():
    cll = BSNode(-3)
    clr = BSNode(-1)
    cl = BSNode(-2, left=cll, right=clr)
    crl = BSNode(1)
    crr = BSNode(3)
    cr = BSNode(2, left=crl, right=crr)
    pp = BSNode(0, left=cl, right=cr)
    BSNode.rotate_left(pp)
    root = cr
    assert root.left is pp
    assert pp.left is cl
    assert pp.right is crl
    assert cl.left is cll
    assert cl.right is clr
    assert root.right is crr


def test_rotate_right():
    cll = BSNode(-3)
    clr = BSNode(-1)
    cl = BSNode(-2, left=cll, right=clr)
    crl = BSNode(1)
    crr = BSNode(3)
    cr = BSNode(2, left=crl, right=crr)
    pp = BSNode(0, left=cl, right=cr)
    BSNode.rotate_right(pp)
    root = cl
    assert root.right is pp
    assert pp.right is cr
    assert pp.left is clr
    assert cr.left is crl
    assert cr.right is crr
    assert root.left is cll


def test_next_prev_1():
    cl = BSNode(-1)
    cr = BSNode(1)
    pp = BSNode(0)
    pp.set_left(cl)
    pp.set_right(cr)
    assert cr is next(BSNode.next(pp))
    assert cl is next(BSNode.prev(pp))
    assert pp is next(BSNode.prev(next(BSNode.next(pp))))
    assert pp is next(BSNode.next(next(BSNode.prev(pp))))
    assert cr is next(BSNode.next(next(BSNode.next(cl))))
    assert cl is next(BSNode.prev(next(BSNode.prev(cr))))


def test_isolated_node():
    node = BSNode(None)
    assert node.is_leaf()
    assert not node.is_child()
    assert not node.is_left()
    assert not node.is_right()


def test_node_left():
    left = BSNode(None)

    parent = BSNode(None, left=left)

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
    right = BSNode(None)

    parent = BSNode(None, right=right)

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
    left = BSNode(None)
    right = BSNode(None)

    parent = BSNode(None, left=left, right=right)

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

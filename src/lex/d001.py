#
# 1
#

s = "Python"

print(s[-2])
print(s[:4])
print(s[1:4])
print(s[::-1])

#
# 2
#

l1 = [3, 7, [1, 4, "hello"]]
l1[2][2] = "goodbye"
assert l1 == [3, 7, [1, 4, "goodbye"]]

#
# 3
#

d1 = {"simple_key": "hello"}
assert d1["simple_key"] == "hello"

d2 = {"k1": {"k2": "hello"}}
assert d2["k1"]["k2"] == "hello"

d3 = {"k1":[{"nest_key":["this is deep", ["hello"]]}]}
assert d3["k1"][0]["nest_key"][1][0] == "hello"

#
# 4
#

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
assert list(set(mylist)) == [1,2,3]

#
# 5
#

age = 4
name = "Sammy"

print(f"Hello my dog's name is {name} and he is {age} years old")

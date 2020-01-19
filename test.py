def func1(lst):
    if len(lst) == 0:
        return 0
    else:
        x = func1(lst[1:])
        return lst[0] + x


def my_member(x, lst):
    if len(lst) == 0:
        return False
    elif x == lst[0]:
        return True
    else:
        return my_member(x, lst[1:])


def make_adder(x):
    return lambda y: x + y


def foldr(func, base, lst):
    if len(lst) == 0:
        return base
    else:
        return func(lst[0], foldr(func, base, lst[1:]))


def add(x, rror):
    return x + rror


def cons(elem, lst):
    lst.insert(0, elem)
    return lst


def my_map(f, lst):
    return foldr(lambda x, rror: cons(f(x), rror), [], lst)


def mult_2(x):
    return 2 * x


def foldl(func, base, lst0):
    def foldl_acc(lst, acc):
        if len(lst) == 0:
            return acc
        else:
            return foldl_acc(lst[1:], func(lst[0], acc))

    return foldl_acc(lst0, base)


def my_reverse(lst):
    return foldl(cons, [], lst)


def my_filter(exp, lst):
    if len(lst) == 0:
        return []
    elif exp(lst[0]):
        return cons(lst[0], my_filter(exp, lst[1:]))
    else:
        return my_filter(exp, lst[1:])


eatApples = my_filter(
    lambda x: x != "apple",
    ["apple", "orange", "banana", "apple", "guava"])

print(eatApples)

add_3 = make_adder(3)

print(add_3(2))

print(foldr(add, 0, [1, 2, 3, 4, 5]))

add_5 = make_adder(5)
print(add_5(7))

print(cons([1, 2, 3], [4, 5, 6]))

print(my_map(mult_2, [1, 2, 3, 4]))

print(my_reverse([1, 2, 3]))


def isPalindrome(str):
    if str == "" or len(str) == 1:
        return True
    elif str[0] == str[-1]:
        return isPalindrome(str[1:-1])
    else:
        return False


def transloc(loc, spec):
    if len(spec) == 0:
        return []
    else:
        return cons(transchar(loc[0], spec), transloc(loc[1:], spec))


def strToLst(s):
    if len(s) == 0:
        return []
    else:
        return cons(s[0], (strToLst[s[1:]]))


def lstToStr(loc):
    if len(loc) == 0:
        return ""
    else:
        return loc[0] + lstToStr(loc[1:])


def transchar(ch, spec):
    if len(spec) == 0:
        return ch
    elif spec[0][0](ch):
        return spec[0][1](ch)
    else:
        return transchar(ch, spec[1:])


def translate(s, spec):
    return transloc(strToLst(s), spec)


class FSO(object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def get_name(self):
        return self.name

    def get_owner(self):
        return self.owner


class File(FSO):
    def __init__(self, name, size, owner):
        FSO.__init__(self, name, owner)
        self.size = size

    def get_size(self):
        return self.size


class Dir(FSO):
    def __init__(self, name, owner, contents):
        FSO.__init__(self, name, owner)
        self.contents = contents

    def get_contents(self):
        return self.contents


def adder(fso, lol):
    if len(lol) == 0:
        return []
    else:
        return [[fso.get_name()] + lol[0]] + adder(fso, lol[1:])


def owned_by(fso, owner):
    if type(fso) == File:
        if fso.get_owner() == owner:
            return [[fso.get_name()]]
        else:
            return []
    elif type(fso) == Dir:
        if fso.get_owner() == owner:
            return [[fso.get_name()], adder(fso, owned_by_lst(fso.get_contents(), owner))]
        else:
            return adder(fso, owned_by_lst(fso.get_contents(), owner))


def owned_by_lst(contents, owner):
    if len(contents) == 0:
        return []
    else:
        path = owned_by(contents[0], owner)
        if len(path) == 0:
            return owned_by_lst(contents[1:], owner)
        else:
            return path + (owned_by_lst(contents[1:], owner))


example_fs = Dir("root", "root",
             [
                 Dir("Dan", "dan",
                     [
                         File("log.txt", 768, "dan"),
                         File("profile.jpg", 60370, "dan"),
                         Dir("music", "dan", [File("Thelonius Monk.mp3", 92227584, "dan")])]),

                 Dir("Slides", "teaching",
                     [
                         Dir("cs135", "teaching",
                             [
                                 File("01-intros.pdf", 72244, "teaching"),
                                 File("11-trees.pdf", 123124, "teaching"),
                                 Dir("system", "root",
                                     [
                                         Dir("logs", "teaching", [])])
                             ])
                     ]),

                 File("vmlinuz", 30, "root")
              ])

print(owned_by(example_fs, "dan"))

x = [("name", "dhruv"), ("name2", "omar")]
x[0] = x[0] + ("hi", )
print(x)

L1 = ["name", "dhruv"]
L2 = ["name2", "omar"]
y = [L1, L2]
L1.append("hii")
print(y)





test_list = ['a',1,'I',(1),'a',3.14]
test_list.append(2)
print(test_list)
test_list.clear()
print(test_list)
test_list = ['a',1,'I',(1),'a',3.14]
test_list_cp = test_list.copy()
print(test_list_cp)
test_list_cp[0] = 'b'
print(test_list)
print(test_list.count('a'))
test_list.extend(test_list_cp)
print(test_list)
test_list.index('a')
test_list.insert(0,'a0')
print(test_list)
print(test_list.pop(3))
print(test_list)
test_list.remove('a')
print(test_list)
test_list.reverse()
print(test_list)
def my_fun(x):
    x = str(x)
    if len(x) == 0:
        return []
    if len(x) == 1:
        return [ord(x)]
    else:
        return [ord(_) for _ in x]

test_list.sort(key=my_fun)
print(test_list)


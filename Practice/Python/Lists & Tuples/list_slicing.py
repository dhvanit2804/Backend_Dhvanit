l = [1,2,3,10,20,30,"tops",True,"python",False,"java",100,200,11,22,1.1,2.2]

print(l[0:2:5])
print(l[15::5])
print(l[1:3:3])
print(l[::16])
print(l[10:12])

print(l[:-17:17])
print(l[-15::10])
print(l[-16:-14:5])
print(l[::-9])
print(l[-13:-7])

'''
[1]
[1.1]
[2]
[1, 2.2]
['java', 100]
[]
[3, 200]
[2]
[2.2, True]
[20, 30, 'tops', True, 'python', False]
'''
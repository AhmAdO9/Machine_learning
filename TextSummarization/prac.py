# data = b'{"\xe6\x9d\xb1\xe4\xba\xac"}'
# data1 = b'\xff\xfeh\x00e\x00l\x00l\x00o\x00'
# with open('file.txt', 'wb') as file:
#     file.write(data)
# with open('README.md','rb') as file:
#     f = file.read()
#     print(f)

# import yaml
# from pathlib import Path
# from box import ConfigBox

# # with open('file.yaml', 'w') as f:
# #     yaml.safe_dump("hello", f)

# def read_yaml(path:Path)->ConfigBox:
#     with open(path, 'r') as f:
#         s = yaml.safe_load(f)
#         return s

# path = Path('file.yaml')

# j = read_yaml(path)
# print(j['name'])

# text = "hello"
# import base64
# s = base64.b64encode(data1)
# t = text.encode('utf-16')

# import sys

# try:
#     x = 1/0
# except Exception as e:

#     type,value, tb = sys.exc_info()

# print(type)
# print(value)
# print(tb.tb_frame.f_code.co_filename)


# def square(x):
#     return x**2


# numbers = [1,2,3,4,5]

# # s = map(square, numbers)

# s = numbers.map(square)

# print(list(s))\\

# num = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0, 10, 2):
#     print(num[i:i+2])

# s = "dfsdfs"
# print((",".join(s)).split(","))

a = [1,2,3]
b =  [5,6,7]
c = [8,9,0]

for i,j,k in zip(a,b,c):
    print(type(i))
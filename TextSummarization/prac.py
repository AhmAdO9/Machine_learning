data = b'{"\xe6\x9d\xb1\xe4\xba\xac"}'
data1 = b'\xff\xfeh\x00e\x00l\x00l\x00o\x00'
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

text = "hello"
import base64
s = base64.b64encode(data1)
t = text.encode('utf-16')

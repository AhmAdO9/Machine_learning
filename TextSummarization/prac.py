import sys

try:
    x = 1/0
except Exception as e:

    type,value, tb = sys.exc_info()

print(type)
print(value)
print(tb.tb_frame.f_code.co_filename)
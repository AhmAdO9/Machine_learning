# with open('requirements.txt', "r") as file:
#     print(file.readlines())

import sys 

# print(sys.platform)
 

import os 

import sys
import logging 

# from dataclasses import dataclass

# # @dataclass
# class easy:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y


# obj = easy(1,2)
# ob = easy(1,2)
# print()


# def error_message_details(error, sys):
#     _,_,exc_tb = sys.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     error_message = "Error occured in python script name: {0} & line number {1} & error message: {2}".format(
#     file_name,exc_tb.tb_lineno, str(error)
#     )
#     print(error_message)


# try:
#     a=1/0
# except Exception as e:
#     # logging.info("logging has started!")
#     error_message_details(e, sys)


# class Human:
#     def __init__(self, legs) -> None:
#         self.legs=legs


# class Boy(Human):
#     def __init__(self, arms) -> None:
#         # print(super().__init__(legs))
#         self.arms=arms

#     def __str__(self)->str:

#         return (f"i have a total of {self.arms} arms")
    

# boy_obj = Boy(2)
# print(boy_obj)


# models = {
#     "Linear Regression":1,
#     "Lasso":2

# }

# print(list(models.values()))


# def helloWorld(x:str)->None:
#     return 1

# print(helloWorld(1))

# data = []

# x,y = zip(data)
# print(x,y)

import os

# Set NUMEXPR_MAX_THREADS to your desired value
# os.environ['NUMEXPR_MAX_THREADS'] = '12'


# Check the value of NUMEXPR_MAX_THREADS
# numexpr_max_threads = os.environ.get('NUMEXPR_MAX_THREADS')

# if numexpr_max_threads is not None:
#     print(f'NUMEXPR_MAX_THREADS is set to {numexpr_max_threads}')
# else:
#     print('NUMEXPR_MAX_THREADS is not set.')

# file_name = os.path.dirname("../ml_Project/artifacts/yolo.py")

# os.makedirs(file_name, exist_ok=True)


data = {
    "a":1,
    "b":2
}

d_list = list(data.keys())[1]
print(d_list)
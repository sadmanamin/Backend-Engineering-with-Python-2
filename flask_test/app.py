
# from contextlib import contextmanager

# class A:
#     def __init__(self):
#         print('I am inside constructor')
#     def __enter__(self):
#         print('I am inside enter')
#         return "Hello"
#     def __exit__(self,exception_type, exception_value, traceback):
#         print('I am inside exit')
#         print(exception_type,exception_value,traceback)

# class MessageWriter(object):
#     def __init__(self, filename):
#         self.file_name = filename

#     @contextmanager
#     def open_file(self):
#         try:
#             file = "hello"
#             yield file
#             print('I am exiting.')
#         finally:
#             print('I am inside exit')

# with MessageWriter('hello.txt').open_file() as my_file:
#     print(my_file)
#     print('Helloooo')

def test_yield():
    yield 1

a = test_yield()
print(a)

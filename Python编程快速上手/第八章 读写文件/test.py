import os

print(os.getcwd())

# print(os.chdir('/'))
# os.mkdir('build')


print(os.getcwd())
print(os.path.relpath(os.getcwd(), '/Users/mac/PycharmProjects/PythonOps/Python编程快速上手'))
print(os.path.basename(os.getcwd()))
print(os.path.dirname(os.getcwd()))
print(os.path.getsize(os.getcwd()))
print(os.listdir())
print(open(os.listdir()[0]).read())

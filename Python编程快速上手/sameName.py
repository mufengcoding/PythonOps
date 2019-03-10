def spam():
    global eggs
    eggs = 'spam'


eggs = 'gload'
spam()
print(eggs)

immutable_var = 18, 12, True, False, "cosmos"
print(immutable_var) # кортежи неизменяемые объекты,
# immutable_var.remove(2) # AttributeError: 'tuple' object has no attribute 'remove'
mutable_list = [5, 7, "october", True, False]
print(mutable_list)
mutable_list.append([12 , 19])
mutable_list.remove(False)
print(mutable_list)
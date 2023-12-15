d={"mon":1,"dad":2,"son":3}

def change_dict(d:dict):
    d={"uncle":4}
    d.update({"aunt":5})
    return d

change_dict(d)
print(d)


#{'mon': 1, 'dad': 2, 'son': 3}
#if uncle key value pair not defined
#then aunt key value will be added.
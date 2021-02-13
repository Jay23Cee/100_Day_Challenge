txt = "A plan, has a man"


def is_palindrone(s):
    new_str = []
    for x in s:
        if not x.isalpha():
            continue
        new_str.append(x.islower())
        
    new_str = "".join(new_str)
    return is_palindrone(new_str)






print(is_palindrone(txt))
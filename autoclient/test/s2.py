import s1


for key in dir(s1):
    if key.isupper():
        print(key, getattr(s1, key))
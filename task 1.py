def kwargsAcceptFun(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargsAcceptFun(name="Timur", age=21, country="Kazakhstan")

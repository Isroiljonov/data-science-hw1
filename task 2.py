def typeBasedTransformer(**kwargs):

    transformed = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed[key] = value ** 2
        elif isinstance(value, str):
            transformed[key] = value[::-1]
        elif isinstance(value, bool):
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed[key] = value[::-1]
        elif isinstance(value, dict):
            if len(set(value.values())) == len(value.values()):
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value
        else:
            transformed[key] = value

    return transformed


print(typeBasedTransformer(num=4, text="Hello", flag=True, items=[1, 2, 3], mapping={"a": 1, "b": 2}))

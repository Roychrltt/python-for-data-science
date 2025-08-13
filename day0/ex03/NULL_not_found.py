def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif object == '' and type(object) is str:
        print(f"Empty: {type(object)}")
        return 0
    elif object is False and type(object) is bool:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1

def first_and_last(value):
    if not value:
        return {"first": "", "last": ""}
    return {
        "first": value[0],
        "last": value[-1]
    }
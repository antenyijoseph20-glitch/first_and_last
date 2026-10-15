def get_initials(name):
    if not name:
        return ""
    words = name.split()
    initials = []
    for word in words:
        initials.append(word[0].upper())
    return ".".join(initials) + "."
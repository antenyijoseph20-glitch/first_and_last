def slug_maker(title):
    title = title.strip()
    title = title.lower()
    title = title.replace(",", "")
    title = title.replace(".", "")
    title = title.replace(" ", "-")

    return title


def get_fullname(name, surname, otasi="") :
    if otasi :
        return f"{name} {otasi} {surname}".title()
    else:
        return f"{name} {surname}".title()

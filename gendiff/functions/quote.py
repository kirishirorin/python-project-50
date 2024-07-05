def form(value, option='mark'):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str) and option != 'without mark':
        return f"'{value}'"
    else:
        return value

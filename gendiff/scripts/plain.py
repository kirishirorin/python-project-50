from gendiff.scripts.quote import form


def hard(cond, different):
    if cond:
        return '[complex value]'
    else:
        return form(different)


def check(cond):
    return isinstance(cond, dict)


def plain(dif, path=''):
    text = []
    st = 'Property '
    for key in dif.keys():
        if isinstance(dif[key], dict):
            key_v = list(dif[key].keys())[0]
            match key_v:
                case 'remove':
                    text.append(f"{st}'{path}{key}' was removed")
                case 'add':
                    value = hard(check(dif[key]['add']), dif[key]['add'])
                    text.append(f"{st}'{path}{key}' "
                                f"was added with value: {value}")
                case 'update':
                    text.append(plain(dif[key]['update'], path=f'{path}{key}.'))
        if key == 'before':
            text.append(f"{st}'{path[:-1]}' was updated. "
                        f"From {hard(check(dif['before']), dif['before'])} "
                        f"to {hard(check(dif['after']), dif['after'])}")
    text_sorted = sorted(text, key=lambda x: x)
    return '\n'.join(text_sorted)

from gendiff.scripts.quote import form


def treeing(diction, deeper):
    if isinstance(diction, dict):
        text = []
        deeper_level = deeper * 4 - 2
        for key in diction:
            text.append(f'{" " * deeper_level}  {key}: '
                        f'{treeing(diction[key], deeper + 1)}')
        text_sorted = sorted(text, key=lambda x: x[deeper_level + 2:])
        text_sorted.insert(0, '{')
        text_sorted.append((' ' * (deeper_level - 2)) + '}')
        return '\n'.join(text_sorted)
    else:
        return form(diction, 'without mark')


def stylish(different, deeper=1):
    text = []
    deeper_level = deeper * 4 - 2
    for key in different.keys():
        if isinstance(different[key], dict):
            key_v = list(different[key].keys())[0]
            match key_v:
                case 'remove':
                    d_rm = treeing(different[key]['remove'], deeper + 1)
                    text.append(f"{' ' * deeper_level}- {key}: "
                                f"{d_rm}")
                case 'add':
                    d_ad = treeing(different[key]['add'], deeper + 1)
                    text.append(f"{' ' * deeper_level}+ {key}: "
                                f"{d_ad}")
                case 'update':
                    d_up = different[key]['update']
                    if list(d_up.keys())[0] != 'before':
                        text.append(f"{' ' * deeper_level}  {key}: "
                                    f"{stylish(d_up, deeper + 1)}")
                    else:
                        text.append(f"{' ' * deeper_level}- {key}: "
                                    f"{stylish(d_up, deeper + 1)[0]}")
                        text.append(f"{' ' * deeper_level}+ {key}: "
                                    f"{stylish(d_up, deeper + 1)[1]}")
                case 'unchanged':
                    d_un = treeing(different[key]['unchanged'], deeper + 1)
                    text.append(f"{' ' * deeper_level}  {key}: "
                                f"{d_un}")
        if key == 'before':
            d_be = treeing(different['before'], deeper)
            d_af = treeing(different['after'], deeper)
            return (d_be, d_af)
    text_sorted = sorted(text, key=lambda x: x[deeper_level + 2:(x.index(':'))])
    text_sorted.insert(0, "{")
    text_sorted.append((" " * (deeper_level - 2)) + "}")
    return "\n".join(text_sorted)

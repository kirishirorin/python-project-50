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
            if list(different[key].keys())[0] == 'remove':
                text.append(f"{' ' * deeper_level}- {key}: "
                            f"{treeing(different[key]['remove'], deeper + 1)}")
            elif list(different[key].keys())[0] == 'add':
                text.append(f"{' ' * deeper_level}+ {key}: "
                            f"{treeing(different[key]['add'], deeper + 1)}")
            elif list(different[key].keys())[0] == 'update':
                if list(different[key]['update'].keys())[0] != 'before':
                    text.append(f"{' ' * deeper_level}  {key}: "
                                f"{stylish(different[key]['update'], deeper + 1)}")
                else:
                    text.append(f"{' ' * deeper_level}- {key}: "
                                f"{stylish(different[key]['update'], deeper + 1)[0]}")
                    text.append(f"{' ' * deeper_level}+ {key}: "
                                f"{stylish(different[key]['update'], deeper + 1)[1]}")
            elif list(different[key].keys())[0] == 'unchanged':
                text.append(f"{' ' * deeper_level}  {key}: "
                            f"{treeing(different[key]['unchanged'], deeper + 1)}")
        if key == 'before':
            return (treeing(different['before'], deeper), treeing(different['after'], deeper))
    text_sorted = sorted(text, key=lambda x: x[deeper_level + 2:(x.index(':'))])
    text_sorted.insert(0, "{")
    text_sorted.append((" " * (deeper_level - 2)) + "}")
    return "\n".join(text_sorted)

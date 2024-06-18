from gendiff.scripts.quote import form


def plain(different, path=''):
    text = []
    for key in different.keys():
        if isinstance(different[key], dict):
            if list(different[key].keys())[0] == 'remove':
                text.append(f"Property '{path}{key}' was removed")
            elif list(different[key].keys())[0] == 'add':
                value = '[complex value]' if isinstance(different[key]['add'], dict) else form(different[key]['add'])
                text.append(f"Property '{path}{key}' was added with value: {value}")
            elif list(different[key].keys())[0] == 'update':
                text.append(plain(different[key]['update'], path=f'{path}{key}.'))
        if key == 'before':
            text.append(f"Property '{path[:-1]}' was updated. "
                        f"From {'[complex value]' if isinstance(different['before'], dict) else form(different['before'])} "
                        f"to {'[complex value]' if isinstance(different['after'], dict) else form(different['after'])}")
    text_sorted = sorted(text, key=lambda x: x)
    return '\n'.join(text_sorted)

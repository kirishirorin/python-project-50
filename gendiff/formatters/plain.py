from gendiff.functions.quote import form


def cut_dict(cond, different):
    if cond:
        return '[complex value]'
    else:
        return form(different)


def condition(diff, key_after, key, head, path):
    if key_after == 'remove':
        return (f"{head}'{path}{key}' was removed")
    elif key_after == 'add':
        value = cut_dict(isinstance(diff[key]['add'], dict), diff[key]['add'])
        return (f"{head}'{path}{key}' "
                f"was added with value: {value}")
    elif key_after == 'update':
        return (inner(diff[key]['update'],
                path=f'{path}{key}.'))


def across_key(diff, path):
    lines = []
    head = 'Property '
    for key in diff.keys():
        if isinstance(diff[key], dict):
            key_after = list(diff[key].keys())[0]
            result = condition(diff, key_after, key, head, path)
            if result:
                lines.append(result)
        if key == 'before':
            value_before = cut_dict(isinstance(diff['before'], dict),
                                    diff['before'])
            value_after = cut_dict(isinstance(diff['after'], dict),
                                   diff['after'])
            lines.append(f"{head}'{path[:-1]}' was updated. "
                         f"From {value_before} to {value_after}")
    return lines


def inner(diff, path=''):
    lines = across_key(diff, path)
    lines_sorted = sorted(lines, key=lambda x: x)
    return '\n'.join(lines_sorted)


def plain(diff):
    return inner(diff)

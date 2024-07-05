from gendiff.functions.quote import form


NUM_SPACE = 4


def treeing(diff, deeper):
    if isinstance(diff, dict):
        lines = []
        deeper_level = deeper * NUM_SPACE - 2
        for key in diff:
            lines.append(f'{" " * deeper_level}  {key}: '
                         f'{treeing(diff[key], deeper + 1)}')
        lines_sorted = sorted(lines, key=lambda x: x[deeper_level + 2:])
        lines_sorted.insert(0, '{')
        lines_sorted.append((' ' * (deeper_level - 2)) + '}')
        return '\n'.join(lines_sorted)
    else:
        return form(diff, 'without mark')


def condition(diff, key_after, key, deeper):
    deeper_level = deeper * NUM_SPACE - 2
    if key_after == 'remove':
        tree_remove = treeing(diff[key]['remove'], deeper + 1)
        return (f"{' ' * deeper_level}- {key}: "
                f"{tree_remove}")
    elif key_after == 'add':
        tree_add = treeing(diff[key]['add'], deeper + 1)
        return (f"{' ' * deeper_level}+ {key}: "
                f"{tree_add}")
    elif key_after == 'update':
        tree_update = diff[key]['update']
        if list(tree_update.keys())[0] != 'before':
            return (f"{' ' * deeper_level}  {key}: "
                    f"{inner(tree_update, deeper + 1)}")
        else:
            lines = []
            lines.append(f"{' ' * deeper_level}- {key}: "
                         f"{inner(tree_update, deeper + 1)[0]}")
            lines.append(f"{' ' * deeper_level}+ {key}: "
                         f"{inner(tree_update, deeper + 1)[1]}")
            return lines
    elif key_after == 'unchanged':
        tree_unchanged = treeing(diff[key]['unchanged'], deeper + 1)
        return (f"{' ' * deeper_level}  {key}: "
                f"{tree_unchanged}")


def inner(diff, deeper=1):
    lines = []
    deeper_level = deeper * NUM_SPACE - 2
    for key in diff.keys():
        if isinstance(diff[key], dict):
            key_after = list(diff[key].keys())[0]
            result = condition(diff, key_after, key, deeper)
            if isinstance(result, str):
                lines.append(result)
            elif isinstance(result, list):
                lines.extend(result)
        if key == 'before':
            tree_before = treeing(diff['before'], deeper)
            tree_after = treeing(diff['after'], deeper)
            return (tree_before, tree_after)
    lines_sorted = sorted(lines,
                          key=lambda x: x[deeper_level + 2:(x.index(':'))])
    lines_sorted.insert(0, "{")
    lines_sorted.append((" " * (deeper_level - 2)) + "}")
    return "\n".join(lines_sorted)


def stylish(diff, deeper=1):
    return inner(diff)

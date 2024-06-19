def diff(file1, file2):
    if isinstance(file1, dict) and isinstance(file2, dict):
        set_file_1 = set(file1.keys()) - set(file2.keys())
        set_file_2 = set(file2.keys()) - set(file1.keys())
        set_file_12 = set(file1.keys()) & set(file2.keys())
        d = {}
        for key in set_file_1:
            d.update({key: {"remove": file1[key]}})
        for key in set_file_2:
            d.update({key: {"add": file2[key]}})
        for key in set_file_12:
            if file1[key] == file2[key]:
                d.update({key: {"unchanged": file2[key]}})
            else:
                d.update({key: {"update": diff(file1[key], file2[key])}})
        return d
    else:
        return {"before": file1, "after": file2}

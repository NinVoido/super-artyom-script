METHOD_TO_CHECK = "get"
TYPE_TO_CHECK = list
ALL_METHODS = True
JUST_HELP = False


def is_dunder(mtd):
    return str(mtd[:1]) == "__"

methods = dir(TYPE_TO_CHECK)
for method in methods:
    if not ALL_METHODS and is_dunder(method):
        continue
    if JUST_HELP:
        if method == METHOD_TO_CHECK:
            help_target = getattr(TYPE_TO_CHECK, METHOD_TO_CHECK)
            print(help(help_target))
            break
    else:
        print(method)

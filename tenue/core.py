

# check if multiple args exists, return 1 if true, 0 if false
def multiple_args_exist(args):
    if len(args.split()) > 1:
        return 1
    else:
        print("This command requires at least two (2) arguments. Please type help <command>.")
        return 0

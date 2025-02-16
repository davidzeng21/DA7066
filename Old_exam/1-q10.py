def line_cleaner(line):
    for i in range(len(line)):
        if line[i] == "#":
            return line[:i]
    return line

def comment_remover(in_filename, out_filename):
    with open(in_filename, "r") as in_file, open(out_filename, "w") as out_file:
            for line in in_file:
                print(line_cleaner(line), file=out_file, end="")
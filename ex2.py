def read_data(filename):
    lines = []
    infile = None
    try:
        infile = open(filename, encoding="utf8")
        for line in infile:
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if infile is not None:
            infile.close()
    return lines


lines=read_data('age.txt')
print(lines)

#TODO home
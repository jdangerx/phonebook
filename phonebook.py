import argparse
import re

# phonebooks go here


def add(name, number, pbname):
    # needs to be refactored into a "change_a_phonebook" dealio
    try:
        pb = globals()[pbname]
    except KeyError:
        raise ValueError("No such phonebook.")

    line = "    " + '"{}": "{}",'.format(name, number)
    with open(__file__, "r") as source_file:
        source_lines = [l.rstrip() for l in source_file.readlines()]
    index_of_pb = source_lines.index(pbname + " = {")
    first, rest = source_lines[:index_of_pb+1], source_lines[index_of_pb+1:]
    new_source = "\n".join(first + [line] + rest)
    with open(__file__, "w") as source_file:
        source_file.write(new_source)


def create(pbname):
    if pbname in globals():
        raise ValueError("Phonebook already exists!")

    with open(__file__, "r") as source_file:
        source_lines = [l.rstrip() for l in source_file.readlines()]
    pbline = source_lines.index("# phonebooks go here")
    first, rest = source_lines[:pbline+1], source_lines[pbline+1:]
    new_source = "\n".join(first + ["", pbname + " = {", "}"] + rest)
    with open(__file__, "w") as source_file:
        source_file.write(new_source)


def lookup(name, pbname):
    # needs to be refactored into a "change_a_phonebook" dealio
    try:
        pb = globals()[pbname]
    except KeyError:
        raise ValueError("No such phonebook.")

    print("\n".join([n + " " + num for n, num in pb.items() if re.search(name, n)]))


def change(name, number, pbname):
    # needs to be refactored into a "change_a_phonebook" dealio
    try:
        pb = globals()[pbname]
    except KeyError:
        raise ValueError("No such phonebook.")

    with open(__file__, "r") as source_file:
        source_lines = [l.rstrip() for l in source_file.readlines()]
    # TODO : if the name is in two phonebooks, will change both
    new_line = '    "' + name + '": "' + number + '"'
    def replace(oldline):
        if oldline.startswith('    "' + name + '"'):
            new_line
        else:
            oldline
    new_source_lines = map(replace, source_lines)
    new_source = "\n".join(new_source_lines)
    with open(__file__, "w") as source_file:
        source_file.write(new_source)


def remove(name, pbname):
    # needs to be refactored into a "change_a_phonebook" dealio
    try:
        pb = globals()[pbname]
    except KeyError:
        raise ValueError("No such phonebook.")

    with open(__file__, "r") as source_file:
        source_lines = [l.rstrip() for l in source_file.readlines()]
    # TODO : if the name is in two phonebooks, will delete both
    new_source = "\n".join([l for l in source_lines if not l.startswith('    "' + name + '"')])
    with open(__file__, "w") as source_file:
        source_file.write(new_source)


def reverse_lookup(number, pbname):
    # needs to be refactored into a "change_a_phonebook" dealio
    try:
        pb = globals()[pbname]
    except KeyError:
        raise ValueError("No such phonebook.")

    print("\n".join([n + " " + num for n, num in pb.items() if re.search(number, num)]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help="Can only be 'add' or 'print' right now.")
    parser.add_argument('args', nargs='+', help="the rest of the args")

    args = parser.parse_args()
    globals()[args.command](*args.args)

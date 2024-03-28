#!/usr/bin/env python3

from sys import argv


def main():
    files = argv[1:]
    contents = [open(f).readlines() for f in files]

    if len(contents) == 0:
        return

    num_lines = len(contents[0])
    assert all(
        len(lines) == num_lines for lines in contents
    ), "Files don't have same number of lines."

    duplicate_line_indexes = set(
        line_idx
        for line_idx in range(1, num_lines)
        if contents[0][line_idx] == contents[0][line_idx - 1]
    )

    for file_idx, file in enumerate(files):
        with open(file, "w") as store:
            store.writelines(
                line
                for line_idx, line in enumerate(contents[file_idx])
                if line_idx not in duplicate_line_indexes
            )


if __name__ == "__main__":
    main()

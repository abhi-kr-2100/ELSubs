#!/usr/bin/env python3

from sys import argv

SENTENCE_ENDS = (".", "!", "?")


def main():
    files = argv[1:]
    contents = [open(f).readlines() for f in files]

    if len(contents) == 0:
        return

    num_lines = len(contents[0])
    assert all(
        len(lines) == num_lines for lines in contents
    ), "Files don't have same number of lines."

    main_line_indexes = [0] + [
        i
        for i, line in enumerate(contents[0], start=1)
        if line.strip().endswith(SENTENCE_ENDS) or i == num_lines
    ]

    for file_idx, file in enumerate(files):
        with open(file, "w") as store:
            joined_content = [
                " ".join(
                    line.strip()
                    for line in contents[file_idx][
                        main_line_indexes[i] : main_line_indexes[i + 1]
                    ]
                )
                + "\n"
                for i in range(len(main_line_indexes) - 1)
            ]
            store.writelines(joined_content)


if __name__ == "__main__":
    main()

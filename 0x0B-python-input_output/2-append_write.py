#!/usr/bin/python3
"""Function definiton for a appending to file"""


def append_write(filename="", text=""):
    """ Appends a string to a text file (UTF8) and returns
        the number of characters added

        Args:
            filename(str): name of file to be appended to
            text(str): string to append into file
        Return:
            number of characters added
    """
    with open(filename, "a", encoding="utf-8") as fp:
        return fp.write(text)

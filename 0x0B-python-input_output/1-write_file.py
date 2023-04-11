#!/usr/bin/python3
"""Function definiton for a file writer"""


def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8) and returns
        the number of characters written

        Args:
            filename(str): name of file to be written to
            text(str): string to write into file
        Return:
            number of characters written
    """
    with open(filename, "w", encoding="utf-8") as fp:
        return fp.write(text)

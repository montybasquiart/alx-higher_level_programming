#!/usr/bin/python3

if __name__ == "__main__":
    """A program that prints all names defined by the compiled module.
    """
    import hidden_4

    names = dir(hidden_4)
    names.sort()
    for name in names:
        if not name.startswith("__"):
            print(name)

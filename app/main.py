import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    cmd, fin, fout = parts

    if cmd != "cp":
        return

    if fin == fout:
        return

    if not os.path.exists(fin):
        return

    with open(fin, "r") as f1, open(fout, "w") as f2:
        f2.write(f1.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")

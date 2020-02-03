import os


def list_files(startpath):
    with open(os.path.join(startpath, "index.md"), "w", encoding="utf-8")\
            as file:
        for root, dirs, files in os.walk(startpath):
            if root.find(".git") >= 0 or root == startpath:
                pass
            else:
                level = root.replace(startpath, '').count(os.sep) - 1
                indent = '    ' * (level)
                file.write(
                    '{}- {}\n'.format(
                        indent,
                        "[" + os.path.basename(root) + "]" +
                        "(" + root.replace(" ", "%20") + ")"
                    )
                )
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    if(all(ext not in f for ext in
                           [".md", ".ini", ".yml", "build.py"])):
                        file.write(
                            '{}- {}\n'.format(
                                subindent,
                                "[" + os.path.basename(f) + "]" +
                                "(" +
                                os.path.join(root[2:], f).replace(" ", "%20")
                                + ")"
                            )
                        )


list_files(".")

import os


def list_files(startpath):
    with open(os.path.join(startpath, "index.md"), "w", encoding="utf-8")\
            as file:
        for root, dirs, files in os.walk(startpath):
            if root.find(".git") >= 0:
                pass
            else:
                level = root.replace(startpath, '').count(os.sep) - 1
                if level != -1:
                    if level <= 1:
                        indent = ' ' * 4 * (level)
                        file.write(
                            '{}- {}\n'.format(
                                indent,
                                "[" + os.path.basename(root) + "]" +
                                "(" + os.path.relpath(root, startpath)
                                .replace(" ", "%20") + ")"
                            )
                        )
                if level <= 0:
                    subindent = ' ' * 4 * (level + 1)
                    for f in files:
                        if(all(ext not in f for ext in
                               [".md", ".ini", ".yml", "build.py"])):
                            file.write(
                                '{}- {}\n'.format(
                                    subindent,
                                    "[_" + os.path.basename(f) + "_]" +
                                    "(" + os.path.relpath(os.path.join(root, f),
                                                          startpath)
                                    .replace(" ", "%20") + ")"
                                )
                            )
                else:
                    pass


for root, dirs, files in os.walk("."):
    list_files(root)

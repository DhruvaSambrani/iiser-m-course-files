#!/usr/bin/env python3

import os
import argparse
import re
import sys
import fnmatch

ignored = [
    "index.md",
    "README.md",
    "*.ini",
    "*.yml",
    ".git*",
    "_layout*"]


def list_files(startpath, depth=1):
    with open(
        os.path.join(startpath, "index.md"),
        "w",
        encoding="utf-8"
    ) as file:
        segs = startpath.split(os.path.sep)
        file.write("# " + (segs[-1]
                           if segs[-1] != "."
                           else args.homename) + "\n")
        file.write("#### ")
        list = []
        for i in range(len(segs)):
            temp = ""
            temp += "[" + (segs[i]
                           if segs[i] != "."
                           else args.homename) + "]"
            path_str = "/".join(
                [".." for j in range(len(segs) - i - 1)])
            temp += "(" + path_str + ")"
            list.append(temp)
        file.write(
            ("/").join(list))
        file.write("\n")
        for root, dirs, files in os.walk(startpath):
            if re.search(args.regex, root) is None:
                global subdircount
                subdircount += 1
                level = root.replace(startpath, '').count(os.sep) - 1
                if level != -1:
                    if level <= depth:
                        indent = ' ' * 4 * (level)
                        file.write(
                            '{}- {}\n'.format(
                                indent,
                                "[" + os.path.basename(root) + "]"
                                "(" + os.path.relpath(root, startpath)
                                .replace(" ", "%20")
                                .replace(".md", "")
                                .replace(os.path.sep, "/") + ")"
                            )
                        )
                if level <= depth - 1:
                    subindent = ' ' * 4 * (level + 1)
                    for f in files:
                        if(re.search(args.regex, f) is None):
                            global filecount
                            filecount += 1
                            if args.verbose:
                                print("\t\t" + f)
                            file.write(subindent + "- ")
                            file.write("[_" + os.path.basename(f) + "_]")
                            path_str = os.path.relpath(
                                os.path.join(root, f), startpath)
                            file.write(
                                "(" + path_str.replace(" ", "%20")
                                .replace(".md", "")
                                .replace(os.path.sep, "/") + ")")
                            file.write("\n")
                        else:
                            if args.verbose:
                                print("\t\t" + f + " ignored")


parser = argparse.ArgumentParser(
    description='Build an index for all files to use for a static website')
parser.add_argument('root', metavar='root', type=str, nargs="?", default=".",
                    help='root dir from where to index')
parser.add_argument('-i', '--add_ignore_paths', dest='ignore', nargs="*",
                    default=[], help='Regex to ignore. '
                    'File Paths which match these are ignored')
parser.add_argument('-I', '--default_ignore', action='store_true',
                    dest='use_default', default=False,
                    help='Use this flag if you want to '
                    'ALSO use the default ignore')
parser.add_argument('-g', '--git-ignore', action='store_true',
                    dest='use_git_ignore', default=False,
                    help='Use this flag if you want to '
                    'ALSO ignore from .gitignore at the root')
parser.add_argument('-n', '--homename', dest='homename', type=str, default=".",
                    help="The name to give the root dir.")
parser.add_argument('-c', '--clean', dest='clean', action="store_true",
                    default=False, help="Clean old index files.")
parser.add_argument('-v', dest='verbose', action="store_true", default=False,
                    help="Print dirs and files indexed")

args = parser.parse_args()

if args.use_default:
    args.ignore += ignored
if args.use_git_ignore:
    with open(args.root + "/.gitignore") as gifile:
        args.ignore += [i.rstrip() for i in gifile.readlines()]

args.regex = "|".join([fnmatch.translate(i) for i in args.ignore])
if (args.verbose):
    print(args)

filecount = 0
dircount = 0
subdircount = 0

homeroot = args.root
if args.clean:
    if (sys.platform == "linux"):
        os.system(
            "find " + homeroot + " -name index.md -print0 | xargs -0 rm"
        )
    elif (sys.platform == "win32"):
        os.system("powershell \"Get-ChildItem index.md -Recurse | rm\"")
    else:
        print("Unknown system. Old indexes not be removed")
for root, dirs, files in os.walk(homeroot):
    if re.search(args.regex, root) is None:
        if args.verbose:
            print(root)
        list_files(root)
        dircount += 1
    else:
        if args.verbose:
            print(root + " ignored.")

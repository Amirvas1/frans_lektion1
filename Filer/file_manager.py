import argparse
from pathlib import Path

def list_files(directory, file_type=None):
    files = []
    for item in Path(directory).iterdir():
        if item.is_file() and (file_type is None or item.suffix == file_type):
            files.append(item.name)
    return files

def main():
    parser = argparse.ArgumentParser(description="File manager")
    parser.add_argument("directory", help="Target directory")
    parser.add_argument("-o", "--operation", choices=["list", "copy", "move"], required=True, help="Choose operation to perform")

    parser.add_argument("-d", "--destination", help="Destination directory")
    parser.add_argument("-f", "--filetype", help="Filter files by type")

    args = parser.parse_args()

    if args.operation == "list":
        files = list_files(args.directory, args.filetype)
        print(f"Files in directory {args.directory}:")
        for file in files:
            print(file)

if __name__ == "__main__":
    main()

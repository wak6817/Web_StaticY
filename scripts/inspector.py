import subprocess
from collections import Counter
from pathlib import Path

files = list(Path(".").rglob("*"))
line_count = 0

file_count = sum(file.is_file() for file in files)
directory_count = sum(file.is_dir() for file in files)

print(f"Files\t{file_count}")
print(f"Folders\t{directory_count}")

for file in files:
    if file.is_file():
        try:
            line_count += len(file.read_text().splitlines())
        except (UnicodeDecodeError, PermissionError):
            pass

print(f"Lines\t{line_count}")

try:
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"],
        text=True
    ).strip()

    print("\nGit:")
    print(f"  Branch\n{branch}")

except subprocess.CalledProcessError:
    print("\nGit: Not a repository")

print("\nFiles:")
for file in files:
    print(f"  {file}")

extensions = Counter(
    file.suffix
    for file in files
    if file.is_file() and file.suffix
)

print("\nFile types:")
for extension, count in extensions.most_common():
    print(f" {extension}\t{count}")

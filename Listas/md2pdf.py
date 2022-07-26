import os
import sys
import subprocess

#find all md files in the current directory and subdirectories
md_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            md_files.append(os.path.join(root, file))

print(f"Found {len(md_files)} md files")
print("\n".join(md_files))
print("Converting...")

# Using pandoc to convert all md files to pdf
for md_file in md_files:
    pdf_file = md_file.replace(".md", ".pdf")
    subprocess.call(["pandoc", "-o", pdf_file, md_file])
    print(f"Converted {md_file} to {pdf_file}")

print("All Done!")
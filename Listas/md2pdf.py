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

# Using pandoc to convert all md files to html
pdf_files = []
for md_file in md_files:
    pdf_file = md_file.replace(".md", "")
    pdf_file = pdf_file + "solved" + ".html"
    pdf_files.append(pdf_file)
    print(f"Converting {md_file} ...")
    subprocess.call(["pandoc", "-o", pdf_file, md_file])
    if os.path.exists(pdf_file):
        print(f"Converted {md_file} to {pdf_file}")
    else:
        print(f"Failed to convert {md_file} to {pdf_file} you dumb idiot, you don't have pandoc installed")
        sys.exit(1)

# Using wkhtmltopdf to convert all html files to pdf

for pdf_file in pdf_files:
    pdf_file = pdf_file.replace("html", "pdf")
    print(f"Converting {pdf_file} ...")
    subprocess.call(["wkhtmltopdf", pdf_file, pdf_file])
    if os.path.exists(pdf_file):
        print(f"Converted {pdf_file} to {pdf_file}")
    else:
        print(f"Failed to convert {pdf_file} to {pdf_file} you dumb idiot, you probably don't have wkhtmltopdf installed")
        sys.exit(1)

print("All Done!")
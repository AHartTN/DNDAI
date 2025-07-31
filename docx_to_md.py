import os
from docx import Document
from markdownify import markdownify as md

def docx_to_md(docx_path, md_path):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    md_content = md('\n\n'.join(full_text))
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

def convert_all_docx(root_dir):
    for folder, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.docx'):
                docx_path = os.path.join(folder, file)
                md_path = os.path.splitext(docx_path)[0] + '.md'
                docx_to_md(docx_path, md_path)
                print(f"Converted: {docx_path} -> {md_path}")

if __name__ == "__main__":
    convert_all_docx("Research")

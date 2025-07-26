# DNDAI Workspace Cleanup & Migration Task List

_Last updated: 2025-07-23_

This checklist is for anyone new to this project. Each step is explained in detail, with definitions and examples, so you can follow along even if you have never seen this workspace before.

## 1. Documentation Migration & Cleanup

- [ ] **Replace Placeholder Files with Real Content**
    - **What is a placeholder file?**
      - A placeholder file is a file in the `docs/` folder that only contains a comment like `// Moved from documentation/xxx.md` and does not have any real documentation.
    - **What to do:**
      1. Open the placeholder file in `docs/` (for example, `docs/ai-implementation-architecture.md`).
      2. Open the file with the same name in the `documentation/` folder (for example, `documentation/ai-implementation-architecture.md`).
      3. Copy all the content from the `documentation/` file and paste it into the `docs/` file, replacing the placeholder comment.
      4. Save the file in `docs/`.
      5. Repeat for every `.md` file in `docs/` that is just a placeholder.
    - **After all files are copied:**
      - Delete the old files in `documentation/` only after you are sure the content is safely in `docs/`.

- [ ] **Update Links and Cross-References**
    - **What is a cross-reference?**
      - Any link in a Markdown file that points to another file in the project (for example, `[see here](../documentation/ai-implementation-architecture.md)`).
    - **What to do:**
      1. Search for links in all `.md` files that point to the `documentation/` folder.
      2. Change them so they point to the correct file in the `docs/` folder instead.
      3. Save your changes.

- [ ] **Images & Diagrams**
    - **What to do:**
      1. Make sure all image prompt files (for example, `feudal-hierarchy-diagram-prompt.txt`) are in the `docs/images/` folder.
      2. If you find duplicate or empty image prompt files, delete the extras and keep only one copy in `docs/images/`.
      3. Update any links in documentation that point to images so they use the `docs/images/` path.

- [ ] **Table of Contents & Index**
    - **What to do:**
      1. Open `docs/INDEX.md` and the root `Table of Contents.md` file.
      2. Make sure they list all the correct files and sections, matching the new structure in `docs/`.
      3. Remove or update any placeholder or outdated Table of Contents files.

- [ ] **Knowledge Aggregation**
    - **What to do:**
      1. Open `Knowledge Aggregation.md` in the root.
      2. Make sure it accurately lists the status of all documentation files.
      3. If there are duplicate or outdated aggregation/status files, remove or merge them.

## 2. Python Bytecode & Source Organization

- [ ] **Remove Placeholder `.pyc` Files from `docs/`**
    - **What is a placeholder `.pyc` file?**
      - These are files in `docs/` that only have a comment like `# Moved from __pycache__/xxx.cpython-xxx.pyc` and do not contain any real code.
    - **What to do:**
      1. Delete all `.pyc` files in `docs/` that are just placeholders.
      2. The real `.pyc` files should only be in the `__pycache__/` folder (or ignored in version control).

- [ ] **Review Python Source Files**
    - **What to do:**
      1. Make sure all `.py` files (Python source code) are in the correct folder (`src/` or the project root).
      2. If you find any `.py` files in the wrong place, move them to the right folder.

## 3. Root Directory Cleanup

- [ ] **Move or Cross-Link Important Root Files**
    - **What to do:**
      1. Check that important files in the root (like `.docx` files, `README.md`, and `context-document.md`) are mentioned in the documentation and Table of Contents.
      2. If they are not, add references or links to them in the appropriate places.
      3. If a file belongs in a different folder, move it and update any links.

## 4. General Workspace Organization

- [ ] **Remove Obsolete or Duplicate Files**
    - **What is an obsolete or duplicate file?**
      - An obsolete file is one that is empty, out of date, or replaced by a newer version.
      - A duplicate file is an extra copy of a file that already exists elsewhere in the project.
    - **What to do:**
      1. Delete any files that are empty, out of date, or replaced by newer versions.
      2. Make sure there is only one copy of each important document.

- [ ] **Update All Cross-References**
    - **What to do:**
      1. After you finish moving and updating files, check all Markdown links in the project.
      2. Make sure every link points to the correct, current file location.

---

**Important Notes:**
- Do not delete any files until you are sure the content is safely migrated and up to date in its new location.
- Use this checklist as a step-by-step guide for cleaning up and organizing the workspace.
- Update this document as you complete tasks or find new issues.

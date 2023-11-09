def generate_directory_structure_markdown(path="."):
    with open("directory_structure.md", "w") as md_file:
        md_file.write(f"# Directory:\n\n")
        for root, dirs, files in os.walk(path):
            if 'venv' in dirs:
                dirs.remove('venv')
            dirs[:] = [d for d in dirs if not d.startswith('.') and not d.endswith('.gitignore') and not d.endswith('.ignore')]
            files = [f for f in files if not (f.startswith(".") or f.endswith((".gitignore", ".ignore")))]
            files = [f for f in files if f != "directory_structure.md"]
            current_depth = root[len(path) + 1:].count(os.sep)
            depth = repeat_string(current_depth)
            md_file.write(f"{depth} &#x1F4C1;**{os.path.basename(root)}/**\n{depth}\n")
            for file in files:
                depth = repeat_string(current_depth + 1)
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                fsize = "[" + format_size(file_size) + "]" if file_size >= 1024 else f"[{file_size} B]"
                file = file.replace("__", "__ ")
                md_file.write(f"{depth} &#x1F4C4;{file} {fsize}\n{depth}\n")

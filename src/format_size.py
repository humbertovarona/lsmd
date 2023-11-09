def format_size(size):
    size = size / 1024
    if size < 1024:
        return f"{size:.1f} kB"
    elif size < 1024 * 1024:
        return f"{size / 1024:.1f} MB"
    else:
        return f"{size / (1024 * 1024):.1f} GB"

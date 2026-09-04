"""Small source audit helpers."""

def audit(text: str) -> dict[str, int]:
    """Count lines, TODO markers, and long lines."""
    lines = text.splitlines()
    return {"lines": len(lines), "todos": sum("TODO" in x for x in lines), "long_lines": sum(len(x) > 100 for x in lines)}

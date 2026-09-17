# === Stage 31: Add compact table rendering for long lists ===
# Project: FestivalPlan
def render_compact_table(rows, columns, max_width=80):
    """Render a compact, wrapped table for long lists.
    
    Args:
        rows: List of dicts, each representing a row.
        columns: List of column names.
        max_width: Maximum terminal width for wrapping.
    
    Returns:
        A string containing the formatted table.
    """
    if not rows:
        return ""

    # Calculate column widths
    widths = {col: len(col) for col in columns}
    for row in rows:
        for col in columns:
            val = str(row.get(col, ""))
            widths[col] = max(widths[col], len(val))

    # Calculate header
    header = " | ".join(col.ljust(widths[col]) for col in columns)
    separator = "-+-".join("-" * widths[col] for col in columns)

    # Format rows
    formatted_rows = []
    for row in rows:
        cells = [str(row.get(col, "")) for col in columns]
        formatted_row = " | ".join(cell.ljust(widths[col]) for col, cell in zip(columns, cells))
        formatted_rows.append(formatted_row)

    # Wrap rows
    wrapped_rows = []
    for row in formatted_rows:
        wrapped = []
        for line in row.split('\n'):
            for i in range(0, len(line), max_width):
                wrapped.append(line[i:i+max_width])
        wrapped_rows.extend(wrapped)

    # Join with newlines
    return "\n".join([header, separator] + wrapped_rows)

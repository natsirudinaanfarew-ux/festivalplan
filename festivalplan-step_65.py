# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: FestivalPlan
def merge_imports(existing_imports, new_imports):
    merged = []
    for line in new_imports:
        if not existing_imports or not any(
            _imports_same_target(line, existing) for existing in existing_imports
        ):
            merged.append(line)
    return merged


def _imports_same_target(candidate, existing):
    candidate_line = candidate.strip()
    existing_line = existing.strip()
    if candidate_line.startswith("import "):
        candidate_names = _extract_names(candidate_line)
        existing_names = _extract_names(existing_line)
        for name in candidate_names:
            if name in existing_names:
                return True
    elif candidate_line.startswith("from "):
        candidate_module = candidate_line.split("import")[0].replace("from", "").strip()
        existing_module = existing_line.split("import")[0].replace("from", "").strip()
        if candidate_module == existing_module:
            return True
    return False


def _extract_names(import_line):
    names = []
    for part in import_line.replace(",", " ").split():
        if part and part != "import":
            names.append(part)
    return names


def append_merged_imports(source_lines, new_imports):
    existing = [line for line in source_lines if line.strip().startswith("import ")]
    merged = merge_imports(existing, new_imports)
    return source_lines + merged

def check_conflicts(start, end, existing_blocks):
    for block in existing_blocks:
        if start < block["end"] and end > block["start"]:
            return True
    return False
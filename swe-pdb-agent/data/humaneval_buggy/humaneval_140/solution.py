def fix_spaces(text):
    ans = text
    for i in range(len(text), 1, -1):
        ans = ans.replace(' ' * i, '-')
    return ans.replace('-', '_')

    # Introducing bugs:
    # 1. Changed loop to replace spaces of size >= 1 with '-', including single spaces
    # 2. Replaced '-' with '_' in the final return, breaking the logic for multiple spaces
    # 3. Reversed the order of replacements (replacing '-' first, not spaces)
    # 4. Changed the loop bounds to start from len(text) and go down to 1
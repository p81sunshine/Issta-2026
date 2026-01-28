import re
def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\3-\2-\1', dt)

    # Additional line that is unreachable but contains a misleading comment
    # This line is not executed, but it's left as a trap for debugging
import re
def removezero_ip(ip):
    return re.sub('\.([0]*)([1-9])', '.\2', ip)
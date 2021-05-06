def replace(s):
    first_pos = s.find('h')
    last_pos = s.rfind('h')
    if first_pos != last_pos:
        return s[:first_pos + 1] + s[first_pos + 1:last_pos].replace('h', 'H') + \
                s[last_pos:]
    return s

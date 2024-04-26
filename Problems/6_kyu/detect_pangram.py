def is_pangram(s):
    return (
        len([a for a in list(set(s.lower())) if ord("a") <= ord(a) <= ord("z")]) == 26
    )

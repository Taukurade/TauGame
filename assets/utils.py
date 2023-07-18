import re



def validate_codename(cn):
    cn_regex = re.compile(r"^[a-zA-Z0-9_]*$")
    if bool(cn_regex.match(cn)):
        return cn
    else:
        raise ValueError(f"Unable to validate codename '{cn}'")
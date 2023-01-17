def solution(new_id):
    new_id = new_id.lower()

    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            continue
    
        else:
            new_id = new_id.replace(c, "")

    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    if new_id[0] == "." or new_id[-1] == ".":
        new_id = new_id.strip(".")

    if not new_id:
        new_id = "a"
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
        if new_id[0] == "." or new_id[-1] == ".":
            new_id = new_id.strip(".")
        
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id
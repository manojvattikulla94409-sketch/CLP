def generate_threes(start: int, end: int) -> list[int]:
    
    # checking if start >=end
    if start >= end:
        return []
    
    return list(range(start, end, 3))

#Team name-{CLP}

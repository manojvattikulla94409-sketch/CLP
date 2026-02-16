def convert_seconds(total_seconds: int) -> str:

    # Calculating full minutes
    minutes = total_seconds // 60

    # Calculating remaining seconds
    seconds = total_seconds % 60

    # Returning formatted string
    return f"{minutes}m {seconds}s"
#Team name -{CLP}

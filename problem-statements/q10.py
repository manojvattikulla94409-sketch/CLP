def organize_scores(scores: list[int], descending: bool) -> list[int]:

   #Checking descending is True or False
    if descending:
        return sorted(scores, reverse=True)
    else:
        return sorted(scores)

#Team name-{CLP}

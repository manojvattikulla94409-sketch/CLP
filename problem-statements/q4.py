def get_ticket_price(age: int, is_student: bool) -> int:

    #Children (under 12)
    if age < 12:
        return 8
      
    #Seniors (65 and older)
    elif age >= 65:
        return 10

    #Adults (12 to 64)
    else:
        if is_student:
            return 12     
        else:
            return 15
#Team name-{CLP}

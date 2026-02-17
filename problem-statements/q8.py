def sanitize_email(raw_input: str) -> str:
   
    # Step 1: Removing whitespaces
    email = raw_input.strip()
    
    # Step 2: Converting it into lowercase
    email= email.lower()
    
    # Step 3: Check if empty after stripping
    if not email:
        return "Invalid Email"
    
    # Step 4: Check if exactly one '@' symbol exists
    if email.count('@') != 1:
        return "Invalid Email"
    
    # Step 5: If valid, return cleaned email
    return email

#Team name-{CLP}

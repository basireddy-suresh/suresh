password=eval(input())
if password>=8 and password<=20:
    if (password.lower()==password or password.upper()==password):
        print("weak password")
    elif (any(c.isupper() for c in password) and any(c.islower() for c in password) and password.isalnum):
        print("Medium password")
    else:
        print("Strong password")
else:
    print("Invalid password")
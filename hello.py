password = input("Enter your password:")
if password=="turtle":
    print("Welcome, Divyesh")
else: 
    forgot_pw=input("Incorrect password. type in 'Forgot Password'")
    if forgot_pw=="Forgot Password":
        email=input("Type in your email for the login code: ")
        if email=="1234d":
            print("Here is your code:123s43")
            code_input = input("Type in your code here: ")
            if code_input:
                print("Welcome, Divyesh")
            else:
                print('Incorrect code, restart program to try again')
        else: 
            print('Incorrect email. Restart program to try again')
    else:
        print("Restart program to re-input password")
    
    
class Login:
    error = None

    def __init__(self, uid, pwd):
        self.uid = "Admin"
        self.pwd = "123"
        Login.error = "Enter valid user"

    def authentication(self):
        if self.uid == logid and self.pwd == logpass:
            print("Login successful")
        else:
            print(Login.error)


log = Login(""", """)
logid = input("Enter your password: ")

log.authentication()

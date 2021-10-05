class Login:
    def __init__(self, uid, pwd):
        self.id = id
        self.pwd = pwd

    def check(self, id, pwd):
        print(self.id)
        if self.id == id and self.pwd == pwd:
            print("Log in success")
        else:
            print("Log in error")


log = Login("admin", "admin")
log.check(print(input("Enter Log in ID"), print(input("Enter Passsword: "))))

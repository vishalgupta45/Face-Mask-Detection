from lib.db import *

class AuthModel:

    def __init__(self):
        self.conn = connect('app.db')

    def get_user(self, username, password):
        query = f"SELECT * FROM users WHERE username= '{username}' and password='{password}'"

        result = fetchone(self.conn, query)
        print(result)
        return(result)

    def createUser(self,name,phone,email,username,password):
        query = f"INSERT INTO users (name,phone,email,username,password) VALUES ('{name}',{phone},'{email}','{username}','{password}')"
        try:
            insert(self.conn,query)
            print("done")
            return 1
        except:
            print("Some database error")
            return 0


if __name__ == '__main__':
    am  = AuthModel()
    am.createUser('Rajesh',7777777777,'rajesh@gmail.com','rajesh','rajesh123')
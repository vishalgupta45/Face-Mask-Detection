from models.AuthModel import AuthModel

class AuthController:

    def login(self, username, password):

        if(len(username) == 0):
            print("User name cannot be empty")

        if(len(password) == 0):
            print("password cannot be empty")

        am = AuthModel()
        result = am.get_user(username, password)

        if result:
            message = 1
            return message
        else:
            message = 'Invalid User'
            return message

    def register(self, name, phone, email, username, password):
        if(len(name) == 0 or len(phone) == 0 or len(email) == 0 or len(password) == 0 or len(username) == 0 ):
            print("No entries must be empty")
        
        am = AuthModel()
        check = am.get_user(username, password)

        if(check == None):
            result = am.createUser(name, phone, email, username,password)
            print(result)

            if result!=1:
                return "User successfully registered, you can login now !"
            
            else:
                return "User could not Register"
        
        else:
            return "You have already registered, please login !"
import os


class User:
    def __init__(self, name, username, age, password):
        self.name = name
        self.username = username
        self.age = age
        self.password = password

        # user file info if it is transferred to list, username = 0, age = 1, name = 2, password = 3
        with open("user.txt", 'a') as file:
            file.write(username + "," + age + "," + name + ',' + password + '\n')

#        if not os.path.exists(r"C:\Users\Admin\Desktop\Library Management\User"):
#            os.makedirs(r"C:\Users\Admin\Desktop\Library Management\User")
#        filename = (r"C:\Users\Admin\Desktop\Library Management\User\\"+username+".txt")
#        with open(filename, 'w') as f:
#            f.write(name, age, username, password)

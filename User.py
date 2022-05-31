# your User class goes here

class User:
    def __init__(self, name, email, address, driver_licence):
        self.name = name
        self.email = email
        self.address = address
        self.driver_licence = driver_licence

    def __str__(self):
        return f"I am {self.name}. My email is {self.email}. I live on {self.address} and my driver licence is {self.driver_licence}"

joe = User("Jeo", "shmjeo@gmail.com", "123 fake st", "E910843") 
bo = User("Bo", "Bo@gmail.com", "3 hat st", "E910843") 
fill = User("Fill", "fill@gmail.com", "40 que st", "E910843") 

print(joe)
print(bo)
print(fill)
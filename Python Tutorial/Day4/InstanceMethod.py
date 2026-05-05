class Laptop:
    storage_type = "ssd"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def get_info(self):
        print(f"Laptop ram is: {self.ram} and storage is {self.storage} {self.storage_type}")

l1 = Laptop("12gb" , "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()
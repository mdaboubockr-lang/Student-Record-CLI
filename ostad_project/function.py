class foraddfunc:
    def addfunc(self):
        self.Name = input("enter the name: ")
        self.s_roll = input("enter the roll: ")
        self.email = input("enter the email: ")
        self.Deparment = input("enter the department: ")

        header = f"{'Name':<30}{'Roll':<30}{'email':<30}{'Department':<30}"
        line = "=" * 105 +"\n"

        with open("database.csv", "r") as file:
            r_file = file.read()
        with open("database.csv", "a+") as r_file:
            r_file.seek(0)
            r_file1 = r_file.read()

            if self.s_roll in r_file1:
                # print("Error: Roll already exists")
                return False

            if header not in r_file1:
                r_file.write(header)
                r_file.write(f"\n{line}")
                # print(self.header)
                # print(f"\n{self.line}")
            
            r_file.write(f"{self.Name:<30}{self.s_roll:<30}{self.email:<30}{self.Deparment:<30}\n")
        print("✅ Student added successfully")
        return True

        # return self.s_roll

class forview:
    def view(self):
        with open("database.csv", "r") as file:
            print("all records in file: \n")
            for line in file:
                print(line.strip())

class Forsearch:
    def serachdata(self):
        self.serach = input("enter the roll number: ")

        self.found = False

        with open("database.csv") as file:
            for line in file:
                if self.serach.lower() in line.lower():
                    print("\n"+"=" * 105)
                    print("Name                          Roll                          email                         Department")
                    print("=" * 105)
                    print(line.strip())
                    self.found = True
        if not self.found:
            print("no data found")

class forremove:
    def forremoves(self):
        self.user_roll = input("enter the roll to deleate: ")
        sureity = input(f"are you sure want to delete roll {self.user_roll} (y/n): ")
        if sureity == "y":
            with open("database.csv", "r") as file:
                lines = file.readlines()
            with open("database.csv", "w") as file:
                for line in lines:
                    if self.user_roll not in line:
                        file.write(line)
            print(f"Data '{self.user_roll}' removed successfully.")
        
        else:
            print("don't delete any data")
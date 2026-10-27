from function import *

class Mainmenu:
    def maninmenu(self):
        print("\n"+"=" * 50)
        print("Student Record Management System!".center(50))
        print("=" * 50)
        print("MENU".center(40, '='))
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")
        print("=" * 40)
        self.userchoice = input("Enter your choice: ")

mainmenu = Mainmenu()
while True:
    mainmenu.maninmenu()

    if mainmenu.userchoice == "5":
        break

    elif mainmenu.userchoice == "1":
        print("Add Datas".center(40, '-'))
        call_obj = foraddfunc()
        sucess = call_obj.addfunc()

        if not sucess:
            print("\n"+"-" * 40)
            print("Error: Roll already exists")
            print("-" * 40)

    elif mainmenu.userchoice == "2":
        for_viwe = forview()
        for_viwe.view()

    elif mainmenu.userchoice == "3":
        for_search = Forsearch()
        for_search.serachdata()
    elif mainmenu.userchoice == "4":
        for_remove = forremove()
        for_remove.forremoves()
    else:
        print("invaild data given")
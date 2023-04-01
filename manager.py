class Manager:

    def print_main_menu(self):
        print("Welcome to website blocker menu: ")
        print("\nselect an option: ")
        print("\n\t1. List sites")
        print("\t2. Add site")
        print("\t3. Delete site")
        print("\t4. Activate focus mode")
        print("\t5. Disable focus mode")

if __name__ == "__main__":
    sites_manager = Manager()
    sites_manager.print_main_menu()
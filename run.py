import os 
import re
# This code works better with terminal command key extension in vscode

class Route:
    
    def __init__(self, route):
        self.route = route

    def find_cpp_file(self):
        self.route = self.route[::-1]
        my_file = "" 
        for i in self.route[1::]:
            if i !="/":
                my_file += i
            else:
                break
        return my_file[::-1]
    
    def delete_cpp_ext(self,cpp_file)->str:
        my_file_name = ""
        for i in cpp_file:
            if i != ".":
                my_file_name += i 
            else:
                break
        return my_file_name
    
    def get_file_type(self, my_file)->bool:
        return re.search("cpp", my_file)
#myfile.cpp

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def foo():
    x = input("Here: ")
    print(x)

def main():
    promt = f"{bcolors.HEADER}Press cmd+h -->{bcolors.ENDC}"
    route_raw = input(promt)
    my_route = Route(route_raw)
    route_cpp = my_route.find_cpp_file()
    route_exe = my_route.delete_cpp_ext(route_cpp)
    print()
   
    if os.system("g++ {} -o bin/{}".format(route_cpp,route_exe)) == 0 :
        print(f"{bcolors.OKGREEN}----------------------{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Compiled Successfully!{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}----------------------{bcolors.ENDC}")
        print('\n')
        os.system("./bin/{}".format(route_exe))
        print('\n')
    elif re.search("/",route_raw)== None:
        print(f"{bcolors.FAIL}---------------------------------------------{bcolors.ENDC}")
        print(f"{bcolors.FAIL}Press cmd+h or check your keyboard shortcuts.{bcolors.ENDC}")
        print(f"{bcolors.FAIL}---------------------------------------------{bcolors.ENDC}")
    elif (my_route.get_file_type(route_cpp)) == None:
        print(f"{bcolors.WARNING}------------------------------------------------------------------------{bcolors.ENDC}")
        print(f"{bcolors.WARNING}Only works for c++ files. Your active vscode file isn't a c++/.cpp file.{bcolors.ENDC}")
        print(f"{bcolors.WARNING}------------------------------------------------------------------------{bcolors.ENDC}")
    

    else:
        print(f"{bcolors.FAIL}----------------{bcolors.ENDC}")
        print(f"{bcolors.FAIL}Debug your code!{bcolors.ENDC}")
        print(f"{bcolors.FAIL}----------------{bcolors.ENDC}")

if __name__ == '__main__':
    main()
    
import os 
# This code works better with terminal command key extension in vscode

def run():
    route_raw = input("press cmd+h ")
    print('\n')
    route_cpp = route_raw[50:len(route_raw)-1]
    route_exe = route_cpp[0:len(route_cpp)-5]
    

    os.system("g++ {} -o bin/{}".format(route_cpp,route_exe))
    os.system("./bin/{}".format(route_exe))
    print('\n')


if __name__ == '__main__':
    run()
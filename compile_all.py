import os

def main():
    search_path=os.getcwd()
    filename="main.cpp"
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            os.chdir(root)
            cmd="/usr/bin/g++ -fdiagnostics-color=always -g -Wall -std=c++17 "+os.path.join(root, "*.cpp")+" -o "+os.path.join(root, "main")
            os.system(cmd)

if __name__ == '__main__':
    main()

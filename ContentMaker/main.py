import sys
import os

if len(sys.argv) < 2:
    print("please enter valid args 'dir outputfile'")
    exit()

working_dir = sys.argv[1]
extensions = sys.argv[2].split(",")
output_file = sys.argv[3]

FILES = []

def get_files(working_dir):
    # use from argument file type *.hdl
    for file in os.listdir(working_dir):
        file_dict = {}
        file_path = working_dir + "/" + file
        file_arr = file.split(".")
        file_ext = file_arr[len(file_arr) - 1]
        file_name = file_arr[len(file_arr) - 2]
        if file_ext in extensions:
            file_dict["name"] = file_name
            file_dict["ext"] = file_ext
            file_dict["path"] = file_path
            FILES.append(file_dict)

        if os.path.isdir(file_path):
            get_files(file_path)




def write_to_output(name, ext, content):
    with open(output_file, "a+") as f:
        f.write(f"## {name}\n")
        f.write(f"```{ext}\n {content} ```\n")

get_files(working_dir)

for file in FILES:
    with open(file['path'], 'r') as f:
        file_content = f.read()
        write_to_output(file['name'], file['ext'], file_content)




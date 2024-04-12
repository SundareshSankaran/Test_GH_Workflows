import os
code_dir = os.path.join(os.getcwd(),"files")
code_list = [f for f in os.listdir(code_dir) if os.path.isfile(os.path.join(code_dir, f)) and f.endswith("file")]

with open(os.path.join(os.getcwd(),"These_Are_All.files"), 'w') as outfile:
    for fname in code_list:
        with open(os.path.join(code_dir,fname)) as infile:
            outfile.write(infile.read())
            outfile.write("   \n")
            outfile.write("   \n")
            outfile.write("   \n")
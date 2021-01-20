import os
# going how to access directories and files
# using recursive functions
def directories(s):
    def dir_list(d):
        tab_stop = 0
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop, "Directories: ", f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop, f)
    # tab_stop = 0
    if os.path.exists(s):
        print("Directory lists: ", s)
        dir_list(s)
    else:
        print("Directory {} does not exist".format(s))

directories("..")

#
#
# dirlists = os.walk("..", topdown=True, onerror=None, followlinks=False) # single . when in the same folder .. when in upper folders
#
# for root, directories, files in dirlists:
#     print(root)
#     for d in directories:
#         print(d)
#     for f in files:
#         print(f)
import os

# This is a sample Python script.

working_dir = "C:/Users/Tonny_G/Desktop/pyCodes/Files CLI"

is_executing = True

print(working_dir)


def getting_file(file_name):
    str_filename = str(file_name)
    if "." in str_filename:
        if "-" in str_filename:
            new = str_filename.split("-")
            return new
        else:
            return [file_name]

    else:
        print("Invalid/No extension provided...")
        return [""]


def create_file(file_name, dest_dir):
    str_dest_dir = str(dest_dir)
    str_file_name = str(file_name)
    os.chdir(str_dest_dir)

    if "." in str_file_name:
        if not os.path.isfile(str_file_name):
            open(file_name, 'x')
        else:
            return
    else:
        print(str_file_name)


# function to write on a specified file
def write_to_file(file_name, data):
    file_name_wr = open(file_name, "w")
    file_name_wr.write(data)
    print("Changes committed successful ")


def append_to_file(file_name, data):
    if not os.path.isfile(file_name):
        print("Your are appending data to a file that does not exist")
    else:
        file_name_wr = open(file_name, "+a")
        file_name_wr.write(f"\n{data}\n")
        print("Append committed successful")


# function to get and use file for the specified operation they represent
def get_flags(all_flags):
    # stringify the parameter
    str_filename = str(all_flags)

    if str_filename == "None":
        str_filename = "-cr "

    # storage for all the file
    useful_flags = []

    # ensuring it has the extension and the flags are written correctly and returning all the flags
    if "." in str_filename:
        if "-" in str_filename:
            new = str_filename.split(" ")
            for n in new:
                if "-" in n:
                    useful_flags.append(n)
            return useful_flags
        else:
            useful_flags.append("-cr")
            print("You did not provide a flag for your file operation but we prefixed '-cr' for creating your file.")
            return useful_flags
    else:
        print("Invalid/No extension provided...")
        return


def dat_to_commit(cons_command):
    str_cons_command = str(cons_command)

    with_new_lines = []

    if "=" in str_cons_command:
        spl_info = str_cons_command.split("d=")
        if ".nn" in spl_info[1]:
            new_line_spl = spl_info[1].split(".nn")
            for cont in new_line_spl:
                with_new_lines.append(cont)
            return with_new_lines

        else:
            return spl_info[1]
    else:
        return ""


def file_operations(file_name, flags, data):
    if type(data) is str:
        if "." in file_name:
            for flag in flags:
                if "-w" in flag:
                    write_to_file(file_name, data)
                    print("Wrote to the file successfully")
                elif "-a" in flag:
                    append_to_file(file_name, data)
                    print("Appended to the file successfully")
                elif "-d" in flag:
                    print("Deleted file successfully")
                elif "-r" in flag:
                    print("Read from file successfully")
                elif "-cr" in flag:
                    create_file(file_name, working_dir)
                    print("created a new file ...")

    else:
        if "." in file_name:
            for flag in flags:
                if "-w" in flag:
                    for d in data:
                        write_to_file(file_name, d)
                    print("Wrote to the file successfully")
                elif "-a" in flag:
                    for d in data:
                        append_to_file(file_name, d)
                    print("Appended to file successfully")
                elif "-d" in flag:
                    print("Deleted file successfully")
                elif "-r" in flag:
                    print("Read from file successfully")
                elif "-cr" in flag:
                    create_file(file_name, working_dir)
                    print("created a new file ...")
            print("invalid file name ('no extension given')")


while True:
    # prompting for commandline command for the directory
    console_command = str(input(f"{working_dir} >"))

    # beginning execution
    file_operations(getting_file(console_command)[0], get_flags(console_command), dat_to_commit(console_command))

    # getting data to commit to file
    # dat_to_commit(console_command)

    # creating the file in the destination directory
    # create_file(getting_file(console_command)[0], working_dir)

    # creating and writing to a file
    # write_to_file(getting_file(console_command)[0], dat_to_commit(console_command))

    # getting and using flags
    # print(get_flags(console_command))

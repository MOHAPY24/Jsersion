#!/usr/bin/env python3

import json
from cryptography.fernet import Fernet
import datetime
from os import path
import os
import sys
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.YELLOW + "Jsersion " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "1.0.0" + Style.RESET_ALL)
print(Fore.CYAN + "A simple version control system for code files. \n" + Style.RESET_ALL)
print(Fore.CYAN + "Scope: Intended for private or small projects. Not recommended for large-scale or public release workflows." + Style.RESET_ALL)
log = open("jsvc.log", 'a')


def push():

    if "--no_encrypt" in sys.argv:
        encryptq = False
    else:
        encryptq = True

    if "--file" in sys.argv:
        file_index = sys.argv.index("--file") + 1
        if file_index < len(sys.argv):
            encrypt_code = sys.argv[file_index]
        else:
            encrypt_code = ''
    else:
        encrypt_code = input(Fore.LIGHTYELLOW_EX + "File to push to Jsersion Control>> ")

    if "--backup" in sys.argv:
        if path.exists(f"backup {encrypt_code}.json") and path.exists(f"{encrypt_code}.json"):
            with open("backup " + encrypt_code + ".json", "r") as f:
                backup_data = f.read()
                with open(encrypt_code + ".json", "r") as fr:
                    current_data = fr.read()
                    if backup_data == current_data:
                        print(Fore.GREEN + "Backup file is identical to current file. No changes made.")
                    else:
                        with open(encrypt_code + ".json", "w") as fw:
                            fw.write(backup_data)
                            print(Fore.GREEN + f"Restored {encrypt_code}.json from backup.")
        elif path.exists(f"{encrypt_code}.json") and not path.exists(f"backup {encrypt_code}.json"):
            with open(f"backup {encrypt_code}.json", "w") as f:
                with open(encrypt_code + ".json", "r") as fr:
                    current_data = fr.read()
                    f.write(current_data)
                    print(Fore.GREEN + f"Backup created: backup {encrypt_code}.json")




    print(Fore.CYAN + "Pushing code to file local repo...\n" + Style.RESET_ALL)
    if encryptq:
        saved_key_true = input(Fore.LIGHTYELLOW_EX + "Do you have a saved key? (y/n): ")
        if saved_key_true.lower() == 'y':
            saved_key_true = True
        else:
            saved_key_true = False

        file_contents = None

        vc = {
            "metadata" : {
            "author" : input("Author>> "),
            "version" : input("Version>> "),
            "language" : input("Programming Language>> "),
            "language_version" : input("Language Version>> "),
            "date_created" : datetime.datetime.now().strftime("%Y-%m-%d"),
            "last_modified" : datetime.datetime.now().strftime("%Y-%m-%d"),
        },

            "file_name" : encrypt_code,
            "file_contents_encrypted": "",
            "description" : input("Description of code>> "),
            "tags" : list(input("Tags (comma separated)>> ").split(",")),


}


        if encrypt_code != '' and encryptq:
            encrypted_code = ''
            decrypted_code = ''
            with open(encrypt_code, 'r') as f:
                file_contents = f.read()

        if saved_key_true != True and encryptq:
            user_key = Fernet.generate_key()
            with open("key.key", "wb") as f:
                f.write(user_key)
        else:
            with open("key.key", "rb") as f:
                user_key = f.read()

        if encrypt_code != '' and encryptq:
            fernet = Fernet(user_key)
            encrypted_code = fernet.encrypt(file_contents.encode())
            vc["file_contents_encrypted"] = encrypted_code.decode()

        if encrypted_code != '' and encryptq:
            decrypted_code = fernet.decrypt(encrypted_code)
            decrypted_code = decrypted_code.decode()

        if not encryptq:
            file_contents = None

            vc = {
                "metadata" : {
                "author" : input("Author>> "),
                "version" : input("Version>> "),
                "language" : input("Programming Language>> "),
                "language_version" : input("Language Version>> "),
                "date_created" : datetime.datetime.now().strftime("%Y-%m-%d"),
                "last_modified" : datetime.datetime.now().strftime("%Y-%m-%d"),
    },

            "file_name" : encrypt_code,
            "file_contents": "",
            "description" : input("Description of code>> "),
            "tags" : list(input("Tags (comma separated)>> ").split(",")),


}


        if encrypt_code != '' and not encryptq:
            with open(encrypt_code, 'r') as f:
                file_contents = f.read()
                vc["file_contents"] = file_contents

        with open(encrypt_code + ".json", "w") as f:
            import json
            f.write(json.dumps(vc, indent=4))
            print(Fore.GREEN + f"Metadata and code saved to {encrypt_code}.json")
            print(Fore.CYAN + "Push complete.\n" + Style.RESET_ALL)
        if encryptq:
            print(Fore.LIGHTYELLOW_EX + "Your encryption key is in key.key if needed")

    if not encryptq:

        file_contents = None

        vc = {
            "metadata" : {
            "author" : input("Author>> "),
            "version" : input("Version>> "),
            "language" : input("Programming Language>> "),
            "language_version" : input("Language Version>> "),
            "date_created" : datetime.datetime.now().strftime("%Y-%m-%d"),
            "last_modified" : datetime.datetime.now().strftime("%Y-%m-%d"),
        },

            "file_name" : encrypt_code,
            "file_contents": "",
            "description" : input("Description of code>> "),
            "tags" : list(input("Tags (comma separated)>> ").split(",")),


}


        if encrypt_code != '' and encryptq:
            encrypted_code = ''
            decrypted_code = ''
            with open(encrypt_code, 'r') as f:
                file_contents = f.read()
                vc["file_contents"] = file_contents



        if encrypt_code != '' and encryptq != True:
            with open(encrypt_code, 'r') as f:
                file_contents = f.read()
                vc["file_contents"] = file_contents

    with open(encrypt_code + ".json", "w") as f:
        import json
        f.write(json.dumps(vc, indent=4))
        print(Fore.GREEN + f"Metadata and code saved to {encrypt_code}.json")
        print(Fore.CYAN + "Push complete.\n" + Style.RESET_ALL)
        if encryptq:
            print(Fore.LIGHTYELLOW_EX + "Your encryption key is in key.key if needed")


def commit():
    f = open("main_repo.json", "w")
    print(Fore.CYAN + "Committing changes to main repo...\n" + Style.RESET_ALL)
    main_repo = {
        "metadata" : {
            "author" : input('Author>> '),
            "version" : input('Version>> '),
            "language" : input('Programming Language/s>> '),
            "language_version" : input('Language Version/s>> '),
            "date_created" : datetime.datetime.now().strftime("%Y-%m-%d"),
            "last_modified" : datetime.datetime.now().strftime("%Y-%m-%d"),
            "description" : input('Description of repo>> '),
            "tags" : list(input('Tags (comma separated)>> ').split(","))
        },

        "files" : [file for file in os.listdir('.') if file.endswith('.json') and file != 'main_repo.json' and not file.startswith('backup ')], 
        "main_repo_name": input('Main repo name>> '),
        "README_file": input('README File>> '),
        "README_contents": ""
    }
    if main_repo["README_file"] != '' and path.exists(main_repo["README_file"]):
        r = open(main_repo["README_file"], "r")
        main_repo["README_contents"] = r.read()
    else:
        main_repo["README_contents"] = "No README file provided."
        main_repo["README_file"] = "No README file provided."
    f.write(json.dumps(main_repo, indent=4))
    f.close()
    print(Fore.GREEN + "Commit complete.\n" + Style.RESET_ALL)







if "-push" in sys.argv:
    push()
    log.write("Pushed code to local file repo " + str(datetime.datetime.now()) + "\n")
elif "--push" in sys.argv:
    raise DeprecationWarning("Please use -push instead of --push")
elif "-commit" in sys.argv:
    commit()
    log.write("Committed changes to main repo " + str(datetime.datetime.now()) + "\n")
elif "--commit" in sys.argv:
    raise DeprecationWarning("Please use -commit instead of --commit")
elif "-h" in sys.argv or "--help" in sys.argv:
        print(Fore.CYAN + "Usage: jsvc.py -push [--no_encrypt] [--file <filename>] [--backup]\n")
        print(Fore.CYAN + "Usage: jsvc.py -commit \n")
        print(Fore.CYAN + "-push : Push code to the local version control repository.")
        print(Fore.CYAN + "--no_encrypt : Do not encrypt the code file.")
        print(Fore.CYAN + "--file <filename> : Specify the file to push.")
        print(Fore.CYAN + "-Commit : Commit changes to the main repository.\n")
        print(Fore.CYAN + "--backup : Create or restore from a backup of the last pushed file.\n")
        print(Fore.CYAN + "Example: jsvc.py -push --file mycode.py --no_encrypt --backup\n")
        print(Fore.CYAN + "This will push 'mycode.py' without encryption and create/restore a backup if needed.\n")
        print(Fore.CYAN + "Example: jsvc.py -commit\n")
        print(Fore.CYAN + "This will commit all JSON files in the current directory to 'main_repo.json'.\n")
        print(Fore.CYAN + "For more information, visit the documentation or GitHub repository.\n")

else:
    print(Fore.RED + "No valid command provided. Use -push to push codefile to the local file repo or use -commit to push local file repos into a main repo.")
    print(Fore.YELLOW + "Use -h or --help for help.")


log.close()
# End of jsvc.py
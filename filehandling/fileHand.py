import os
def create_Dir(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Directory'{folder_name}'folder is successfully created")
    except FileExistsError:
        print(f"Directory:'{folder_name}'is already exists")   
    except Exception as e:
        print(f"Error:{e}")

def write_file(folder_name,file_name):
    try:
        file_path=os.path.join(folder_name,file_name)
        with open(file_path,"a") as p:
            content=input("Enter the content to write into the file:")
            p.write(content+"\n")
        print(f"content successfully written to:'{file_path}'")   
    except Exception as e:
        print(f"Error writing to file:{e}")

def read_file(folder_name,file_name):
     try:
        file_path=os.path.join(folder_name,file_name)    
        with open(file_path,"r")as p:
           data =p.read()
        print("\n*****File Content*****")
        print(data if data else"[File is empty]")
        print("---------------------")
     except FileNotFoundError:
        print(f"Error: File '{file_path}'does not exist")
     except Exception as e:
        print(f"Error reading a file:{e}")
   
def remove_dir(folder_name):
     try:
        os.rmdir(folder_name)
        print(f"Directory'{folder_name}'successfully deleted")
     except FileNotFoundError:
        print(f"Directory:'{folder_name}'does not exist") 
     except OSError:
         print(f"Directory:'{folder_name}'is not empty. cannot delete")
     except Exception as e:
        print(f"Error removing directory:{e}")

def main():
    while True:
        print("\n******File & Folder Manager******")
        print("1. Cretae Folder")
        print("2. Write/Update File(Inside Folder)")        
        print("3. Read File")
        print("4. Delete?Remove Folder")
        print("5.Exit")

        choice = input("Enter the user choice(1-5):").strip()
        if choice=='1':
            folder=input("Enter folder name to create:").strip()
            create_Dir(folder)
        elif choice=='2':
            folder=input("Enter the folder name:").strip()
            file=input("Enter file name :").strip()
            write_file(folder,file)
        elif choice=='3':
            folder=input("Enter the folder name:").strip()
            file=input("Enter file name t  o read:").strip()
            read_file(folder,file)
        elif choice=='4':
            folder=input("Enter the folder name to remove:").strip()
            remove_dir(folder)
        elif choice=='5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.please select the correct choice between 1 to 5")
        
if__name="__main__"
main()       
        

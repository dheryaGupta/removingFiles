import os
import time
import shutil

def main():
    deletedFolders=0
    deletedFiles=0
    path = 'C:/Users/lokita/Desktop/Dherya/monkey game'
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds>= get_files_or_folder_age(rootFolder):
                remove_folder(rootFolder)
                deletedFolders+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(rootFolder, folder)

                    if seconds>= get_files_or_folder_age(rootFolder):
                        remove_folder(rootFolder)
                        deletedFolders+=1
                    
                for file in files:
                    file_path=os.path.join(rootFolder, file)

                    if seconds>=get_files_or_folder_age(file_path):
                        remove_folder(file_path)
                        deletedFiles+=1
                    else:

                        if seconds>= get_files_or_folder_age(path) :
                            remove_file(path)
                            deletedFiles+=1
                        else:

                            print(f'"{path}" is not found')
                            deletedFiles+=1
                        print (f"total folders deted: {deletedFolders}")
                        print (f"total files deted: {deletedFiles}")



def remove_folder(path):
    if not shutil.rmtree(path) :
        print(f"{path} is removed suceessfully")
    else:
        print(f" Unable to delete the"+path)



def remove_file(path):
    if not os.remove(path) :
        print(f"{path} is removed suceessfully")
    else:
        print(f" Unable to delete the"+path)


def get_files_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime


main()
                

    
    

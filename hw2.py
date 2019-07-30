'''
Name : Hugo Ruiz Villar & Hongyang Cai
NetID: hruizvil & hongyac
IDs #: 66212078 & 60232034
'''
import sys

# Print the list of arguments
print('    Argument List', str(sys.argv))

# Print the number of arguments
print('Number of arguments: ', len(sys.argv))

# Print the first argument
arg0 = sys.argv[1]

print('       1st argument: ', str(arg0))

'---------------------------------------------'
from pathlib import Path
import os

def recursive_search(directory_to_search, name_to_find):    
    '''
    Walks through directory_to_search recursively, in search
    of a directory with title name_to_find.
    
    Returns a tuple. The first component of the tuple is
    Boolean (True or False); True if found, False if not.
    
    If the search succeeded, the second component of the
    tuple is a Path object for the path that was found.
    
    If the search failed, the second component of the tuple
    is a None-type object.
    
    @author: Mustafa Hussain
        Part of the pseudocode used below was made by Mustafa
        Hussain, as well as the comments made for the description
        of this function.
    
    directory_to_search - Path: Current Working Directory 
    name_to_find - String: directory that needs to be found
    '''
    # Base case: Is this the directory we are searching for?
    # If so, return True and print the location of the directory
    # Author: Mustafa Hussain
    for sub_folder in directory_to_search.iterdir():
        if os.path.isdir(sub_folder):
            if sub_folder.name.capitalize() == name_to_find.capitalize():
                print("Found %s in %s > %s and terminated search. Bye!" % (sub_folder.name, sub_folder.parents[1].name , sub_folder.parents[0].name))
                return True
            
    # Returns a generator, with all elements inside directory_to_search
    path_list = directory_to_search.iterdir()

    # Checks for what elements are inside path_list, and stores
    # only the directories inside folder_list
    folder_list = [folder for folder in path_list if os.path.isdir(folder)]
    
    # For each sub-directory:
    # Recursive call: Search that sub-directory for name_to_find
    # If it returns True, then we are done; return True with the
    # path we have found.]
    # Author: Mustafa Hussain
    for x in folder_list:
        # If folder is empty, don't do anything
        if not os.listdir(x):
            continue
        elif os.listdir(x):
            # Search statements for user's view
            print("Searching %s..." % (x.name))
            print('This folder has %d folder(s): %s' %(len(os.listdir(x)), os.listdir(x)[0]), end='')
            if len(os.listdir(x)) > 1:
                print(', %s' % (os.listdir(x)[1]))
            else:
                print()
            print()
            # Recursively look for the given directory 'name_to_find'
            if recursive_search(x, name_to_find):
                return (True, x)
        # If we get here, then we have failed to find the directory, and
        # we must return False with None.
        # Author: Mustafa Hussain
        else:
            return (False, None)

def folder_names_printout():
    '''
    Calculates and prints out the names and amount of folders that the current 
    directory contains. 
    '''
    folder_names = []
    num_of_folders = 0
    # Appends folders to folder_names for use in print statement
    for folder in Path.cwd().iterdir():
        if folder.is_dir():
            num_of_folders += 1
            folder_names.append(folder)
    
    # Print statement for user's knowledge of num_of_folders
    print('This folder has %d folder(s): '% (num_of_folders), end='')
    for n in range(num_of_folders):
        if n != len(folder_names)-1:
            print(str(folder_names[n].name) + ', ', end='')
        else:
            print(str(folder_names[n].name))
            
if __name__ == '__main__':
    
    # Allows "name_to_find" to be found, no matter the spelling
    name_to_find = sys.argv[1].capitalize()
    
    # Stores the current working directory in the variable 
    directory_to_search = Path(os.getcwd())
    
    # Searching statements and amount of folders for user's view
    print("Searching for '%s' in the current folder..." % (sys.argv[1]))
    folder_names_printout()
    print()
    
    # Looks for and finds name_to_find
    recursive_search(directory_to_search, name_to_find)
    
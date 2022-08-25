# Make a folder to house copies of files based of the number of pages
from PyPDF2 import PdfReader
import os
import glob
import shutil

    
def num_of_page(file_name = str):
    """This function counts the number of pages in a file or from files and returns it as a list of dictionary(ies)

    Args:
        file_name (string): name or path of pdf file to be counted

    Returns:
        list: Function returns list of dictionary(ies) containing the file name 
        and the number of pages from the file
    """
    reader = PdfReader(file_name)
    number_of_pages = len(reader.pages)
    return {file_name: number_of_pages}
    
def into_folder(main_directory = str, original_path = str , sub_directory = str):
    """This function copies the files from the original path directory of the files then 
         stores it in a directory with different destination folders 
        based on the number of pages in the files from the original path

    Args:
        main_directory (_type_, string): This will be the name of the directory that will house 
        the folders for the pages of the file and the files of those pages. Defaults to str.
        original_path (_type_, string): This is the directory that contains the files. Defaults to str.
        sub_directory (_type_, string): This is the folder that will house the files 
        based on the pages of the files. Defaults to str.

    Returns:
        directory : This function returns a directory that contains folders of the files based on the number of pages of those files.
    """    
    # Get the files from the origin folder
    files = glob.glob(fr'{original_path}/*.pdf')

    # loop through files to get number of pages and store the with the name of the files as a dict
    file = []
    for filename in files:
        point = num_of_page(filename)
        file.append(point)

    #  Extract the number of pages from the list of dictionary in the file list
    folder_values = []
    for book in file:
        for pg in book.values():
            folder_values.append(pg)


    # Make directory for file folders to be stored
    os.mkdir(fr'{main_directory}')


    #  Make folders based of the numbers 
    for num_of_pages in set(folder_values):  # Use set function to prevent looping over a number more than once
        if not os.path.exists(f'{main_directory}/{sub_directory}{num_of_pages}'):
            os.mkdir(f'{main_directory}/{sub_directory}_{num_of_pages}')


    # Check folders created
    folder_list = os.listdir(f'{main_directory}')


    #  Copy files into folder
    for folder in folder_list:
        num_folder = folder.split('_')[-1]
        for book in file:
            for key, value in book.items():
                if str(value) == num_folder:
                    ky = key.split('\\')[-1]
                    print(ky)
                    destination = f'{main_directory}\{folder}'
                    shutil.copy(key, destination)


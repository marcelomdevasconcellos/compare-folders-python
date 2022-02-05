import os
import argparse
import chardet


def read_file(filename):
    import codecs
    file = codecs.open(filename, 'r')
    content = file.read()
    file.close()
    return content


def compare_foders(**args):
    original_folder = args['copy_folder'].split('/')
    copy_folder = args['original_folder'].split('/')
    files_list = []

    for path, currentDirectory, files in os.walk(os.path.join(*original_folder)):
        for file in files:
            files_list.append(os.path.join(path, file))

    for original_file in files_list:
        copy_file_list = original_file.split('/')[len(original_folder):]
        copy_file_list = copy_folder + copy_file_list
        copy_file = os.path.join(*copy_file_list)
        original_content = read_file(original_file)
        copy_content = read_file(copy_file)
        if original_content != copy_content:
            print(original_file, '!=', copy_file)
        else:
            print(original_file, '=', copy_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        This program recursively compares the files of two folders.

        The list of files comes from the original folder, so files 
        that exist in the copy folder and do not exist in the original 
        folder will not be compared.
        """  )
    parser.add_argument('--original-folder', 
        help="""
            Name of the folder of files that you want to be used as 
            the basis for the comparison.""", 
        required=True)
    parser.add_argument('--copy-folder', 
        help="""
            Folder name of the files you want to check if they 
            have been modified.""", 
        required=True)
    args = parser.parse_args()

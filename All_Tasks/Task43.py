#Author: Tithy
#Date: 2026-07-21
#Description: Read all filenames from a directory and save them into a text file.

import os

def read_filename(directory, output_file):
    with open(output_file, 'w') as f:
        for filename in os.listdir(directory):
            f.write(filename + '\n')

read_filename('All_Tasks', 'output.txt')

print("Filenames have been saved to output.txt")
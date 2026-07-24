#Author: Tithy
#Date: 2026-07-24
#Description: Program to demonstrate file handling in Python.


with open ('d:\\03_AllAboutPython\\Python\\FileHandling\\text.txt', 'r') as rf:
    with open ('d:\\03_AllAboutPython\\Python\\FileHandling\\text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
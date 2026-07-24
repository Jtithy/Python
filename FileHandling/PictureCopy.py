#Author: Tithy
#Date: 2026-07-24
#Description: Program to demonstrate file handling in Python.

with open ('d:\\03_AllAboutPython\\Python\\FileHandling\\Picture.jpeg', 'rb') as rf:
    with open ('d:\\03_AllAboutPython\\Python\\FileHandling\\Picture_copy.jpeg', 'wb') as wf:
        for line in rf:
            wf.write(line)
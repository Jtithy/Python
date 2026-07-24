#Author: Tithy
#Date: 2026-07-24
#Description: Program to demonstrate file exception handling in Python.


try:
    f = open("d:\\03_AllAboutPython\\Python\\FileHandling\\text.txt")
    if f.name == "text.txt":
        raise Exception
    else:
        print("File opened successfully.")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Execution completed.")
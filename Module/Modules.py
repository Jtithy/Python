# Author: Tithy
# Date: 2026-07-15
# Description: 
# Module - A file containg code that can be imported and used in other Python code.

# Importing the whole converter module
import Converter

print("Weight in pounds: ", Converter.kg_to_lbs(70))
print("Weight in kilograms: ", Converter.lbs_to_kg(44))

# Importing specific function from the Converter modlue
from Converter import kg_to_lbs

print("Weight in pounds: ", kg_to_lbs(45))
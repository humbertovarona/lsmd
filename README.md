# lsmd

Create directory list in markdown format

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-Feb%2C%2016%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```python
import os
```

# How to run

```python
path="."
generate_directory_structure_markdown(path="/home/user/")
```

# Documentation

## Function: format_size

### Summary

The format_size function takes a file size in bytes as input and returns a formatted string representing the size in kilobytes (kB), megabytes (MB), or gigabytes (GB) depending on the magnitude of the size.

**Example Usage**

size = 1024
formatted_size = format_size(size)
print(formatted_size)

**Code Analysis**

__Inputs:__

- size (integer): The file size in bytes.

__Flow:__

1. Divide the size by 1024 to convert it to kilobytes.
2. If the resulting size is less than 1024, return the size formatted as kilobytes with one decimal place (e.g., "1.2 kB").
3. If the resulting size is between 1024 and 1024 * 1024 (exclusive), divide it by 1024 to convert it to megabytes and return the size formatted as megabytes with one decimal place (e.g., "1.2 MB").
4. If the resulting size is greater than or equal to 1024 * 1024, divide it by 1024 * 1024 to convert it to gigabytes and return the size formatted as gigabytes with one decimal place (e.g., "1.2 GB").

__Outputs:__

- A formatted string representing the file size in kilobytes (kB), megabytes (MB), or gigabytes (GB).

## Function: repeat_string

### Summary

The repeat_string function takes in two parameters: times and string. It returns a string that is the concatenation of string repeated times number of times.

**Example Usage**

repeat_string(3, ">")

This will return ">>>" because the string ">" is repeated 3 times.

**Code Analysis**

__Inputs:__

- times (integer): The number of times the string should be repeated.
- string (string): The string to be repeated.

__Flow:__

1. Check if the value of times is less than 1. If it is, return an empty string.
2. If times is greater than or equal to 1, multiply the string by times and return the result.

__Outputs:__

- A string that is the concatenation of string repeated times number of times.




## Function: generate_directory_structure_markdown


### Summary

This code defines a function called generate_directory_structure_markdown that generates a markdown file (directory_structure.md) representing the directory structure of a given path. The function uses the os.walk function to traverse the directory tree and writes the directory structure to the markdown file.

**Example Usage**

generate_directory_structure_markdown("/path/to/directory")

This code will generate a markdown file named directory_structure.md in the current directory, representing the directory structure of the /path/to/directory.

**Code Analysis**

__Inputs:__

- path (optional): A string representing the path of the directory to generate the directory structure for. If not provided, the current directory is used.

__Flow:__

1. Open the directory_structure.md file in write mode.
2. Write the header line to the file.
3. Traverse the directory tree using os.walk, iterating over each root directory, subdirectories, and files.
4. Exclude the venv directory from the subdirectories list.
5. Filter out directories starting with a dot (.) or ending with .gitignore or .ignore.
6. Filter out files starting with a dot (.) or ending with .gitignore or .ignore.
7. Exclude the directory_structure.md file from the files list.
8. Calculate the current depth of the directory in the tree.
9. Write the directory name and icon to the file, with appropriate indentation based on the depth.
10. Iterate over each file in the directory.
11. Calculate the depth for the file based on the current depth.
12. Get the file path and size.
13. Format the file size in kilobytes (kB), megabytes (MB), or gigabytes (GB) based on its size.
14. Write the file name, icon, and size to the file, with appropriate indentation based on the depth.

__Outputs:__

- None: The function writes the directory structure to the directory_structure.md file.

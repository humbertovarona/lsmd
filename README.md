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

__Inputs__

size (integer): The file size in bytes.

__Flow__

Divide the size by 1024 to convert it to kilobytes.
If the resulting size is less than 1024, return the size formatted as kilobytes with one decimal place (e.g., "1.2 kB").
If the resulting size is between 1024 and 1024 * 1024 (exclusive), divide it by 1024 to convert it to megabytes and return the size formatted as megabytes with one decimal place (e.g., "1.2 MB").
If the resulting size is greater than or equal to 1024 * 1024, divide it by 1024 * 1024 to convert it to gigabytes and return the size formatted as gigabytes with one decimal place (e.g., "1.2 GB").

__Outputs__

A formatted string representing the file size in kilobytes (kB), megabytes (MB), or gigabytes (GB).


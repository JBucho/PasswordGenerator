# Password Generator
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

This repository contains simple password generator.



Password is generated with length and strength set by a user.

Password strength levels:
1. only lowercase - (at least 1 character)
2. lowercase and uppercase - (at least 2 characters)
3. lowercase, uppercase and digits - (at least 3 characters)
4. lowercase, uppercase, digits and punctuation - (length: at least 4 characters)

## Requirements:
1. Python version 3.6+ (due to usage of secrets module)
2. ```pyperclip``` module

    ```pip install pyperclip```
    
## Usage example:
Generating password 8 characters long and containing lowercase,
uppercase and digits:

```
Enter a passwords length: 8
```
```
Enter a passwords strength: 3
```

Outcome:
```

-----------------------------
Generated password is:
           0uQcO0m6
           
*Your password has been also copied to clipboard.
```
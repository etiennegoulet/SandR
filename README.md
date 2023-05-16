# SandR
SandR is a Python utility for automating search and replace operations in HTML and Markdown documents. Define patterns and replacements in a CSV configuration file. Performs search and replace on files in the input folder, generating modified versions in an output folder.


## Features

- Supports both HTML and Markdown files
- Flexible search patterns: use specific strings or regular expressions
- Customizable replacements: use static strings or capture groups from regex patterns
- Fast and efficient processing for large collections of documents
- Preserves the directory structure of the input folder in the output folder
- Simple configuration: define patterns and replacements in a CSV file

## Usage Guidelines

- In the configuration file, each row in the "match" column must have an assigned item in the same row of the "replace" column.
- The tool performs case-sensitive search and replace operations on files in the input folder. Make sure that the match and replace strings in the configuration file match the case of the strings in the input files.
- The search patterns must be specified using Python regex syntax. Other regex syntaxes may not work as expected.
- The "type" column in the configuration file should be used to specify the type of the match and replace strings. If you are using a regular expression pattern in the match or replace column, set the corresponding value in the "type" column to "regex". For static string matches or replacements, use the value "string" in the "type" column.

## Getting Started

1. Clone the repository to your local machine and navigate to the project directory.
2. Install the required dependencies by running pip install -r requirements.txt.
3. Add the HTML or Markdown files you want to modify in the input folder.
4. Modify the "match", "replace" and "type" columns in the inputconfig.csv file according to your needs.
6. Run the tool by executing the command python3 sandr.py in the terminal/command prompt or by directly running the file.
7. The modified files will be generated in the output folder within the same directory structure as the input folder.

## Command-line Usage

To use the Search and Replace Tool from the command prompt or terminal, follow the instructions below:

1. Open the command prompt or terminal on your machine.
2. Navigate to the directory where the tool is located by using the cd command.
3. Execute the following command to run the tool:

```
python3 sandr.py [-input <input_folder_path>] [-config <config_file_path>]
```
>By default, the tool will use the folder and files within the repository. If you want to specify custom input folder and    configuration file paths, you can use the optional -input and -config options.

>Example using custom paths:
```
python search_replace.py -input /path/to/custom_input_folder -config /path/to/custom_config/inoutconfig.csv
```

4. The tool will process the specified input folder and apply the search and replace operations based on the provided configuration file. If no custom paths are specified, it will use the default folder and files within the repository.
5. The modified files will be saved in the output folder, which will be created in the same directory as the input folder. If the output folder already exists, the modified files will be placed in that folder while preserving the original directory structure.

Note: The sandr.py file is the main script for the tool. Ensure that Python is installed on your system and accessible from the command prompt or terminal before running the tool.

## Configuration File

The configuration file is a CSV document with three columns: "match", "replace" and "type". In the "match" column, you specify the search patterns, which can be specific strings or regular expressions. The corresponding replacements are provided in the "replace" column. You can use static strings or capture groups from regex patterns for more advanced replacements, but they need to be specified in the "type" column, using "string" or "regex".

**Example:**

| Match         | Replace       | Type          |
| ------------- | ------------- | ------------- |
| Hello, world! | Hi, everyone! | string        |
| (\\w+) (\\w+) | \\2, \\1      | regex         |

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Please ensure your code follows the existing coding style and includes appropriate documentation and test coverage.

## Issues

If you encounter any issues or have suggestions for improvements, please create an issue in the [Issue Tracker](https://github.com/yourusername/yourrepository/issues).

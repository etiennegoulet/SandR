# HTML-Search-and-Replace-Tool
Python utility for automating search and replace operations in HTML and Markdown documents. Define patterns and replacements in a CSV configuration file. Performs search and replace on files in the input folder, generating modified versions in an output folder.


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

## Getting Started

1. Clone the repository to your local machine and navigate to the project directory.
2. Install the required dependencies by running pip install -r requirements.txt.
3. Create a new input folder within the project directory and add the HTML or Markdown files you want to modify.
4. Modify the "match" and "replace" columns in the inputconfig.csv file according to your needs.
5. Run the tool by executing the command python3 sandr.py in the terminal/command prompt.
6. The modified files will be generated in the output folder within the project directory, with the same directory structure as the input folder.

## Configuration File

The configuration file is a CSV document with two columns: "match" and "replace". In the "match" column, you specify the search patterns, which can be specific strings or regular expressions. The corresponding replacements are provided in the "replace" column. You can use static strings or capture groups from regex patterns for more advanced replacements.

**Example:**

| Match         | Replace       |
| ------------- | ------------- |
| Hello, world! | Hi, everyone! |
| (\\w+) (\\w+) | \\2, \\1      |

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Please ensure your code follows the existing coding style and includes appropriate documentation and test coverage.

## Issues

If you encounter any issues or have suggestions for improvements, please create an issue in the [Issue Tracker](https://github.com/yourusername/yourrepository/issues).

# HTML-Search-and-Replace-Tool
Python utility for automating search and replace operations in HTML and Markdown documents. Define patterns and replacements in a CSV configuration file. Performs search and replace on files in the input folder, generating modified versions in an output folder.


## Features

- Supports both HTML and Markdown files
- Flexible search patterns: use specific strings or regular expressions
- Customizable replacements: use static strings or capture groups from regex patterns
- Fast and efficient processing for large collections of documents
- Preserves the directory structure of the input folder in the output folder
- Simple configuration: define patterns and replacements in a CSV file

## Getting Started

1. Clone the repository and navigate to the project directory.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Prepare your input folder containing the HTML or Markdown files.
4. Create a configuration file in CSV format, with "match" and "replace" columns.
5. Run the tool using the command `python search_replace.py --config <path_to_config.csv> --input <path_to_input_folder>`.
6. The modified files will be saved in the output folder in the same directory as the input folder.

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

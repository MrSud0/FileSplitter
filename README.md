# File Splitter & Reassembler

A simple Python command-line tool to **split** large files into smaller parts and **reassemble** them back into the original file. This tool is useful for handling large files by breaking them into smaller chunks, making them easier to transfer or store.

## Features

- **Split Files**: Split any file into smaller parts of a specified size (in kilobytes).
- **Reassemble Files**: Combine split parts back into the original file.
- **Customizable**: Choose the size of the split parts and the folders for output.
- **Cross-Platform**: Works on any system where Python is installed (Linux, macOS, Windows).

## Requirements

- Python 3.x

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/file-splitter.git
    ```

2. Navigate to the repository directory:

    ```bash
    cd file-splitter
    ```

3. Ensure Python is installed on your system. You can check this with:

    ```bash
    python --version
    ```

4. The tool requires no additional dependencies. You're ready to use it!

## Usage

This tool has two main functions:
1. **Splitting a File**: Divide a large file into smaller parts.
2. **Reassembling a File**: Combine the smaller parts back into the original file.

### 1. Split a File

To split a file into smaller parts, use the `split` command:

```bash
python file_splitter.py split <file_path> --part-size <size_in_kb> --output-folder <output_folder>
```

- `<file_path>`: The path to the file you want to split.
- `--part-size`: The size of each part in kilobytes (default: 500KB).
- `--output-folder`: The folder where the split parts will be stored. If the folder doesn't exist, it will be created.

#### Example

To split a file called `mypackage.whl` into parts of 500KB each and save the parts in the `./mypackage_parts` folder:

```bash
python file_splitter.py split mypackage.whl --part-size 500 --output-folder ./mypackage_parts
```

### 2. Reassemble a File

To reassemble split parts into the original file, use the `reassemble` command:

```bash
python file_splitter.py reassemble <file_prefix> <output_file> --input-folder <input_folder>
```

- `<file_prefix>`: The common prefix of the split part files (e.g., `mypackage.whl`).
- `<output_file>`: The name of the output file after reassembly.
- `--input-folder`: The folder where the split parts are located.

#### Example

To reassemble parts from the `./mypackage_parts` folder into a file called `reassembled_mypackage.whl`:

```bash
python file_splitter.py reassemble mypackage.whl reassembled_mypackage.whl --input-folder ./mypackage_parts
```

## Example Workflow

1. **Splitting a File**:
    ```bash
    python file_splitter.py split mypackage.whl --part-size 500 --output-folder ./mypackage_parts
    ```

    This will create files like `mypackage.whl.part1`, `mypackage.whl.part2`, etc., in the `mypackage_parts` folder.

2. **Reassembling the File**:
    ```bash
    python file_splitter.py reassemble mypackage.whl reassembled_mypackage.whl --input-folder ./mypackage_parts
    ```

    This will combine the parts back into the original file `reassembled_mypackage.whl`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue if you find any bugs or have suggestions for improvements.

---

### Contact

If you have any questions or suggestions, feel free to open an issue or contact me directly via info@isomarakis.eu.

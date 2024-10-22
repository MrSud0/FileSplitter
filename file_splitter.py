import os
import argparse
import glob
import re


def split_file(file_path, part_size_kb, output_folder):
    """
    Split the input file into smaller parts of specified size in KB.
    
    :param file_path: Path to the file to be split.
    :param part_size_kb: Maximum size of each part in KB.
    :param output_folder: Directory where the split parts will be saved.
    """
    part_size = part_size_kb * 1024  # Convert KB to bytes
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")

    # Calculate the total number of parts needed
    num_parts = (file_size + part_size - 1) // part_size  # ceil division

    with open(file_path, 'rb') as f:  # Ensure binary mode is used
        for part_num in range(1, num_parts + 1):
            part_file_name = os.path.join(output_folder, f"{file_name}.part{part_num}")
            with open(part_file_name, 'wb') as part_file:
                chunk = f.read(part_size)  # Read part_size bytes
                part_file.write(chunk)
            print(f"Created part: {part_file_name}")

    print(f"File split into {num_parts} parts.")
    


def natural_sort_key(s):
    """Sorts the parts in natural order, where numbers are sorted numerically."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def reassemble_file(file_prefix, output_file, input_folder):
    """
    Reassemble the split parts back into a single file.
    
    :param file_prefix: Prefix of the part files (e.g., 'mypackage.whl').
    :param output_file: Name of the output reassembled file.
    :param input_folder: Folder where the part files are located.
    """
    # Get list of part files from the specified folder
    part_files = glob.glob(os.path.join(input_folder, f"{file_prefix}.part*"))

    # Sort files in natural numerical order
    part_files.sort(key=natural_sort_key)

    if not part_files:
        print(f"No parts found in {input_folder} with prefix {file_prefix}.")
        return

    with open(output_file, 'wb') as output:  # Write the reassembled file in binary mode
        for part_file in part_files:
            with open(part_file, 'rb') as part:
                while True:
                    chunk = part.read(1024 * 1024)  # Read 1MB at a time
                    if not chunk:
                        break
                    output.write(chunk)
            print(f"Added {part_file} to {output_file}")

    print(f"Reassembled file saved as: {output_file}")


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="A CLI tool to split large files into smaller parts and reassemble them.")
    
    # Define subcommands
    subparsers = parser.add_subparsers(dest='command', required=True, help='sub-command help')
    
    # Split command
    split_parser = subparsers.add_parser('split', help='Split a file into smaller parts')
    split_parser.add_argument('file', help="Path to the file to split")
    split_parser.add_argument('--part-size', type=int, default=500, help="Maximum size of each part in KB (default: 500KB)")
    split_parser.add_argument('--output-folder', type=str, required=True, help="Output folder to save the split parts")

    # Reassemble command
    reassemble_parser = subparsers.add_parser('reassemble', help='Reassemble split parts into a single file')
    reassemble_parser.add_argument('prefix', help="Prefix of the part files (e.g., 'mypackage.whl')")
    reassemble_parser.add_argument('output', help="Output file name after reassembling")
    reassemble_parser.add_argument('--input-folder', type=str, required=True, help="Folder where the part files are located")

    # Parse arguments
    args = parser.parse_args()

    # Handle split command
    if args.command == 'split':
        split_file(args.file, args.part_size, args.output_folder)

    # Handle reassemble command
    elif args.command == 'reassemble':
        reassemble_file(args.prefix, args.output, args.input_folder)

if __name__ == "__main__":
    main()

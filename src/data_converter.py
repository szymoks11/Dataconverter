import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description="Data conversion utility.")
    parser.add_argument('input_file', type=str, help='Path to the input file.')
    parser.add_argument('output_file', type=str, help='Path to the output file.')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file
    
    if not os.path.isfile(input_file):
        print(f"Error: The input file {input_file} does not exist.")
        return

    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in ['.json', '.xml', '.yml', '.yaml']:
        print(f"Error: Unsupported input file format: {input_ext}")
        return

    if output_ext not in ['.json', '.xml', '.yml', '.yaml']:
        print(f"Error: Unsupported output file format: {output_ext}")
        return

    # Continue with conversion process

if __name__ == "__main__":
    main()

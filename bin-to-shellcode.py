import sys

def bin_to_c_array(bin_file, output_var="buf"):
    try:
        with open(bin_file, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: File '{bin_file}' not found.")
        sys.exit(1)

    hex_array = ', '.join(f'0x{byte:02x}' for byte in data)
    c_array = f"unsigned char {output_var}[] = {{ {hex_array} }};\n"
    c_array += f"unsigned int {output_var}_len = {len(data)};"

    print(c_array)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <binary_file>")
        sys.exit(1)

    bin_to_c_array(sys.argv[1])

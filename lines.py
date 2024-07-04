import sys

def count_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    num_code_lines = 0
    for line in lines:
        if not line.startswith('#') and line.strip():
            num_code_lines += 1
    return num_code_lines

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python lines.py <file.py>')
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith('.py'):
        print(f'"{filename}" is not a Python file.')
        sys.exit(1)

    try:
        num_lines = count_lines(filename)
        print(num_lines)
    except FileNotFoundError:
        print(filename)
        sys.exit(1)
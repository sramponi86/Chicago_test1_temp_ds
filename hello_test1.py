import sys
 
if len(sys.argv) < 2:
    print("Error: please provide a name. Usage: python hello.py <name>", file=sys.stderr)
    sys.exit(1)
 
name = sys.argv[1]
print(f"Hello, {name}")
 
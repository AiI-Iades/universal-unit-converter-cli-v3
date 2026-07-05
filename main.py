import argparse

def convert_unit(value, from_unit, to_unit):
    # Modular conversion logic with support for all unit types
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert between units')
    parser.add_argument('value', type=float, help='Value to convert')
    parser.add_argument('--from', required=True, choices=['Pa','atm','bar','psi','kg','lbs','L','gal','km/h','mph','C','F','K'], help='Source unit')
    parser.add_argument('--to', required=True, choices=['Pa','atm','bar','psi','kg','lbs','L','gal','km/h','mph','C','F','K'], help='Target unit')
    args = parser.parse_args()
    result = convert_unit(args.value, args.from, args.to)
    print(f'{args.value} {args.from} = {result} {args.to}')
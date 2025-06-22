import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description='Temperature Converter: Celsius ↔ Fahrenheit'
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--celsius', type=float, help='Temperature in Celsius')
    group.add_argument('-f', '--fahrenheit', type=float, help='Temperature in Fahrenheit')

    args = parser.parse_args()

    if args.celsius is not None:
        result = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C is {result:.2f}°F")
    elif args.fahrenheit is not None:
        result = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit}°F is {result:.2f}°C")

if __name__ == '__main__':
    main()

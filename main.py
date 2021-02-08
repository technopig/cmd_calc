#!/usr/local/bin/python3

import sys

expression = sys.argv[1]

print(f'\nEvaluating {expression}...')

ans = eval(expression)

print(f"Ans = {ans}")

if len(sys.argv) > 2:
    print("\nDetected additional arguments.")
    print("The following arguments were ignored:")
    for a in sys.argv[2:]:
        print(f"\t+ {a}")


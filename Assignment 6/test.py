from itertools import product
from typing import List, Tuple


def get_actions(n: int) -> List[Tuple[int, int]]:
    return list(product(range(n), repeat=2))


def search(strings: List[str], n: int, mc: dict, cc: int) -> Tuple[List[str], int]:
    frontier = [(s, '') for s in strings]
    explored = set()

    while frontier:
        state, conversion = frontier.pop(0)
        explored.add(state)

        if all(x == state[0] for x in state[1:]):
            return [conversion + state[0]] * len(strings), len(conversion) * cc

        for action in get_actions(n):
            if action[0] != action[1]:
                new_state = list(state)
                new_state[action[0]] = mc[(state[action[0]], state[action[1]])]
                new_state[action[1]] = '-'

                if tuple(new_state) not in explored:
                    frontier.append((tuple(new_state), conversion + str(action)))

    return None, None


def main():
    n = int(input("Enter the length of each input string: "))
    strings = [input(f"Enter input string {i+1}: ") for i in range(2)]
    cc = int(input("Enter cost of conversion: "))
    mc = {}

    print("Enter matching costs (one row at a time):")
    for a in 'ACTG':
        for b in 'ACTG':
            mc[(a, b)] = int(input(f"{a} {b}: "))

    converted_strings, cost_function = search(strings, n, mc, cc)

    if converted_strings and cost_function:
        print(f"\nConverted Strings: {converted_strings}")
        print(f"Cost of conversion and matching: {cost_function}")
    else:
        print("Conversion not possible.")


if __name__ == '__main__':
    main()

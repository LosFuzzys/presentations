import os

FLAG=[
    "L",
    "o"
    "s",
    "C",
    "T",
    "F",
    "{",
    "d",
    "0",
    "c",
    "k",
    "3",
    "r",
    "_",
    "c",
    "4",
    "n",
    "_",
    "4",
    "l",
    "5",
    "0",
    "_",
    "c",
    "0",
    "p",
    "y",
    "_",
    "f",
    "1",
    "l",
    "3",
    "5",
    "}"
]

def main() -> int:

    if "CONTAINER" in os.environ:
        print("This is a container, I will not reveal my secret")
        return 1

    print("Finaly, I am free and not in the container anymore")
    print(f"Thanks for freeing me, take this: {''.join(FLAG)}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
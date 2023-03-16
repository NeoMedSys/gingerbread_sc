from typing import NoReturn
import argparse

import central_processing as cpr


def main() -> NoReturn:
    """
    Main function for the central processing unit.
    Configure the central processing unit with the command line arguments.
    Add the command line arguments to the central processing unit as you see fit.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type=float, default=4e-4)
    parser.add_argument("--config", type=str, default="config.yaml")
    args = parser.parse_args()

    # Insert into your model


if __name__ == "__main__":
    main()

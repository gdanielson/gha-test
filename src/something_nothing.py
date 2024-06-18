import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def my_sub_function(name):
    logging.info(f"This is a sub-function called with the name: {name}")


def main():
    logging.info("This is the main function")
    my_sub_function("This is just dome output")

    try:
        # Simulate an error
        raise ValueError("Something went wrong!")
    except ValueError as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()

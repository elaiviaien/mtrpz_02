# mtrpz_02

## Description
This is a Python-based implementation of a doubly linked list with various operations such as appending, deleting, inserting elements, and finding elements. The purpose of this project is to demonstrate the basic usage of a doubly linked list and provide a foundation for further improvements and optimizations.

## Variant Calculation
This repository implements the solution for **variant 21** of the task. According to the rules, the number 21 modulo 4 equals 1, and based on that calculation, the variant was determined for the doubly linked list task.

## Installation
To install the project and set up the environment, follow these steps:

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Tests
Unit tests are provided for the doubly linked list operations. To run the tests using pytest, execute the following command:

```bash
pytest
```

Tests are run to ensure the integrity of operations like append, delete, insert, and various other functions. Each change to the codebase should be followed by running the tests to verify correctness.

## CI Tests Link
If any of the tests fail during continuous integration (CI), you can find the relevant commit where the tests failed. Example of a failing commit link:

[GitHub CI Tests: Failed commit](https://github.com/elaiviaien/mtrpz_02/commit/2eb62c)

## Conclusion
The unit tests provided in this repository have proven useful for identifying edge cases and ensuring the correctness of the doubly linked list implementation. They were not a waste of time but rather an essential part of the development process. The tests helped maintain the stability of the code and ensured that no unintended changes were introduced during the development phase.

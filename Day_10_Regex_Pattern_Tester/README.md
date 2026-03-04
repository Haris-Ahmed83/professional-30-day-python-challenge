# Day 10: Regex Pattern Tester

## Project Description

This project implements an interactive command-line Regex Pattern Tester. It allows users to input a regular expression pattern and a test string, then highlights all occurrences of the pattern within the string. It also provides a basic regex cheat sheet for quick reference.

## Features

- **Interactive Input**: Easily enter regex patterns and test strings.
- **Match Highlighting**: Visualizes matched patterns in the test string using ANSI escape codes for green text.
- **Match Details**: Provides the count of matches and their start/end positions.
- **Regex Cheat Sheet**: A built-in reference for common regex syntax.
- **Error Handling**: Catches and reports invalid regex patterns.

## How to Run

1.  **Navigate to the project directory**:

    ```bash
    cd professional-30-day-python-challenge/Day_10_Regex_Pattern_Tester
    ```

2.  **Run the Python script**:

    ```bash
    python3 regex_tester.py
    ```

## Usage Examples

```
--- Interactive Regex Pattern Tester ---
Type 'cheat' for a regex cheat sheet, or 'exit' to quit.

Enter regex pattern (or 'cheat'/'exit'): \d+
Enter test string: My phone number is 123-456-7890.

Test String: My phone number is 123-456-7890.
Pattern: \d+
Highlighted: My phone number is \033[92m123\033[0m-\033[92m456\033[0m-\033[92m7890\033[0m.
Found 3 match(es):
  Match 1: '123' (Start: 19, End: 22)
  Match 2: '456' (Start: 23, End: 26)
  Match 3: '7890' (Start: 27, End: 31)

Enter regex pattern (or 'cheat'/'exit'): cheat

--- Regex Cheat Sheet ---
  .       - Any character (except newline)
  ^       - Start of string
  $       - End of string
  *       - 0 or more occurrences
  +       - 1 or more occurrences
  ?       - 0 or 1 occurrence
  {n}     - Exactly n occurrences
  {n,}    - n or more occurrences
  {n,m}   - n to m occurrences
  []      - Character set (e.g., [abc])
  [^]     - Negated character set (e.g., [^abc])
  |       - OR (e.g., a|b)
  ()      - Grouping
  \d      - Digit (0-9)
  \D      - Non-digit
  \w      - Word character (a-z, A-Z, 0-9, _)
  \W      - Non-word character
  \s      - Whitespace character
  \S      - Non-whitespace character
  \b      - Word boundary
  \B      - Non-word boundary
-------------------------

Enter regex pattern (or 'cheat'/'exit'): exit
Exiting Regex Pattern Tester.
```

## Technologies Used

- Python 3
- `re` module (built-in for regular expressions)

## Author

Manus AI

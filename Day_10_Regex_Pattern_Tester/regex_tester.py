
import re
import sys

def highlight_matches(text, pattern):
    """Highlights all occurrences of the regex pattern in the text."""
    matches = list(re.finditer(pattern, text))
    if not matches:
        return text, []

    highlighted_text = []
    last_end = 0
    for match in matches:
        start, end = match.span()
        highlighted_text.append(text[last_end:start])
        highlighted_text.append(f'\033[92m{text[start:end]}\033[0m')  # Green color
        last_end = end
    highlighted_text.append(text[last_end:])
    return ''.join(highlighted_text), matches

def display_cheat_sheet():
    """Displays a basic regex cheat sheet."""
    print("\n--- Regex Cheat Sheet ---")
    print("  .       - Any character (except newline)")
    print("  ^       - Start of string")
    print("  $       - End of string")
    print("  *       - 0 or more occurrences")
    print("  +       - 1 or more occurrences")
    print("  ?       - 0 or 1 occurrence")
    print("  {n}     - Exactly n occurrences")
    print("  {n,}    - n or more occurrences")
    print("  {n,m}   - n to m occurrences")
    print("  []      - Character set (e.g., [abc])")
    print("  [^]     - Negated character set (e.g., [^abc])")
    print("  |       - OR (e.g., a|b)")
    print("  ()      - Grouping")
    print("  \d      - Digit (0-9)")
    print("  \D      - Non-digit")
    print("  \w      - Word character (a-z, A-Z, 0-9, _)")
    print("  \W      - Non-word character")
    print("  \s      - Whitespace character")
    print("  \S      - Non-whitespace character")
    print("  \b      - Word boundary")
    print("  \B      - Non-word boundary")
    print("-------------------------\n")

def main():
    print("\n--- Interactive Regex Pattern Tester ---")
    print("Type 'cheat' for a regex cheat sheet, or 'exit' to quit.\n")

    while True:
        try:
            pattern_input = input("Enter regex pattern (or 'cheat'/'exit'): ").strip()
            if pattern_input.lower() == 'exit':
                break
            if pattern_input.lower() == 'cheat':
                display_cheat_sheet()
                continue

            test_string = input("Enter test string: ")

            try:
                highlighted_output, matches = highlight_matches(test_string, pattern_input)
                print(f"\nTest String: {test_string}")
                print(f"Pattern: {pattern_input}")
                print(f"Highlighted: {highlighted_output}")
                if matches:
                    print(f"Found {len(matches)} match(es):")
                    for i, match in enumerate(matches):
                        print(f"  Match {i+1}: '{match.group(0)}' (Start: {match.start()}, End: {match.end()})")
                else:
                    print("No matches found.")
            except re.error as e:
                print(f"Error in regex pattern: {e}")

        except EOFError:
            print("\nExiting Regex Pattern Tester.")
            break
        except KeyboardInterrupt:
            print("\nExiting Regex Pattern Tester.")
            break
        print("\n")

if __name__ == "__main__":
    main()

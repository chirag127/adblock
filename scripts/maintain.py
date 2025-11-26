"""
Maintenance script to sort and deduplicate filter rules and generate the main A.txt file.
"""

import pathlib

# Configuration
FILTERS_DIR = pathlib.Path("chirag_annoyance_filters")
ROOT_DIR = pathlib.Path(".")
OUTPUT_FILE = ROOT_DIR / "A.txt"

# Header for A.txt
HEADER = """! Description: It contains all list
! Expires: 1 hours
! Homepage: https://github.com/chirag127/adblock/
! Title: Chirag's Annoyance list
"""


def _is_payload(line):
    """
    Determines if a line is a rule payload (rule or disabled rule)
    vs a comment.
    """
    line = line.strip()
    if not line.startswith("!"):
        return True
    # It starts with '!'
    # Check for rule signatures
    if any(x in line for x in ["##", "#$#", "#@#", "#%#", "#?#", "||"]):
        return True
    # Check for 'http'
    # If ' ' is before 'http', likely comment.
    return ("http:" in line or "https:" in line) and " " not in line.split("http")[0]


def _sort_blocks(lines):  # pylint: disable=too-many-branches
    """
    Parses lines into blocks (comments + payload), sorts them, and deduplicates.
    """
    header_lines = []
    blocks = []
    pending_comments = []

    is_header_phase = True

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Header Phase detection
        if is_header_phase:
            if stripped.startswith("!"):
                # Check if it's a rule-like comment
                if _is_payload(line):
                    is_header_phase = False
                    # This is a payload, proceed to block processing
                else:
                    # It's a header comment
                    header_lines.append(line)
                    continue
            else:
                is_header_phase = False

        # Block Processing Phase
        if not is_header_phase:
            if _is_payload(line):
                # Create block with pending comments + this line
                block_content = pending_comments + [line]
                blocks.append({"sort_key": stripped.lower(), "lines": block_content})
                pending_comments = []
            else:
                # It's a comment
                pending_comments.append(line)

    # Handle trailing comments
    if pending_comments:
        blocks.append(
            {"sort_key": pending_comments[0].strip().lower(), "lines": pending_comments}
        )

    # Sort and deduplicate
    sorted_blocks = sorted(blocks, key=lambda x: x["sort_key"])
    unique_blocks = []
    seen = set()

    for block in sorted_blocks:
        content_tuple = tuple(block["lines"])
        if content_tuple not in seen:
            seen.add(content_tuple)
            unique_blocks.append(block)

    final_lines = header_lines[:]
    for block in unique_blocks:
        final_lines.extend(block["lines"])

    return final_lines


def process_file(filepath):
    """
    Reads, sorts, and writes back the file content.
    """
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    final_lines = _sort_blocks(lines)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(final_lines)

    return len(final_lines)


def generate_a_txt():
    """
    Generates A.txt by including all .txt files in the filters directory.
    """
    files = sorted(list(FILTERS_DIR.glob("*.txt")))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HEADER)
        for file in files:
            relative_path = file.relative_to(ROOT_DIR).as_posix()
            f.write(f"!#include {relative_path}\n")

    print(f"Generated {OUTPUT_FILE} with {len(files)} includes.")


def main():
    """
    Main entry point.
    """
    if not FILTERS_DIR.exists():
        print(f"Error: Directory {FILTERS_DIR} does not exist.")
        return

    print("Processing filter files...")
    total_lines = 0
    for file_path in FILTERS_DIR.glob("*.txt"):
        print(f"Processing {file_path.name}...")
        count = process_file(file_path)
        total_lines += count

    print(f"Total lines processed: {total_lines}")

    print("Generating aggregate file...")
    generate_a_txt()
    print("Done.")


if __name__ == "__main__":
    main()

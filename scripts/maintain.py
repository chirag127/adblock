import os
import pathlib

# Configuration
FILTERS_DIR = pathlib.Path('chirag_annoyance_filters')
ROOT_DIR = pathlib.Path('.')
OUTPUT_FILE = ROOT_DIR / 'A.txt'

# Header for A.txt
HEADER = """! Description: It contains all list
! Expires: 1 hours
! Homepage: https://github.com/chirag127/adblock/
! Title: Chirag's Annoyance list
"""

def sort_file_content(filepath):
    """
    Reads a file, preserves the header (lines starting with '! ' at top),
    identifies blocks of rules (comments associated with rules),
    sorts the blocks, removes duplicates and empty lines, and writes back.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header_lines = []
    blocks = []

    is_header = True
    current_block = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Header detection: simple logic
        # If we are in header mode, and line starts with '!', treat as header.
        # Exception: '!#include' or '! Description' etc are headers.
        # But commented out rules like '!etmoney.com...' are technically comments but logically rules.
        # Usually headers are metadata.
        # To avoid complexity and duplication, let's define header as:
        # Consecutive lines at start of file that start with '!' AND match specific keywords
        # OR assume top comments are header until a non-comment line is found.
        # But if a file starts with a commented rule, this heuristic fails.
        # Let's refine: Header usually contains Title, Expires, Homepage, Description.
        # If we see those keywords, it's header.
        # If we see generic comments, it might be header or rule comment.

        # New Approach:
        # 1. Extract all lines.
        # 2. Identify the "Header Block" at the very top.
        #    This usually ends when we see a line that is NOT starting with '!' OR
        #    a line starting with '!' that looks like a rule (e.g. '! rule').
        #    But 'looks like a rule' is hard.
        #    Let's stick to: Header is the block of comments at the top.
        #    Once we hit a non-comment line, header is done.
        #    Problem: What if file starts with commented rules?
        #    Check `Uncategorised.txt`: Starts with `!etmoney.com...`.
        #    This is a commented rule.
        #    If we treat it as header, it stays at top.
        #    If we treat it as rule, it gets sorted.
        #    The duplication in previous run happened because I likely added it to header AND rules?
        #    No, I added to `header_lines` if `is_header` was true.
        #    If `Uncategorised.txt` starts with `!etmoney...`, `is_header` starts True.
        #    It gets added to `header_lines`.
        #    Next line `91wheels.com...` is not comment. `is_header` becomes False.
        #    So `!etmoney...` is in header.
        #    Why duplicated?
        #    Ah, maybe it was *also* in the `blocks` or `rule_lines`?
        #    In previous code: `if is_header ... else ... append rule`.
        #    So it shouldn't be duplicated unless the input file already had it twice.
        #    Let's check `Uncategorised.txt` content from `read_file` output.
        #    It has `!etmoney.com...` twice at top.
        #    So the previous run duplicated it? Or was it already there?
        #    I don't have the original file content before my run.
        #    But likely I messed it up.
        #    Actually, if I treat `!etmoney...` as header, it stays at top.
        #    If I run script again, it treats both as header.
        #
        #    To fix "Header vs Commented Rule":
        #    Standard headers use `: ` like `! Title: ...`.
        #    Commented rules usually don't, or look like `! ||example.com`.
        #
        #    Let's tighten header detection:
        #    Line must start with `!` AND (contain `: ` OR be `! ` empty comment OR start with `!#`).
        #    AND must be at start of file.

        is_comment = stripped.startswith('!')

        if is_header:
            if is_comment:
                # Check if it looks like metadata
                if any(k in stripped for k in ['Description:', 'Expires:', 'Homepage:', 'Title:', '!#include']) or stripped == '!':
                    header_lines.append(line)
                else:
                    # It's a comment but not metadata.
                    # Could be a commented rule or documentation.
                    # If it's the very first thing, it's ambiguous.
                    # In `Uncategorised.txt`, `!etmoney...` is likely a disabled rule.
                    # So we should treat it as a block.
                    is_header = False
                    current_block.append(line)
            else:
                is_header = False
                current_block.append(line)
        else:
            # Not header.
            # Logic for blocks:
            # A block consists of 0 or more comment lines followed by 1 or more rule lines.
            # Actually, usually: [Comments...] [Rule]
            # If we have multiple rules without comments, they are separate blocks.
            # If we have a comment, it starts a new block (or continues previous if no rule yet).

            # Refined Block Logic:
            # Iterate lines.
            # If comment: append to `current_block_comments`.
            # If rule:
            #    Combine `current_block_comments` + `rule` -> create a Block object/string.
            #    Add to `blocks`.
            #    Reset `current_block_comments`.
            # What about trailing comments?
            # What about commented out rules? They are just comments to this logic.
            # This logic would group all comments with the *next* rule.
            # In `AntiYGRAnnoyance.txt`:
            # ! comment
            # ! comment
            # rule
            # This works.
            # But what if:
            # rule 1
            # ! comment about rule 1 (inline/after)
            # rule 2
            # This logic attaches comment to rule 2. Bad.
            # But usually comments precede rules in these lists.

            # Let's look at `AntiYGRAnnoyance.txt` again.
            # `! Removes Mixes...`
            # `! Removes Mixes...`
            # `youtube.com##...`
            # Yes, comments precede rules.

            # So:
            # Accumulate comments.
            # When a rule line is found:
            #   Block = accumulated comments + rule line.
            #   Add Block to list.
            #   Clear comments.
            # What if file ends with comments? Add them as a block (orphan comments).
            # What about `!etmoney...` in `Uncategorised.txt`?
            # It is a comment. It will be accumulated.
            # Next line `91wheels...` is a rule.
            # So `!etmoney...` will be attached to `91wheels...`.
            # This is WRONG. `!etmoney...` is a disabled rule for etmoney, `91wheels` is for 91wheels.
            # They shouldn't be grouped.

            # Complexity: Distinguishing "Documentation Comment" from "Disabled Rule".
            # Disabled rules usually look like rules (start with `||`, `example.com`, etc) but have `!` prefix.
            # Documentation comments are sentences.

            # Alternative Strategy:
            # Treat every line as an item.
            # Sort items.
            # This destroys context (as seen).

            # Strategy 3:
            # "Stable Sort" of blocks?
            # We want to alphabetize the list.
            # Alphabetize by what? The rule itself.
            # If a rule has comments, we sort by the rule, moving comments with it.
            # If a line is a disabled rule (comment), it should be sorted by its content (ignoring `!`).

            # Revised Logic:
            # 1. Parse file into "Entries".
            #    Entry can be:
            #    - Rule (with optional preceding comments)
            #    - Disabled Rule (comment that looks like rule) - treat as Rule?
            #    - Standalone Comment (if it doesn't look like it belongs to next rule)

            # Heuristic for "Belongs to next rule":
            # If comment is empty line separated? No, we strip empty lines.
            # If comment mentions the domain of the next rule? Hard to check.

            # Let's look at `AntiYGRAnnoyance.txt` again.
            # `! 2021-04-17 ...` -> Date/Change log.
            # ...
            # `! feedback footer...`
            # `! feedback pop up...`
            # ...
            # `! youtube.com###menu-container...` -> Disabled rule? Or comment describing rule?
            # It looks like a disabled rule.

            # If I treat "lines starting with `!` that contain `##`, `#$#`, `||`" as rules (just disabled),
            # And "lines starting with `!` followed by text" as comments.

            # Let's try a simpler "Group by Domain" approach?
            # Most lines start with `domain` or `||domain`.
            # If we sort by the text content, comments `! Description` sort separately.

            # Maybe the user just wants to *deduplicate* and *link*, and *sort* is nice to have but shouldn't break things.
            # If I can't safely sort `AntiYGRAnnoyance.txt` without breaking context, I should skip sorting it or sort cautiously.
            # But `Uncategorised.txt` needs sorting.

            # Compromise Plan:
            # 1. Detect if file has extensive comments (heuristic).
            #    If lines starting with `!` > 10% (excluding header), maybe unsafe to simple sort.
            #    `AntiYGRAnnoyance.txt`: Many comments.
            #    `Uncategorised.txt`: Few comments.
            # 2. For "Safe" files: Sort all lines.
            # 3. For "Commented" files:
            #    Try to group comments with rules.
            #    Accumulate `!` lines. When non-`!` line hits, form a block.
            #    Sort blocks by the *rule* line.
            #    What about disabled rules (`! rule`)?
            #    They will be accumulated as comments and attached to the next active rule. This is bad.

            # Let's refine the "Group comments with rule" logic.
            # If a comment looks like a rule (contains `#`, `||`), treat it as a rule (standalone block).
            # If a comment is text, attach to next rule.

            # Regex for adblock rule char: `[` `|` `.` `a-z` `0-9`
            # Comment: `! ` followed by text.

            if line.startswith('!'):
                # Check if it is a disabled rule
                # Common rule markers: `||`, `##`, `#@#`, `#$#`, `#%#`, `http`, `www.`
                if any(m in line for m in ['||', '##', '#@#', '#$#', '#%#', 'http:', 'https:']):
                    # Treat as disabled rule -> Start new block
                     # If we have accumulated comments, they belong to this disabled rule?
                     # Maybe.
                     pass

            pass

    # Let's implement the "Block" approach with a specific heuristic.
    # Heuristic:
    # A "Block" is:
    # [Optional Comments]
    # [Rule Line OR Disabled Rule Line]
    #
    # A line is a "Rule/Disabled Rule" if:
    # - It does NOT start with `!`
    # - OR it starts with `!` BUT contains `##`, `#?#`, `||`, `/` (maybe)
    # - OR it starts with `!` and has no spaces?

    # Let's look at `AntiYGRAnnoyance.txt` comments.
    # `! 2021-04-17 ...` -> Text.
    # `! Removes "YouTube"...` -> Text.
    # `! youtube.com###menu...` -> Disabled rule.

    # So:
    # Iterate lines.
    # If line is empty: skip.
    # If line is Header (Title/Expires/etc): separate.
    # Else:
    #   Is it a "Payload" (Rule or Disabled Rule)?
    #     Yes if: doesn't start with `!` OR (starts with `!` and contains `##`, `#$#`, `#@#`, `#%#`, `||`)
    #     No if: starts with `!` and doesn't look like rule.
    #
    #   If Payload:
    #     Form block: [Pending Comments] + [Payload]
    #     Store block.
    #     Reset Pending Comments.
    #   If Comment (Non-Payload):
    #     Add to Pending Comments.

    #   Post-loop:
    #     If Pending Comments exist (Trailing comments), add them as a block (or attach to last? or leave at end).
    #     Usually attach to last or keep as separate block at end.

    # Sorting:
    # Sort blocks by the *Payload* string.

    return _robust_sort(lines)

def _is_payload(line):
    line = line.strip()
    if not line.startswith('!'):
        return True
    # It starts with '!'
    # Check for rule signatures
    if any(x in line for x in ['##', '#$#', '#@#', '#%#', '#?#', '||']):
        return True
    # Check for 'http'
    if 'http:' in line or 'https:' in line:
        # Careful with comments containing links "See https://..."
        # If ' ' is before 'http', likely comment.
        # If '!http...' or '!|http...', rule.
        # Let's check space.
        if ' ' not in line.split('http')[0]:
            return True
    return False

def _robust_sort(lines):
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
            if stripped.startswith('!'):
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
                # Key for sorting: the payload line itself (normalized)
                block_content = pending_comments + [line]
                blocks.append({'sort_key': stripped.lower(), 'lines': block_content})
                pending_comments = []
            else:
                # It's a comment
                pending_comments.append(line)

    # Handle trailing comments
    if pending_comments:
        # Append to the last block or create a dummy block?
        # If we create dummy block, what is sort key?
        # Maybe sort key is the comment itself.
        blocks.append({'sort_key': pending_comments[0].strip().lower(), 'lines': pending_comments})

    # Sort blocks
    # Remove duplicates?
    # If blocks are identical (same comments + same rule), dedupe.
    # We need a hashable representation.

    unique_blocks = []
    seen = set()

    # Sort first
    sorted_blocks = sorted(blocks, key=lambda x: x['sort_key'])

    for block in sorted_blocks:
        # content tuple for deduping
        content_tuple = tuple(block['lines'])
        if content_tuple not in seen:
            seen.add(content_tuple)
            unique_blocks.append(block)

    # Reconstruct
    final_lines = header_lines[:]
    for block in unique_blocks:
        final_lines.extend(block['lines'])

    # Write back
    return final_lines

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    final_lines = _robust_sort(lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

    return len(final_lines) # Approximate rule count (includes comments)

def generate_a_txt():
    """
    Generates A.txt by including all .txt files in the filters directory.
    """
    files = sorted([f for f in FILTERS_DIR.glob('*.txt')])

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(HEADER)
        for file in files:
            relative_path = file.relative_to(ROOT_DIR).as_posix()
            f.write(f"!#include {relative_path}\n")

    print(f"Generated {OUTPUT_FILE} with {len(files)} includes.")

def main():
    if not FILTERS_DIR.exists():
        print(f"Error: Directory {FILTERS_DIR} does not exist.")
        return

    print("Processing filter files...")
    total_rules = 0
    for file_path in FILTERS_DIR.glob('*.txt'):
        print(f"Processing {file_path.name}...")
        count = process_file(file_path)
        total_rules += count

    print(f"Total lines processed: {total_rules}")

    print("Generating aggregate file...")
    generate_a_txt()
    print("Done.")

if __name__ == "__main__":
    main()

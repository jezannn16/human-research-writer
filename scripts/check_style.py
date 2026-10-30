"""Read-only character scan for authored UTF-8 coursework text, not an AI detector."""
import argparse
import json
from pathlib import Path
import re
import unicodedata

INVISIBLE = {0x00AD, 0x2060, 0xFEFF} | set(range(0x200B, 0x2010)) | set(
    range(0x202A, 0x202F)
) | set(range(0x2066, 0x206A)) | {0xFE0E, 0xFE0F}
DECORATIVE = set("•◦▪▫◆◇★☆✓✔✗✘☑☒►▶")
PATTERNS = [
    (re.compile(r"\.{3,}"), "ASCII_ELLIPSIS"),
    (re.compile(r"\bturn\d+(?:search|view|fetch)\d+\b|contentReference\[|oaicite"), "TOOL_TOKEN"),
]


def line_range(value):
    try:
        start, end = map(int, value.split(":"))
        if start < 1 or end < start:
            raise ValueError
        return start, end
    except ValueError as error:
        raise argparse.ArgumentTypeError("invalid line range; use START:END, 1 <= START <= END") from error


def scan(text, allowed):
    findings = []
    for line_number, line in enumerate(text.splitlines(), 1):
        if any(start <= line_number <= end for start, end in allowed):
            continue
        for column, char in enumerate(line, 1):
            point = ord(char)
            kind = None
            if 0x2012 <= point <= 0x2015:
                kind = "typographic dash"
            elif point == 0x2026:
                kind = "ellipsis"
            elif point in INVISIBLE:
                kind = "invisible formatting"
            elif 0x2190 <= point <= 0x21FF or char in DECORATIVE:
                kind = "arrow or decoration; review scientific context"
            elif 0x1F000 <= point <= 0x1FAFF or 0x2600 <= point <= 0x27BF:
                kind = "pictograph or dingbat; review scientific context"
            elif 0xE200 <= point <= 0xE2FF:
                kind = "service citation character"
            if kind:
                findings.append({"line": line_number, "column": column,
                                 "code": f"U+{point:04X}", "kind": kind,
                                 "name": unicodedata.name(char, "UNNAMED")})
        for pattern, code in PATTERNS:
            for match in pattern.finditer(line):
                findings.append({"line": line_number, "column": match.start() + 1,
                                 "code": code, "kind": "literal artifact"})
    return sorted(findings, key=lambda item: (item["line"], item["column"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--allow-lines", action="append", type=line_range, default=[],
                        metavar="START:END", help="manually verified quote, bibliography or technical lines")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        text = args.path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    if any(end > len(text.splitlines()) for _, end in args.allow_lines):
        parser.error("line range exceeds file length")
    findings = scan(text, args.allow_lines)
    if args.json:
        print(json.dumps({"file": str(args.path), "allowed_lines": args.allow_lines,
                          "findings": findings}, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f"{item['line']}:{item['column']} {item['code']} {item['kind']}")
        print(f"Findings: {len(findings)}; explicit line exceptions: {args.allow_lines}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

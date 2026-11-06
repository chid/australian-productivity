"""Convert the research report's bibliography (markdown list) into references.bib.

Each line looks like:
  - [Key] Authors (2026). *Title* or "Title." Publisher... https://url — label
Usage: python3 -I paper/tools/bib_from_report.py "reports/<report>.md" paper/references.bib
"""
import re, sys

src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
bib_part = text.split("## Bibliography", 1)[1]
section = "official"
entries, seen = [], set()


def esc(s):
    s = s.replace("\\", "").replace("{", "").replace("}", "")
    for a, b in [("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"), ("$", r"\$")]:
        s = s.replace(a, b)
    return s.strip()


for line in bib_part.splitlines():
    h = re.match(r"^###\s+(.*)", line)
    if h:
        section = h.group(1).split("(")[0].strip().lower()
        continue
    m = re.match(r"^- \[([^\]]+)\]\s+(.*)$", line)
    if not m:
        continue
    key, rest = m.group(1).strip(), m.group(2)
    key = re.sub(r"[^A-Za-z0-9_:-]", "", key)
    if key in seen:
        continue
    seen.add(key)
    label = section
    lm = re.search(r"\s+—\s+([^—]+)$", rest)
    if lm:
        label = lm.group(1).strip()
        rest = rest[: lm.start()]
    urls = re.findall(r"https?://[^\s;,)]+[^\s;,).]", rest)
    url = urls[0] if urls else ""
    am = re.match(r"^(.*?)\s*\((\d{4}|n\.d\.)[a-z]?\)\.?\s*(.*)$", rest)
    if am:
        author, year, after = am.group(1), am.group(2), am.group(3)
    else:
        author, year, after = rest.split(".")[0], "n.d.", rest
    tm = re.search(r"\*([^*]+)\*", after) or re.search(r"[\"“]([^\"”]+)[\"”]", after)
    title = tm.group(1) if tm else after.split(". ")[0]
    # venue: italic text after a quoted title
    venue = ""
    if re.search(r"[\"“]", after) and re.search(r"\*([^*]+)\*", after):
        venue = re.search(r"\*([^*]+)\*", after).group(1)
        title = re.search(r"[\"“]([^\"”]+)[\"”]", after).group(1)
    author = author.replace(", and ", " and ").replace(" & ", " and ")
    # Corporate authors stay as one braced name
    corp = not re.search(r",\s*[A-Z]\.", author)
    author_field = "{" + esc(author) + "}" if corp else esc(re.sub(r"\.,\s*(?=[A-Z][a-z])", ". and ", author))
    fields = [("author", author_field), ("title", "{" + esc(title.rstrip(".")) + "}"), ("year", year if year != "n.d." else "n.d.")]
    if venue:
        fields.append(("journal" if section.startswith("peer") else "howpublished", esc(venue)))
    if url:
        fields.append(("url", url))
    fields.append(("note", esc(f"Reliability: {label}")))
    entries.append(f"@misc{{{key},\n" + ",\n".join(f"  {k} = {{{v}}}" if not v.startswith("{") else f"  {k} = {v}" for k, v in fields) + "\n}\n")

with open(dst, "w", encoding="utf-8") as f:
    f.write("% Generated from the research report bibliography by tools/bib_from_report.py.\n")
    f.write("% Entries are @misc with a reliability note; verify flagged entries before submission.\n\n")
    f.write("\n".join(entries))
print(f"wrote {len(entries)} entries to {dst}")

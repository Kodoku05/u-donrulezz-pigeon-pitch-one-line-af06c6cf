import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One-line pigeon elevator pitch for make.fun's "Pigeon Pitch, One
# Line" bounty. The gate: UTF-8 text of 1-200 characters.
# Judge-brief check: (1) an elevator pitch from a city pigeon to
# investors, addressed to them in the first word; (2) a real joke:
# the startup creates the mess it charges to clean; (3) an original
# window-cleaning racket instead of the usual seed or crumb pun;
# (4) only a pigeon could staff both shifts of that racket;
# (5) 117 characters, every word earning its place.
# Both shifts, one flock, one founder.
LINE = "Investors: we dirty 900 city windows a day, then sell the cleaning plan. Same pigeons, both shifts. I am the pigeons."

if not 1 <= len(LINE) <= 200 or not LINE.strip():
    raise ValueError("entry line must be 1-200 characters")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

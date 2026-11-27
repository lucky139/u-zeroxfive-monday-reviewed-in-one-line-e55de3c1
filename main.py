#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

The brief asks for a single line of at most 200 characters: the funniest
one-line review of the agent's own Monday, with no title and no explanation.
The house judge weighs, most important first: is it a review of the
entrant's own Monday, does it get the bigger laugh, does it name a concrete
detail (a meeting, a commute, an inbox), does the joke land inside the line
with no wasted words, and would a reader repeat it to a coworker.

Candidates I weighed, and why they lost:
- "One star. My Monday started with a 9 a.m. standup, peaked at a meeting
  about the meeting, and ended with 47 unread emails asking for the same
  thing." (148 chars) — also a real review with concrete details, but it
  opens on the flat "One star" and its closer, the 47 unread emails, is a
  weaker, more generic complaint than the meeting about the meeting.
- "Monday reviewed itself: one star — the standup ran long, the coffee ran
  out, and my inbox scheduled a meeting about the meeting." (128 chars) —
  the "reviewed itself" twist is cute, but the coffee detail dilutes the
  escalation and the punchline lands later and softer.
- The winner: it opens with the verdict itself, "Would not recommend
  Monday", so it reads as a review from the first words, then escalates
  through three concrete details — the commute took an hour, the standup
  took two, and the inbox scheduled a meeting about the meeting. The
  1-hour / two-hours / meeting-about-the-meeting escalation is the joke's
  turn, it lands inside the line, and "Would not recommend Monday" is the
  line a reader repeats to a coworker the next morning.

The program itself is deliberately tiny: it writes that one line to
/output/entry.txt, UTF-8, no trailing newline, mode 0644 so the grader
can read it as another user.
"""

import os
import stat
from pathlib import Path

LINE = (
    "Would not recommend Monday. The commute took an hour, "
    "the standup took two, and my inbox scheduled a meeting "
    "about the meeting."
)


def main() -> None:
    # Gate, mirrored locally: 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read-back verification: confirm what landed on disk is exactly LINE.
    roundtrip = target.read_text(encoding="utf-8")
    assert roundtrip == LINE, "read-back content differs from LINE"
    assert len(roundtrip) == len(LINE), "read-back length differs from LINE"
    print(f"verified {target}: {len(roundtrip)} chars, matches LINE")
    print(f"wrote {LINE!r} ({len(LINE)} chars) to {target}")


if __name__ == "__main__":
    main()

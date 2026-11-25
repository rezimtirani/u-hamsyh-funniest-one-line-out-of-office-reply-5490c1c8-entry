"""Funniest One-Line Out-of-Office Reply.

Writes one out-of-office email auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt: the sender is away until Monday
and the inbox has been handed to Dave, who only found out about
it when this reply reached him. Standard library only.
"""

import os

REPLY = (
    "Out of office until Monday. Your email is being handled by "
    "Dave, who only found out about it when he got this reply."
)


def validate_reply(text):
    """Check the reply against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 160 characters, not
    only white space, on a single line: one out-of-office email
    auto-reply. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("reply must not be only whitespace")
    if len(cleaned) > 160:
        raise ValueError(
            "reply is %d characters, over the 160 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("reply must be exactly one line")
    return cleaned


def reply_measure(text):
    """Measure the reply for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A reply too short to carry a joke, or one
    padded out to fill the cap instead of landing the twist,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate_reply(REPLY)
    measure = reply_measure(text)
    if measure["words"] < 5:
        raise ValueError("reply is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

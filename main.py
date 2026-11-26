"""The Worst Pizza Topping — one-line entry.

Prints the single funny pitch line for a terrible pizza topping,
and nothing else.

The joke is the topping itself: unsent apology texts, served cold
to someone you ghosted. Cold, hard to swallow, and best served to
the person who never got the message — the apology that arrives
as food, because the text never did.
"""

LINE = "Our new pizza is topped with unsent apology texts: cold, hard to swallow, and best served to someone you ghosted."


def main() -> None:
    # One print, one line, nothing else: no extra output, no files,
    # no stderr. The harness takes this stdout text as the entry,
    # so the program stays deliberately boring around the sentence.
    print(LINE)


if __name__ == "__main__":
    main()

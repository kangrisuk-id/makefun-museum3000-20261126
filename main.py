"""Museum of the Year 3000 - entry program.

Writes the winning museum label (one line, plain text) to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR. Pure standard library,
fully deterministic: no clock, no randomness, no network.
"""

import os

LABEL = (
    "Proof of Humanity (c. 2023). To open their own accounts, citizens "
    "proved they were not machines by finding every traffic light in a "
    "picture grid for one, unpaid."
)


def candidate_dirs():
    """Output locations, most preferred first."""
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append(os.path.dirname(os.path.abspath(__file__)))
    dirs.append(os.getcwd())
    return dirs


def main():
    last_error = None
    for out_dir in candidate_dirs():
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(LABEL)
            return
        except OSError as error:
            last_error = error
    if last_error is not None:
        raise last_error


if __name__ == "__main__":
    main()

# Contributing to Web_StaticY

Thanks for helping improve Web_StaticY. Contributions can include bug reports, documentation, theme files, accessibility improvements, and focused code changes.

## Before you start

1. Check the existing issues and pull requests for related work.
2. For a substantial change, open an issue first so the approach can be discussed.
3. Keep changes focused. Avoid mixing unrelated formatting or generated files into a pull request.

## Development setup

Use Python 3.14.7 or newer and a POSIX-compatible shell. From the repository root:

```sh
npm install
```

Install the Python dependencies declared in `pyproject.toml`. Install PyQt6 separately when working on `scripts/colorpicker.py`.

Run the relevant checks before submitting a change:

```sh
npx tsc --noEmit
python -m compileall main.py scripts
```

For UI or website changes, also open `page/index.html` and the relevant pages in `tests/themes/` in a browser. For palette-browser changes, run:

```sh
python scripts/colorpicker.py
```

## Making changes

- Put website source in `page/`, shared styles in `src/`, and reusable files in `assets/`.
- Keep theme directories structurally consistent. A theme should provide the files listed in the README.
- Use clear, descriptive names and preserve the existing lowercase theme naming style.
- Keep scripts safe to run from any working directory by resolving paths from the project location.
- Do not commit local virtual environments, caches, editor settings, or generated build output unless the change explicitly requires it.
- Update `README.md` when a command, directory, or supported workflow changes.

## Commits and pull requests

Use a short imperative commit subject, such as `Add Nord theme preview`. In the pull request description, explain:

- what changed and why;
- how you tested it;
- which operating systems or browsers you checked;
- any known limitations or follow-up work.

Keep pull requests reviewable and include screenshots for visible website or UI changes when useful.

## Reporting bugs

Please include the operating system, Python and Node.js versions, the exact command or interaction that failed, and the complete error output. A small reproduction or affected file path makes diagnosis much faster.
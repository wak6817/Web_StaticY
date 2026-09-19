# Web StaticY

Web StaticY is a small static-web project and theme toolkit. It contains a browser page, reusable CSS themes, local assets, and helper tools for browsing and exporting color palettes.

## What is included

- `page/` — the current static website entry point and page assets.
- `src/themes/` — theme source files, including Catppuccin variants, Dracula, Nord, and Alucard.
- `src/templates.css` — shared template styles.
- `assets/` — fonts and icons used by the project.
- `scripts/colorpicker.py` — a PyQt6 desktop palette browser.
- `scripts/export.py` and `scripts/import.py` — early theme import/export helpers.
- `scripts/build/` — build-script work in progress.
- `tests/themes/` — HTML pages for manually inspecting theme components.
- `main.py` — a Textual setup interface for platform/package setup.

## Requirements

- Python 3.14.7 or newer
- Node.js and npm for TypeScript tooling
- A POSIX-compatible shell for the shell scripts
- PyQt6 to run the color picker script
- Textual to run the setup interface

On Windows, use WSL or another POSIX-compatible environment for the shell scripts.

## Getting started

Clone the repository and enter its directory:

```sh
git clone https://github.com/wak6817/Web_StaticY.git
cd Web_StaticY
```

Create or activate a Python environment, then install the Python dependencies with your preferred package manager. The project metadata lists Textual as a runtime dependency; install PyQt6 as well if you want to use the color picker.

Install the JavaScript dependency:

```sh
npm install
```

To preview the site, open `page/index.html` in a browser or serve the repository with a local static server. For example:

```sh
python -m http.server --directory page
```

## Useful commands

Run the Textual setup interface:

```sh
python main.py
```

Run the palette browser:

```sh
python scripts/colorpicker.py
```

Check the TypeScript configuration without emitting files:

```sh
npx tsc --noEmit
```

The theme inspection pages in `tests/themes/` can be opened in a browser to check API, icon, interaction, template, and text styles. The scripts in `scripts/build/` are present but still under development; verify their output before publishing a build.

## Adding or editing a theme

Theme sources live in `src/themes/<theme-name>/`. A complete theme currently contains:

```text
trans.css
api.css
modernv/fonts.css
modernv/margins.css
pixelv/fonts.css
pixelv/margins.css
colorv/interactions.css
colorv/other.css
colorv/text.css
```

Keep names lowercase and consistent with the existing theme directories. Check the result in the relevant pages under `tests/themes/`, and update the documentation when adding a new supported workflow.

## Project status

This project is actively being organized. Some setup, build, and import/export helpers are prototypes rather than a stable release pipeline. If a command does not work as expected, please include the command, operating system, and full error output in an issue.

## Contributing

Bug reports, theme improvements, documentation fixes, and small focused features are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is distributed under the MIT License. See [license](LICENSE).

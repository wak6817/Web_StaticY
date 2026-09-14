import re
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk


ROOT_DIR = Path(__file__).resolve().parent.parent
COLOR_PATTERN = re.compile(
	r"^\s*--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\b", re.MULTILINE
)


def load_palettes():
	palettes = {}
	for palette_file in sorted((ROOT_DIR / "src").glob("*/trans.css")):
		colors = COLOR_PATTERN.findall(palette_file.read_text(encoding="utf-8"))
		if colors:
			palettes[palette_file.parent.name] = colors
	return palettes


def readable_text(hex_value):
	red = int(hex_value[1:3], 16)
	green = int(hex_value[3:5], 16)
	blue = int(hex_value[5:7], 16)
	brightness = (red * 299 + green * 587 + blue * 114) / 1000
	return "#171717" if brightness > 155 else "#ffffff"


class PaletteWindow:
	def __init__(self, parent, palette_name, colors):
		self.window = tk.Toplevel(parent)
		self.window.title(f"{palette_name} colors")
		self.window.minsize(430, 300)
		self.window.geometry("520x520")
		self.colors = colors

		header = ttk.Frame(self.window, padding=(16, 14, 16, 8))
		header.pack(fill="x")
		ttk.Label(header, text=palette_name, style="Title.TLabel").pack(anchor="w")

		preview = tk.Frame(self.window, height=72, bg=colors[0][1])
		preview.pack(fill="x", padx=16, pady=(4, 12))
		preview.pack_propagate(False)
		preview_label = tk.Label(
			preview,
			text="palette preview",
			bg=colors[0][1],
			fg=readable_text(colors[0][1]),
			font=("TkDefaultFont", 12, "bold"),
		)
		preview_label.pack(expand=True)

		content = ttk.Frame(self.window, padding=(16, 0, 16, 16))
		content.pack(fill="both", expand=True)
		canvas = tk.Canvas(content, highlightthickness=0)
		scrollbar = ttk.Scrollbar(content, orient="vertical", command=canvas.yview)
		rows = ttk.Frame(canvas)
		rows.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
		canvas.create_window((0, 0), window=rows, anchor="nw", width=465)
		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.pack(side="left", fill="both", expand=True)
		scrollbar.pack(side="right", fill="y")

		for color_name, hex_value in colors:
			self.add_color_row(rows, color_name, hex_value)

	def add_color_row(self, parent, color_name, hex_value):
		row = ttk.Frame(parent, padding=(0, 3))
		row.pack(fill="x")
		swatch = tk.Frame(row, width=42, height=32, bg=hex_value)
		swatch.pack(side="left", padx=(0, 10))
		swatch.pack_propagate(False)
		ttk.Label(row, text=color_name, width=16).pack(side="left")
		value = tk.StringVar(value=hex_value.upper())
		entry = ttk.Entry(row, textvariable=value, width=10)
		entry.pack(side="left", padx=(0, 8))
		entry.bind("<FocusIn>", lambda event: entry.select_range(0, "end"))
		ttk.Button(row, text="copy", command=lambda: self.copy_value(value.get())).pack(
			side="left"
		)

	def copy_value(self, value):
		self.window.clipboard_clear()
		self.window.clipboard_append(value)
		self.window.update()


def open_palette():
	palette_name = palette_choice.get()
	colors = palettes.get(palette_name, [])
	if not colors:
		messagebox.showerror("No colors", f"Could not load the {palette_name} palette.")
		return
	PaletteWindow(root, palette_name, colors)


def main():
	global palettes, root, palette_choice

	palettes = load_palettes()
	root = tk.Tk()
	root.title("Color scheme browser")
	root.resizable(False, False)

	style = ttk.Style(root)
	style.configure("Title.TLabel", font=("TkDefaultFont", 16, "bold"))
	main_frame = ttk.Frame(root, padding=24)
	main_frame.pack()
	ttk.Label(main_frame, text="colorscheme browser", style="Title.TLabel").pack(anchor="w")

	palette_choice = tk.StringVar(value=next(iter(palettes), ""))
	selector = ttk.Combobox(
		main_frame,
		textvariable=palette_choice,
		values=list(palettes),
		state="readonly",
		width=24,
	)
	selector.pack(side="left", padx=(0, 8))
	ttk.Button(main_frame, text="Open palette", command=open_palette).pack(side="left")

	if not palettes:
		selector.configure(state="disabled")

	root.mainloop()


if __name__ == "__main__":
	main()

import re
import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


ROOT_DIR = Path(__file__).resolve().parent.parent
COLOR_PATTERN = re.compile(
    r"^\s*--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\b", re.MULTILINE
)


def load_palettes():
    palettes = {}
    for palette_file in sorted((ROOT_DIR / "src").rglob("trans.css")):
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


class PaletteWindow(QDialog):
    def __init__(self, parent, palette_name, colors):
        super().__init__(parent)
        self.setWindowTitle(f"{palette_name} colors")
        self.setMinimumSize(430, 300)
        self.resize(520, 520)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 16)
        layout.setSpacing(12)

        title = QLabel(palette_name)
        title.setFont(QFont(self.font().family(), 16, QFont.Weight.Bold))
        layout.addWidget(title)

        preview = QLabel("palette preview")
        preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        preview.setMinimumHeight(72)
        preview.setStyleSheet(
            f"background-color: {colors[0][1]}; "
            f"color: {readable_text(colors[0][1])}; "
            "font-weight: bold; font-size: 12pt;"
        )
        layout.addWidget(preview)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)
        rows = QWidget()
        rows_layout = QVBoxLayout(rows)
        rows_layout.setContentsMargins(0, 0, 0, 0)
        rows_layout.setSpacing(6)
        for color_name, hex_value in colors:
            self.add_color_row(rows_layout, color_name, hex_value)
        rows_layout.addStretch()
        scroll_area.setWidget(rows)
        layout.addWidget(scroll_area)

    def add_color_row(self, layout, color_name, hex_value):
        row = QWidget()
        row_layout = QHBoxLayout(row)
        row_layout.setContentsMargins(0, 0, 0, 0)

        swatch = QLabel()
        swatch.setFixedSize(42, 32)
        swatch.setStyleSheet(f"background-color: {hex_value};")
        row_layout.addWidget(swatch)

        name = QLabel(color_name)
        name.setFixedWidth(128)
        row_layout.addWidget(name)

        entry = QLineEdit(hex_value.upper())
        entry.setFixedWidth(90)
        entry.setReadOnly(True)
        entry.selectAll()
        row_layout.addWidget(entry)

        copy_button = QPushButton("copy")
        copy_button.clicked.connect(lambda: self.copy_value(entry.text()))
        row_layout.addWidget(copy_button)
        row_layout.addStretch()
        layout.addWidget(row)

    def copy_value(self, value):
        QApplication.clipboard().setText(value)


class MainWindow(QMainWindow):
    def __init__(self, palettes):
        super().__init__()
        self.palettes = palettes
        self.setWindowTitle("Color scheme browser")
        self.setFixedSize(390, 120)

        main_frame = QWidget()
        layout = QVBoxLayout(main_frame)
        layout.setContentsMargins(24, 20, 24, 20)

        title = QLabel("colorscheme browser")
        title.setFont(QFont(self.font().family(), 16, QFont.Weight.Bold))
        layout.addWidget(title)

        controls = QHBoxLayout()
        self.palette_choice = QComboBox()
        self.palette_choice.addItems(list(palettes))
        self.palette_choice.setMinimumWidth(190)
        controls.addWidget(self.palette_choice)

        open_button = QPushButton("Open palette")
        open_button.clicked.connect(self.open_palette)
        controls.addWidget(open_button)
        layout.addLayout(controls)
        self.setCentralWidget(main_frame)

        if not palettes:
            self.palette_choice.setDisabled(True)
            open_button.setDisabled(True)

    def open_palette(self):
        palette_name = self.palette_choice.currentText()
        colors = self.palettes.get(palette_name, [])
        if not colors:
            QMessageBox.critical(
                self,
                "No colors",
                f"Could not load the {palette_name} palette.",
            )
            return
        self.palette_window = PaletteWindow(self, palette_name, colors)
        self.palette_window.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow(load_palettes())
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

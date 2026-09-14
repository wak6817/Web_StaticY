from platform import system
import subprocess
from pathlib import Path

from textual import work
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Button, Footer, Header, Label, RichLog, Select, Static


ROOT_DIR = Path(__file__).resolve().parent


class WebStaticyApp(App):
    TITLE = "Web StaticY Setup"
    SUB_TITLE = "Project Initialization"

    CSS = """
    Screen {
        align: center middle;
    }

    #main {
        width: 70;
        height: auto;
        border: round $accent;
        padding: 1 2;
    }

    #system {
        margin: 1 0;
    }

    #actions {
        height: auto;
        margin-top: 1;
    }

    Button {
        margin-right: 1;
    }

    #status {
        margin-top: 1;
        color: $text-muted;
    }

    #output {
        height: 12;
        margin-top: 1;
        border: round $accent;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Container(id="main"):
            yield Label("Web StaticY setup")
            yield Static(
                "Choose your operating system, then run the setup steps."
            )

            yield Select(
                [
                    ("Debian", "debian"),
                    ("Arch", "arch"),
                ],
                prompt="Linux distribution",
                id="system",
                allow_blank=True,
            )

            with Horizontal(id="actions"):
                yield Button("Download packages", id="download")
                yield Button("Initialize project", id="initialize")
                yield Button("Quit", id="quit", variant="error")

            yield Static("Ready.", id="status")
            yield RichLog(id="output")

        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#system", Select).display = system() == "Linux"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.exit()

        elif event.button.id == "download":
            self.download_packages()

        elif event.button.id == "initialize":
            self.initialize_project()

    def download_packages(self) -> None:
        current_system = system()

        if current_system == "Windows":
            self.set_status(
                "Windows is not supported; install WSL to use a Linux environment."
            )
            return

        if current_system == "Darwin":
            command = ["sh", str(ROOT_DIR / "scripts/macos-brew.sh")]

        elif current_system == "Linux":
            distribution = self.query_one("#system", Select).value

            if distribution is Select.BLANK:
                self.set_status("Select Debian or Arch first.")
                return

            scripts = {
                "debian": ROOT_DIR / "scripts/debian-apt.sh",
                "arch": ROOT_DIR / "scripts/arch-pacman.sh",
            }

            script = scripts.get(str(distribution))

            if script is None:
                self.set_status("Unsupported Linux distribution.")
                return

            command = ["sh", str(script)]

        else:
            self.set_status(f"{current_system} is not supported.")
            return

        self.run_script(command, "Package setup finished.")

    def initialize_project(self) -> None:
        self.run_script(
            ["sh", str(ROOT_DIR / "scripts/project-init.sh")],
            "Project initialization finished.",
        )

    @work(thread=True)
    def run_script(
        self,
        command: list[str],
        success_message: str,
    ) -> None:
        output = self.query_one("#output", RichLog)

        self.call_from_thread(output.write, f"$ {' '.join(command)}")

        try:
            result = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
            )

        except OSError as error:
            self.call_from_thread(
                self.set_status,
                f"Could not run setup: {error}",
            )
            return

        if result.stdout:
            self.call_from_thread(output.write, result.stdout.rstrip())

        if result.stderr:
            self.call_from_thread(output.write, result.stderr.rstrip())

        if result.returncode == 0:
            self.call_from_thread(self.set_status, success_message)
        else:
            self.call_from_thread(
                self.set_status,
                f"Setup failed with exit code {result.returncode}.",
            )

    def set_status(self, message: str) -> None:
        self.query_one("#status", Static).update(message)


if __name__ == "__main__":
    WebStaticyApp().run()

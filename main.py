from platform import system
import subprocess

def get_system():
    if system() == "Windows":
        print("System NOT supported, download WSL to run this in a Linux environment")

    elif system() == "Darwin":
        subprocess.run(["sh", "scripts/macos-brew.sh"])

    elif system() == "Linux":
        linux_sys = input("Debian or Arch: ")

        if linux_sys.lower() == "debian":
            subprocess.run(["sh", "scripts/debian-apt.sh"])

        elif linux_sys.lower() == "arch":
            subprocess.run(["sh", "scripts/arch-pacman.sh"])

        else:
            print(f"{linux_sys} is not supported")

    else:
        print("Your system is not supported")

if __name__ == "__main__":
    get_system()
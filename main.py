from platform import system
import subprocess

def get_system():
    i = input("Download needed packages? (y/n)")
    if i == "y":
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
    else:
        print("Abort")

if __name__ == "__main__":
    get_system()
    i = input("Did you edit scripts/project-init.sh? (y/n)")

    if i == "y":
        subprocess.run(["sh", "scripts/project-init.sh"])
    else:
        print("Abort")
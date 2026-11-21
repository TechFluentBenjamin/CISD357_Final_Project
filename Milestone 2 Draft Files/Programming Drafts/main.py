# Benjamin Hays
# W0018940
# CISP 357 - Introduction to Data Science
# Main intefrace for the coding script
# Originally written for Lab 12, but code reuse is a thing.

import os
import platform
import subprocess
import sys


def display_main_menu():
    print("\n1. Read me")
    print("2. Download Data")
    print("3. Analyze Data")
    print("4. Group Data")
    print("5. Clean Data")
    print("6. Generate Charts")
    print("7. View Report")
    print("8. Quit program")


def handle_readme():
    print(
        "\nPlease select an option. This assumes Visual Studio Code is installed and accessible from the command line. These options must be performed in order for the program to successfully run. Running this program out of order will result in an error."
    )


def handle_download():
    if not os.path.exists("download.py"):
        print("\n“download.py was not found.”")
    else:
        subprocess.run([sys.executable, "download.py"])
        print("\n“Download complete. Please select the next option.”")


def handle_analyze():
    if not os.path.exists("analyze.py"):
        print("\n“Analyze.py was not found.”")
    else:
        subprocess.run([sys.executable, "analyze.py"])
        print("\n“Analysis complete. Please select the next option.”")


def handle_group():
    if not os.path.exists("grouping.py"):
        print("\n“Grouping.py was not found.“")
    else:
        subprocess.run([sys.executable, "grouping.py"])
        print("\n“Grouping complete. Please select the next option.”")


def handle_clean():
    if not os.path.exists("clean.py"):
        print("\nError: clean.py was not found.")
    else:
        subprocess.run([sys.executable, "clean.py"])
        print("\n“Successfully cleaned the files. Please select the next option.”")


def handle_chart():
    if not os.path.exists("chart.py"):
        print("\nError: chart.py was not found.")
    else:
        subprocess.run([sys.executable, "chart.py"])
        print("\n“Successfully created the charts. Please select the next option.”")


def handle_report():
    report_file = "visualization_report.md"
    if not os.path.exists(report_file):
        print(f"\nError: '{report_file}' was not found in the main directory.")
        return

    system = platform.system()
    try:
        if system == "Windows":
            # Opens the Windows version of Visual Studio Code
            subprocess.run(["code.cmd", report_file], shell=True, check=True)
            print(
                f"\nOpened '{report_file}' in Visual Studio Code (Windows). "
                "(Tip: Press Ctrl+Shift+V to toggle Markdown Preview mode)."
            )
        elif system == "Darwin":
            # Opens the macOS application bundle for Visual Studio Code
            subprocess.run(
                ["open", "-a", "Visual Studio Code", report_file], check=True
            )
            print(
                f"\nOpened '{report_file}' in Visual Studio Code (macOS). "
                "(Tip: Press Cmd+Shift+V to toggle Markdown Preview mode)."
            )
        else:
            # Opens the Linux version of Visual Studio Code
            subprocess.run(["code", report_file], check=True)
            print(
                f"\nOpened '{report_file}' in Visual Studio Code (Linux). "
                "(Tip: Press Ctrl+Shift+V to toggle Markdown Preview mode)."
            )

    except Exception:
        print(
            "\nplease use your file system to navigate to the visualization_report.md and open the file using an appropriate markdown reader"
        )


def main():
    running = True
    while running:
        display_main_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            handle_readme()
        elif choice == "2":
            handle_download()
        elif choice == "3":
            handle_analyze()
        elif choice == "4":
            handle_group()
        elif choice == "5":
            handle_clean()
        elif choice == "6":
            handle_chart()
        elif choice == "7":
            handle_report()
        elif choice == "8":
            print("\nExiting program. Goodbye!")
            running = False
        else:
            print("\nInvalid option. Please choose a number between 1 and 7.")

    # Let's exit the program with a status code of 0 to indicate successful termination.
    # I was complained once for using break to end a while loop, so now I'm using a boolean variable to control the loop and then exiting with sys.exit(0) to indicate successful termination.
    sys.exit(0)


if __name__ == "__main__":
    main()

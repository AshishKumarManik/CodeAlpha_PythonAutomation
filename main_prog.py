import os
import shutil
import re

def extract_emails_from_file():
    """Extracts email addresses from a given text file and saves them to another file."""
    input_file = input("📄 Enter the input .txt file name (e.g., input.txt): ").strip()
    output_file = input("💾 Enter the output file name (e.g., emails.txt): ").strip()

    if not os.path.exists(input_file):
        print("❌ Error: Input file not found.")
        return

    try:
        with open(input_file, "r") as infile:
            content = infile.read()

        # Regex pattern to find emails
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)
        unique_emails = sorted(set(emails))

        if not unique_emails:
            print("⚠️ No email addresses found in the file.")
            return

        with open(output_file, "w") as outfile:
            for email in unique_emails:
                outfile.write(email + "\n")

        print(f"✅ Successfully extracted {len(unique_emails)} unique email(s) to '{output_file}'.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")


def move_jpg_files_between_folders():
    """Moves all .jpg files from one folder to another."""
    source_folder = input("📂 Enter the source folder path: ").strip()
    destination_folder = input("📁 Enter the destination folder path: ").strip()

    if not os.path.isdir(source_folder):
        print("❌ Error: Source folder does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    jpg_files = [file for file in os.listdir(source_folder) if file.lower().endswith('.jpg')]

    if not jpg_files:
        print("⚠️ No .jpg files found in the source folder.")
        return

    for file in jpg_files:
        shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))

    print(f"✅ Successfully moved {len(jpg_files)} .jpg file(s) to '{destination_folder}'.")


def main():
    """Main menu for automation tasks."""
    print("\n==============================")
    print("🛠️  Python Automation Tool")
    print("==============================")
    print("💌 Type 'email' to extract emails from a text file")
    print("🖼️  Type 'img' to move .jpg files between folders")
    print("==============================")

    choice = input("👉 Enter your choice ('1' or '2'): ").strip().lower()

   if choice == 'email':
    extract_emails_from_file()
elif choice == 'img':
    move_jpg_files_between_folders()
else:
    print("❌ Invalid choice. Please type 'email' or 'img'.")

if __name__ == "__main__":
    main()

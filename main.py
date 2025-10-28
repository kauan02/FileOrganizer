import os
import shutil
import json
from datetime import datetime

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
BACKUP_PATH = os.path.join(DOWNLOADS_PATH, "Backup")
DEST_PATH = os.path.join(DOWNLOADS_PATH, "Organized")
LOG_PATH = os.path.join(DEST_PATH, "log.json")

CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp",
        ".heic", ".svg", ".ico", ".psd", ".ai", ".eps"
    ],
    "Word_Documents": [
        ".doc", ".docx", ".dot", ".dotx", ".rtf", ".odt", ".pages"
    ],
    "Excel_Sheets": [
        ".xls", ".xlsx", ".xlsm", ".xlsb", ".ods", ".csv", ".tsv"
    ],
    "PowerPoint": [
        ".ppt", ".pptx", ".pps", ".odp", ".key"
    ],
    "Documents": [
        ".pdf", ".txt", ".md", ".log", ".tex"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".3gp", ".mpeg", ".mpg"
    ],
    "Audio": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".aiff", ".mid", ".midi"
    ],
    "Code": [
        ".py", ".js", ".ts", ".html", ".css", ".json", ".xml", ".java", ".cpp",
        ".c", ".cs", ".php", ".rb", ".go", ".swift", ".sh", ".bat", ".ps1",
        ".sql", ".yml", ".yaml", ".ini", ".cfg"
    ],
    "Compressed": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"
    ],
    "Executables": [
        ".exe", ".msi", ".bat", ".cmd", ".sh", ".app", ".deb", ".rpm", ".jar"
    ],
    "Fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot"
    ],
    "Design_3D": [
        ".stl", ".obj", ".fbx", ".blend", ".3ds", ".dae"
    ],
    "Others": []
}

def create_folders():
    for path in [BACKUP_PATH, DEST_PATH]:
        os.makedirs(path, exist_ok=True)
    for category in CATEGORIES.keys():
        os.makedirs(os.path.join(DEST_PATH, category), exist_ok=True)

def identify_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def load_log():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def save_log(log_data):
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=4)

def organize_files():
    create_folders()
    log_data = load_log()
    script_name = None
    try:
        script_name = os.path.basename(__file__)
    except:
        script_name = ""
    for file_name in os.listdir(DOWNLOADS_PATH):
        original_path = os.path.join(DOWNLOADS_PATH, file_name)
        if os.path.isdir(original_path) or file_name == script_name:
            continue
        extension = os.path.splitext(file_name)[1]
        category = identify_category(extension)
        destination = os.path.join(DEST_PATH, category, file_name)
        backup_destination = os.path.join(BACKUP_PATH, file_name)
        try:
            size = os.path.getsize(original_path)
        except:
            size = 0
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            shutil.copy2(original_path, backup_destination)
            shutil.move(original_path, destination)
            log_entry = {
                "name": file_name,
                "extension": extension,
                "size_bytes": size,
                "original_path": original_path,
                "backup_path": backup_destination,
                "destination_path": destination,
                "date": current_date,
                "status": "copied and moved"
            }
            log_data.append(log_entry)
            print(f"[OK] {file_name} → {category}")
        except Exception as e:
            print(f"[ERROR] Could not move {file_name}: {e}")
    save_log(log_data)
    print("\nOrganization completed!")

if __name__ == "__main__":
    organize_files()

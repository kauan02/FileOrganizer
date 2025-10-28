# 🗂️ Download Organizer

A simple Python script that automatically organizes your **Downloads** folder by file type,
creates a **backup copy**, and logs every move in a JSON file.

---

## 🚀 Features

* Automatically detects and sorts files into categories (Images, Documents, Videos, Code, etc.)
* Creates a **Backup** folder before moving any file
* Saves file info in a structured **log.json** file (size, name, date, origin, destination)
* Supports dozens of file extensions grouped by category

---

## 📁 Folder structure

```
Downloads/
│
├── Backup/
│   └── (file copies)
│
├── Organized/
│   ├── Images/
│   ├── Documents/
│   ├── Audio/
│   ├── Code/
│   └── Others/
│
└── log.json
```

---

## ⚙️ Installation

1. Make sure you have **Python 3.8+** installed
2. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/download-organizer.git
   cd download-organizer
   ```
3. Run the script:

   ```bash
   python main.py
   ```

---

## 🧠 How it works

* The script scans your **Downloads** folder
* Determines each file’s category by its extension
* Copies the file to the **Backup** folder
* Moves it to the corresponding folder inside **Organized**
* Saves all operations in `log.json`

---

## 🗒 Example log entry

```json
{
    "name": "example.pdf",
    "extension": ".pdf",
    "size_bytes": 24576,
    "original_path": "C:/Users/Kauan/Downloads/example.pdf",
    "backup_path": "C:/Users/Kauan/Downloads/Backup/example.pdf",
    "destination_path": "C:/Users/Kauan/Downloads/Organized/Documents/example.pdf",
    "date": "2025-10-28 15:00:00",
    "status": "copied and moved"
}
```

---

## 🧑‍💻 Author

**Kauan Barbosa Rezende**
GitHub: [github.com/kauan02](https://github.com/kauan02)
LinkedIn: [linkedin.com/in/kauan-barbosa-5b8133268](https://linkedin.com/in/kauan-barbosa-5b8133268)

---

## 🪪 License

This project is licensed under the **MIT License**.


# 🐍 Jsersion – Simple Version Control for Code Files

Jsersion (**JSVC**) is a **lightweight version control system** for code files, written in Python.
It is designed for **private or small-scale projects** where a full-fledged VCS like Git might be unnecessary or too heavy.

> ⚠️ **Note:** Jsersion is **not recommended** for large-scale or public release workflows.

---

## ✨ Features

* 📦 **Push** code files to a local repo with metadata.
* 🔑 **Optional encryption** using [Fernet](https://cryptography.io/) for secure storage.
* 💾 **Backup system** – automatically create or restore from backups.
* 📝 **Metadata storage** (author, version, language, date, description, tags).
* 📚 **Commit** multiple JSON repos into a single `main_repo.json`.
* 🛡️ Simple **log system** (`jsvc.log`) to track actions.
* 🎨 Colorized CLI interface via `colorama`.

---

## 🚀 Installation

1. Clone this repository or copy `jsvc.py`.
2. Install dependencies:

```bash
pip install cryptography colorama
```

3. Make the script executable:

```bash
chmod +x jsvc.py
```

4. Run with Python 3:

```bash
./jsvc.py -h
```

---

## 📖 Usage

### 🔹 Push a file

```bash
./jsvc.py -push --file mycode.py
```

This will:

* Encrypt and save `mycode.py` inside `mycode.py.json`.
* Store metadata (author, version, description, tags, etc.).
* Generate a key (`key.key`) for decryption.

**Without encryption:**

```bash
./jsvc.py -push --file mycode.py --no_encrypt
```

**With backup support:**

```bash
./jsvc.py -push --file mycode.py --backup
```

---

### 🔹 Commit files

```bash
./jsvc.py -commit
```

This will:

* Collect all `*.json` files (except backups and `main_repo.json`).
* Merge them into a single `main_repo.json`.
* Include README contents if provided.

---

### 🔹 Help

```bash
./jsvc.py -h
```

---

## 📂 File Structure

```
project/
│── jsvc.py
│── key.key               # Encryption key (if generated)
│── jsvc.log              # Action logs
│── mycode.py             # Your source file
│── mycode.py.json        # Encrypted or plain metadata+code
│── backup mycode.py.json # Backup (if enabled)
│── main_repo.json        # Repo commit file
```

---

## 🔒 Encryption Details

* Uses **Fernet (symmetric encryption)** from Python’s `cryptography` library.
* Each file push generates or reuses a `key.key`.
* Encrypted contents are stored inside the JSON repo file.

---

## ⚡ Example Workflow

```bash
./jsvc.py -push --file script.py --no_encrypt --backup
./jsvc.py -push --file another.py
./jsvc.py -commit
```

Result:

* `script.py.json` (plain text with backup).
* `another.py.json` (encrypted).
* `main_repo.json` containing all repo data.

---

## 📜 License

GPL 3.0 License, do whatever you want, dont close source it.


# 📚 Text File Analyzer

A Python project that reads and analyzes the contents of a `.txt` file to generate useful statistics such as line count, word count, character count, and word frequency. Results are both printed to the terminal and saved to a report file.

---

## 🚀 Features

- Reads a `.txt` file with UTF-8 encoding
- Counts:
  - Total number of lines
  - Total number of words
  - Total number of characters
  - Frequency of each word (case-insensitive)
- Cleans common punctuation before analysis
- Outputs results to:
  - Terminal
  - `report.txt` file inside the `Text analyzer/` folder

---

## 🛠️ Technologies Used

- Python 3.x
- Built-in modules only (no external libraries)

---

## 📂 Project Structure

```plaintext
Text_File_Analyzer/
├── main.py     # Main script
│── sample.txt           # Input text file
│── report.txt           # Output analysis report
└── README.md            # Project documentation

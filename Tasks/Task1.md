# 🚀 Data Engineering Coding Tasks 

This repository contains 4 foundational data transformation tasks split into a `utils` Python package in `Pipelines` folder, complete with an automated testing suite structure.

---

## 📅 Module 1: `utils/datetime_utils.py`

### Task 1: Robust Datetime Parser
* **Function Signature:** `def parse_to_datetime(date_str: str, time_str: str) -> datetime:`
* **Goal:** Merge a date string and a time string into a single unified Python `datetime` object.
* **Requirements:** 
  * Support `date_str` in `"YYYY-MM-DD"` or `"DD.MM.YYYY"`.
  * Support `time_str` in `"HH:MM:SS"`.
* **Test File:** `tests/test_datetime_utils.py`
* **Test Cases to Implement:**
  * Valid ISO format input (`"2026-05-20"`, `"14:30:00"`)
  * Valid European format input (`"20.05.2026"`, `"14:30:00"`)
  * Invalid format input (should return None)

### Task 2: Datetime Rounding to Whole Hours
* **Function Signature:** `def round_to_whole_hour(dt: datetime) -> datetime:`
* **Goal:** Truncate a `datetime` object down to its nearest whole hour (minutes, seconds, and microseconds become `0`).
* **Test File:** `tests/test_datetime_utils.py`
* **Test Cases to Implement:**
  * Standard timestamp truncation (e.g., `14:35:12` ➡️ `14:00:00`)
  * Midnight edge case processing (e.g., `00:05:00` ➡️ `00:00:00`)

---

## 🔤 Module 2: `utils/string_utils.py`

### Task 3: Text Capitalization Normalizer (Title Case)
* **Function Signature:** `def clean_to_title_case(text: str) -> str:`
* **Goal:** Standardize messy strings so every single word starts with a capital letter and all other letters are lowercase.
* **Test File:** `tests/test_string_utils.py`
* **Test Cases to Implement:**
  * ALL CAPS input string
  * completely lowercase input string
  * mixed mEsSy CaSe input string

### Task 4: Email Address Validator
* **Function Signature:** `def is_valid_email(email_str: str) -> bool:`
* **Goal:** Check if an input string is a syntactically valid email format using regular expressions (`re`).
* **Test File:** `tests/test_string_utils.py`
* **Test Cases to Implement:**
  * Standard valid email (returns `True`)
  * Missing `@` symbol (returns `False`)
  * Missing domain extension like `.com` (returns `False`)

---

## 🧪 Running the Tests

 Run the complete test suite from your root repository directory:
   ```bash
   pytest
   ```
   Or setup test explorer UI in Vscode

---

 ⚠️ Do not forget to install new requirements

  ```bash
  pip install --upgrade -r requirements.txt
  ```

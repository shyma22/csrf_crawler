# CSRF Vulnerability Crawler and Research

A Python-based tool that crawls websites, detects HTML forms, and checks for missing CSRF tokens.  
This project was created for **educational and research purposes** to demonstrate how easily overlooked CSRF vulnerabilities can be detected using automation.  

---

## 🧠 Overview

Cross-Site Request Forgery (CSRF) is a common web vulnerability that allows attackers to perform unauthorized actions on behalf of authenticated users.  
This crawler automates the process of finding forms that might be missing CSRF protection fields (like `csrf_token`, `csrfmiddlewaretoken`, etc.).

---

## ⚙️ Features

- Crawls through pages up to a specified depth  
- Detects all forms on each page  
- Checks if a CSRF token field is missing  
- Prints clear alerts in the console for potential vulnerabilities  
- Easy to modify and expand for deeper security analysis  

---

## 📁 Files Included

- `crawl.py` → Main crawler script (Python)  
- `index.html` → Proof of Concept
- `README.md` → Project documentation (this file)  

---
## Implementation

I developed a PHP-based demonstration that simulates a bank transaction webpage intentionally lacking CSRF protection. The proof-of-concept illustrates how an attacker could exploit the missing token to perform unauthorized transactions. The demo is intended to be run locally using XAMPP; relevant screenshots are included below.
![CSRF Vulnerability Alert](cmd.png)
![CSRF Attack](bank.png)


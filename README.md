### 🎂 **Automatic Birthday Wisher Using Python and Task Scheduler**  
**Automate birthday wishes with personalized emails & scheduled execution!**  

![image](https://github.com/user-attachments/assets/44f95997-1df5-4513-b0c7-fbce71f89a00)

---

## 🎉 **About the Project**  
This **Automatic Birthday Wisher** is a Python-based automation system that sends **personalized birthday emails** with optional image attachments. It fetches recipient details from an **Excel-based database** and schedules email delivery using **Cron (Linux) or Windows Task Scheduler**. Ideal for personal and business applications!  

---

## 🚀 **Tech Stack**
| Technology  | Usage |
|------------|--------------------------------|
| **Programming Language** | Python |
| **Email Service** | SMTP (Gmail, Outlook, etc.) |
| **Data Handling** | Microsoft Excel, NumPy |
| **Task Scheduling** | Cron (Linux), Windows Task Scheduler |
| **Automation** | Python Script Execution |

---

## 🎯 **Key Features**
✅ **Automated Birthday Wishing** – Sends personalized emails automatically  
✅ **Excel-Based Database** – Stores recipient names, emails, and birthdays  
✅ **SMTP Email System** – Secure email sending with attachments  
✅ **Task Scheduling** – Works with **Cron** (Linux) and **Windows Task Scheduler**  
✅ **Personalized Greetings** – Custom message templates with recipient name  

---

## **Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/SampathKumarKolichalam/Automatic-Birthday-Wisher.git
cd Automatic-Birthday-Wisher
```

### **2️⃣ Install Dependencies**
```sh
pip install pandas openpyxl smtplib email.mime
```

### **3️⃣ Configure SMTP Settings**  
Edit `config.py` and add your email credentials:
```python
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```
📌 **Important**: If using Gmail, enable **"Less Secure Apps"** or generate an **App Password**.

---

## 📅 **How It Works**
### **Step 1: Store Birthday Data in Excel**
Fill out `birthdays.xlsx` with:
| Name | Email | Birthday |
|------|-------|----------|
| John Doe | johndoe@example.com | 1995-06-15 |

### **Step 2: Run the Script Manually (For Testing)**
```sh
python birthday_wisher.py
```

### **Step 3: Schedule the Script**
#### 🖥️ **Windows Task Scheduler**
1. Open **Task Scheduler** → Click **Create Basic Task**
2. Set trigger: **Daily at 9:00 AM**
3. Select action: **Run a program**
4. Browse & select `python.exe` with the script path.

#### 🐧 **Cron Job (Linux)**
Edit Crontab:
```sh
crontab -e
```
Add this line (Runs every day at 9 AM):
```sh
0 9 * * * /usr/bin/python3 /path/to/birthday_wisher.py
```

---


## 🔥 **Custom Email Template**
Modify `email_template.txt` to personalize the email:
```
Subject: 🎂 Happy Birthday, {name}! 🎉

Dear {name},

Wishing you a fantastic birthday filled with joy and success! 🎈🎁🎂

Best Regards,  
Your Friend
```

---

## 🤝 **Contributing**
💡 **Want to improve this project?**  
Fork the repo, make your changes, and submit a pull request!  

```sh
git clone https://github.com/yourusername/Automatic-Birthday-Wisher-Using-Python-Project.git
git checkout -b feature-branch
git commit -m "Added new feature"
git push origin feature-branch
```

---

## 📜 **License**
This project is free and access to all. Feel free to use and modify it.  

---
## 👨‍💻 **Connect with Me**
📧 Email: [sampathkumarkolichalam@gmail.com]  

🔗 LinkedIn: [https://www.linkedin.com/in/sampath-kumar-kolichalam-18b57b1ab/]

---

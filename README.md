# CampusConnect 📧🤖

CampusConnect is a smart, extensible platform designed to streamline student engagement, automate academic queries, and simplify communication for educational institutions. With features like a student academic chatbot, secure signup, and automated email notifications, CampusConnect is your all-in-one campus assistant!

---

## 🚀 Features

- **Student Academic Chatbot:** Instantly answers student queries about academics, attendance, grades, and more.
- **Secure Signup & Login:** Robust authentication with password hashing and Google OAuth.
- **Automated Email Notifications:** Send emails (with optional attachments) for password resets, announcements, and more.
- **MongoDB Integration:** All user and student data is securely stored and managed.
- **CI/CD Pipeline:** Automated testing and deployment ensure every update is reliable and production-ready.

---

## 👩‍🎓 Who Is It For?

- **Students:** Get instant answers to academic questions and notifications.
- **Faculty & Admins:** Manage student data, send announcements, and automate repetitive tasks.
- **Developers:** Easily extend or integrate CampusConnect into your institution’s digital ecosystem.

---

## 🛠️ How It Works

1. **User Signup:** Students register securely, with email validation and strong password checks.
2. **Chatbot Interaction:** Students can chat with the academic bot for personalized information.
3. **Email Service:** Automated emails (like password resets) are sent using the built-in mail module.
4. **CI/CD Pipeline:** Every code change is automatically tested and deployed, ensuring a smooth and bug-free experience.

---

## ⚡ The Pipeline

CampusConnect uses a **CI/CD pipeline** (Continuous Integration/Continuous Deployment) to:
- Automatically run tests on every code push.
- Deploy updates seamlessly, so users always get the latest features with minimal downtime.
- Ensure code quality and reliability—no more “it works on my machine” moments!

---

## 📦 Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/CampusConnect.git
   cd CampusConnect
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file with your email credentials and MongoDB URI.

4. **Run the app:**
   ```bash
   python std_bot.py
   ```

---

## 📬 Email Module Example

```python
from mail import send_email

send_email(
    subject="Welcome to CampusConnect!",
    body="Thanks for signing up.",
    to_email="student@example.com"
)
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

MIT License

---

**CampusConnect – Making campus life smarter, one message at a time!**

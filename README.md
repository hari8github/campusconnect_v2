

─────────────────────────────────────────────  
# Campus Connect🎓  
─────────────────────────────────────────────  

Campus Connect is a full-stack academic support application designed to help students access their academic information instantly. This web application provides functionalities like AI chatbot assistance, course details, attendance tracking, credit and enrollment status, as well as student comparison tools for academic performance. The project is built with Python Flask as its backend framework and uses MongoDB for data storage. The user interface leverages Tailwind CSS and vanilla JavaScript to provide a responsive and modern UX.

─────────────────────────────  
## Table of Contents 📑  
─────────────────────────────  
- **Project Overview**  
- **Technologies Used**  
- **Features**  
- **Installation and Setup**  
- **Configuration**  
- **File Structure**  
- **API Endpoints and Usage**  
- **Testing and Running Scripts**  
- **Contribution Guidelines**  
- **License**

─────────────────────────────  
## Project Overview  
─────────────────────────────  
Campus Connect v2 is designed to streamline the process of retrieving and analyzing academic data. The application provides an AI chatbot that can answer queries about a student’s courses, GPA, attendance, credit status, and more. It supports user authentication, including traditional email/password login and Google OAuth integration, and offers tools for both students and administrative staff.

─────────────────────────────  
## Technologies Used 💻  
─────────────────────────────  

| **Technology**      | **Description**                                                               |
|---------------------|-------------------------------------------------------------------------------|
| **Python**          | Primary language used to build the Flask backend.                           |
| **Flask**           | Lightweight web framework powering the server and routing logic.            |
| **MongoDB**         | NoSQL database for storing student and academic information.                |
| **pymongo**         | Python library for interacting with MongoDB.                                |
| **Flask-Bcrypt**    | For secure hashing of user passwords.                                         |
| **spaCy**           | Utilized for natural language processing in the Academic Chatbot module.      |
| **Tailwind CSS**    | CSS framework used for styling the HTML templates.                          |
| **JavaScript**      | Handles client-side interactions, including dynamic updates and sorting.    |
| **Flask-Dance**     | Used to integrate Google OAuth for user authentication.                     |

─────────────────────────────  
## Features 🚀  
─────────────────────────────  

- **AI Chatbot Assistant:**  
  The chatbot (implemented in modules like test2.py) uses spaCy for parsing natural language queries. It supports multiple intents such as overall performance, course details, attendance, semester-specific performance, credit status, and course load information.

- **User Authentication:**  
  The application supports login and signup functionalities with encrypted password storage. It also integrates Google OAuth using Flask-Dance.

- **MongoDB Integration:**  
  The system uses MongoDB Atlas to store and retrieve student academic data. Utility scripts (such as insert.py) handle data insertion.

- **Email Functionality:**  
  The mail module uses SMTP to send emails. This feature is useful for account verifications, password resets, or notifications.

- **Dynamic Student Comparison:**  
  Users can compare academic details between two students. Data such as GPA, credits completed, and attendance are displayed in interactive tables.

- **Dynamic Sorting and Filtering:**  
  Client-side JavaScript in the static files enables the sorting of common academic details dynamically.

─────────────────────────────  
## Installation and Setup  
─────────────────────────────  

### Requirements  
- Python 3.8+  
- MongoDB Atlas Account (or local MongoDB instance)  
- pip package installer  

### Installation Steps  
1. **Clone the Repository:**  
   Run the following command in your terminal:  
   <code>git clone https://github.com/hari8github/campusconnect_v2.git</code>

2. **Create a Virtual Environment:**  
   For example:  
   <pre>
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
   </pre>

3. **Install Dependencies:**  
   Navigate to the project root directory and install all required packages:  
   <pre>
pip install -r requirements.txt
   </pre>

4. **Set Up Environment Variables:**  
   Create a <code>.env</code> file in the root directory and define the following variables:  
   <pre>
MONGODB_URI=<YOUR_MONGODB_URI>
EMAIL_ADDRESS=<YOUR_EMAIL_ADDRESS>
EMAIL_PASSWORD=<YOUR_EMAIL_PASSWORD>
GOOGLE_CLIENT_ID=<YOUR_GOOGLE_CLIENT_ID>
GOOGLE_CLIENT_SECRET=<YOUR_GOOGLE_CLIENT_SECRET>
   </pre>

─────────────────────────────  
## Configuration ⚙️  
─────────────────────────────  

- **Database:**  
  Update the MongoDB URI in the <code>.env</code> file. The collection and database names are configured in both the main Flask application (<code>std_bot.py</code>) and the chatbot module (<code>test2.py</code>).

- **Email Settings:**  
  The <code>mail.py</code> module reads email credentials from the <code>.env</code> file. Adjust these credentials as required.

- **Google OAuth:**  
  Use your credentials from the Google Cloud Console to authorize users via Google login.

─────────────────────────────  
## File Structure Overview 📁  
─────────────────────────────  

The project is organized as follows:

| **File/Folder**      | **Purpose**                                                       |
|----------------------|-------------------------------------------------------------------|
| **std_bot.py**       | Main Flask application that initializes routes, authentication, and chatbot integration. |
| **test2.py**         | Contains the StudentAcademicChatbot class with NLP, MongoDB connection, and multiple intent mapping. |
| **insert.py**        | Script to insert student data into MongoDB from a JSON file.      |
| **mail.py**          | Module to handle email sending via SMTP with attachment support.  |
| **templates/**       | HTML templates for various pages (login, signup, forgot password, etc.). |
| **static/**          | JavaScript files (e.g., test.js) and CSS assets for frontend interactions.         |
| **.env**             | Contains environment variables used for configuration.            |

─────────────────────────────  
## API Endpoints and Usage 🔌  
─────────────────────────────  

Below is a summary table of commonly used API endpoints and their functionalities:

| **Endpoint**                         | **Method** | **Description**                                                                                |
|--------------------------------------|------------|------------------------------------------------------------------------------------------------|
| <code>/</code>                        | GET        | Loads the login page.                                                                          |
| <code>/login</code>                   | GET/POST   | Handles user login with standard form data or JSON payload.                                   |
| <code>/signup</code>                  | GET/POST   | Manages user registration (handled with a Flask Blueprint in <code>signup.py</code>).           |
| <code>/handle_common_details_query</code> | GET        | Retrieves common academic details and returns sorted student academic information.             |
| <code>/reset_password</code> (template) | GET        | Displays a form for resetting the user password (handled in the forgot_password.html template). |

**Usage Example:**  
To launch the application locally, use the command:  
<pre>
flask run
</pre>  
Then, navigate to <code>http://localhost:5000</code> in your web browser.

─────────────────────────────  
## Testing and Running Scripts 🧪  
─────────────────────────────  

- **Data Insertion:**  
  Run the <code>insert.py</code> script to populate the MongoDB database:  
  <pre>
python insert.py
  </pre>  

- **Email Test:**  
  Use the <code>mail.py</code> script to send a test email. Ensure your environment variables are set correctly.

- **JavaScript:**  
  The <code>static/test.js</code> file contains client-side logic for handling AJAX calls, student comparisons, and dynamic data sorting in the common details table.

─────────────────────────────  
## Contribution Guidelines 🤝  
─────────────────────────────  

Contributions to Campus Connect are welcome! Please follow these guidelines when contributing:  

- **Fork** the repository and create a new branch for your feature or bug fix.  
- **Write clean, documented code** that follows the project’s style.  
- **Test your changes** thoroughly before submitting a pull request.  
- **Submit a pull request** with a clear description of your changes and the problem they solve.

─────────────────────────────  
## License 📄  
─────────────────────────────  

This project is licensed under an open-source license. Please check the LICENSE file in the repository for more details.

─────────────────────────────  
## Final Notes  
─────────────────────────────  

Campus Connect v2 integrates modern web practices with robust backend functionality to provide an effective academic support tool. Its use of natural language processing for interpreting multiple academic query intents, along with dynamic data presentation on the front end, makes it a powerful resource for both students and administrators. Enjoy exploring and contributing to the project!  

Happy Coding! 🚀

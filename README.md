# smart_attendance_system

## 📖 **Project Overview**

The **Smart Attendance Manager** is an innovative system built using **Facial Recognition Technology** to automate the process of taking attendance. The system uses real-time facial recognition to mark attendance, making the process more accurate and efficient. This eliminates manual errors and saves time. 

### **Key Features:**
- Real-time facial recognition for attendance tracking.
- Automatic marking of attendance based on face detection.
- Admin interface for managing student records.
- Attendance reports and analytics.
- Integration with a database to track attendance over time.
- Easy to deploy and use.

---

## ⚙️ **Tech Stack**

- **Backend**: Python (Flask/Django)
- **Frontend**: HTML, CSS, JavaScript (optional: React for dynamic UI)
- **Machine Learning**: OpenCV, Dlib, Face Recognition
- **Database**: SQLite/MySQL/PostgreSQL
- **Libraries**:
  - **Face Recognition** (for facial recognition)
  - **OpenCV** (for image processing)
  - **Flask/Django** (for web server)
  - **NumPy** and **Pandas** (for data handling)

---

## 🔧 **Installation & Setup**

Follow the steps below to set up the project locally:

### Prerequisites:
- Python 3.x+
- Pip (Python package installer)

### Steps to Run Locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mahaklachhwani-0412/smart-attendance-manager.git
    cd smart-attendance-manager
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database**:
    ```bash
    python manage.py migrate  # For Django
    ```

6. **Start the application**:
    ```bash
    python app.py  # For Flask
    ```

7. **Access the app**:
    Open your browser and go to `http://localhost:5000` (or the respective port).

---

## 📸 **Usage**

### **For Admins**:
- **Enroll Students**: 
  - Capture student faces by selecting the **"Enroll Student"** option from the Admin Panel. 
  - The system will save the student's face for later recognition.

- **View Attendance**: 
  - Admin can access detailed reports of attendance for each student over specific periods.

### **For Students**:
- **Mark Attendance**: 
  - The system will automatically mark attendance based on the detected face when the student enters the camera frame.

- **View Attendance**: 
  - Students can view their individual attendance status from the system’s dashboard.

---


## 🖥️ **Screenshots**

![Screenshot 1](https://via.placeholder.com/600x400)
*Admin Panel View*

![Screenshot 2](https://via.placeholder.com/600x400)
*Student Attendance Dashboard*

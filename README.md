# Smart Attendance System Using Facial Recognition

## 📖 Project Overview

The **Smart Attendance System** automates attendance marking using **Facial Recognition**. Students' faces are detected from uploaded images, and attendance is recorded in Excel and PDF formats. This system reduces manual errors and saves time.

### Key Features
- Automatic attendance marking from images.
- Face recognition using **Facenet (MTCNN + InceptionResnetV1)**.
- Attendance records saved in Excel and downloadable as PDF.
- Streamlit web interface for easy interaction.
- Temporary image handling and training of new models.

---

## ⚙️ Tech Stack

- **Backend & Interface**: Python, Streamlit  
- **Machine Learning**: PyTorch, Facenet-PyTorch  
- **Image Processing**: OpenCV, PIL  
- **Data Handling**: Pandas, NumPy  
- **PDF Generation**: ReportLab, FPDF  

---

## 🔧 Installation & Setup

### Prerequisites:
- Python 3.8+
- Pip

### Steps to Run Locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mahkkk04/Smart-attendance-using-facial-recognition.git
    cd smart-attendance-system
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:
    ```bash
    streamlit run streamlit_app.py
    ```

5. **Access the app**:
    Open your browser at `http://localhost:8501`.

---

## 📸 Usage

### **Train Model**
- Upload or place images of registered students in `registered_faces/`.
- Go to **"Train Model"** in the sidebar and click **"Train Now"** to update embeddings.

### **Mark Attendance**
- Upload student images via **"Mark Attendance"**.
- Click **"Mark Attendance"** to detect faces and save attendance.
- Temporary images are cleared using **"Clear Uploaded Images"**.

### **Download Attendance PDF**
- Go to **"Download Attendance PDF"**.
- Select the Excel attendance file and download it as a PDF.

---

## 🗂️ Folder Structure
- registered_faces/           # Contains student face images
- Attendance/                 # Generated Excel attendance sheets
- reports/                    # Generated PDF reports
- streamlitapp.py             # Main Streamlit app
- attendance_system.py        # Face recognition & attendance logic
- train_model.py              # Model training logic
- train_config.yml            # Training configuration

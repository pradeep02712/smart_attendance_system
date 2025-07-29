import cv2
import torch
import pandas as pd
import numpy as np
from datetime import datetime
from facenet_pytorch import MTCNN, InceptionResnetV1
import os

device = 'cuda' if torch.cuda.is_available() else 'cpu'
mtcnn = MTCNN(keep_all=True, device=device)
resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)

# Load known faces
def load_known_embeddings(data_dir='registered_faces'):
    known_embeddings = []
    known_names = []

    for name in os.listdir(data_dir):
        person_dir = os.path.join(data_dir, name)
        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face = mtcnn(img_rgb, return_prob=True)[0]
            if face is not None:
                embedding = resnet(face.to(device)).detach().cpu().numpy()
                known_embeddings.append(embedding)
                known_names.append(name)

    return np.vstack(known_embeddings), known_names

known_embeddings, known_names = load_known_embeddings()

# Save attendance to Excel
def save_attendance(marked_names):
    if not marked_names:
        return []

    now = datetime.now()
    date_str = now.strftime('%d-%m-%Y')
    time_str = now.strftime('%H:%M:%S')

    structured_attendance = []

    for full_name in marked_names:
        if '_' in full_name:
            er, name = full_name.split('_', 1)
        else:
            er = "Unknown"
            name = full_name

        structured_attendance.append({
            'ER Number': er,
            'Name': name,
            'Date': date_str,
            'Time': time_str
        })

    # Save to Excel
    df = pd.DataFrame(structured_attendance)
    os.makedirs("Attendance", exist_ok=True)
    excel_path = f"Attendance/attendance_{date_str}.xlsx"
    df.to_excel(excel_path, index=False)

    # Return list of tuples for PDF (in correct order)
    return [(row['ER Number'], row['Name'], row['Date'], row['Time']) for row in structured_attendance]


# 1. Attendance from Image(s)
def mark_attendance_from_images(image_paths):
    marked_names = []

    # Safety check: ensure known embeddings and names are loaded
    if len(known_embeddings) == 0 or len(known_names) == 0:
        print("No known embeddings or names loaded.")
        return save_attendance(marked_names)

    for image_path in image_paths:
        img = cv2.imread(image_path)
        if img is None:
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes, probs = mtcnn.detect(img_rgb)
        faces = mtcnn(img_rgb)

        if faces is not None and boxes is not None:
            for face_tensor, box in zip(faces, boxes):
                if face_tensor is None:
                    continue

                embedding = resnet(face_tensor.unsqueeze(0).to(device)).detach().cpu().numpy()

                if known_embeddings.shape[0] == 0 or embedding.shape[0] == 0:
                    continue

                distances = np.linalg.norm(known_embeddings - embedding, axis=1)

                if distances.size == 0 or len(known_names) == 0:
                    continue

                min_index = np.argmin(distances)

                if 0 <= min_index < len(known_names):
                    print(f"[DEBUG] Closest match: {known_names[min_index]}, Distance: {distances[min_index]:.4f}")
                    if distances[min_index] < 1.0:  # Increased threshold
                        name = known_names[min_index]
                    else:
                        name = "Unknown"
                else:
                    print("[DEBUG] Invalid index or no match.")
                    name = "Unknown"

                if name != "Unknown" and name not in marked_names:
                    marked_names.append(name)

    return save_attendance(marked_names)

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_attendance_pdf(attendance_list, filename="attendance_report.pdf"):
    pdf_path = os.path.join("reports", filename)
    os.makedirs("reports", exist_ok=True)

    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Attendance Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 70, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.drawString(50, height - 100, "Name")
    c.drawString(250, height - 100, "Enrollment No")
    c.drawString(450, height - 100, "Status")

    y = height - 120
    for name, er_no in attendance_list:
        c.drawString(50, y, name)
        c.drawString(250, y, er_no)
        c.drawString(450, y, "Present")
        y -= 28

    c.save()
    return pdf_path


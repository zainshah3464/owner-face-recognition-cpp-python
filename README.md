# 👁️ Owner Face Recognition System (C++ + Python)

A cross-language project that uses C++ to securely launch a Python-based face recognition script. This fun-yet-functional system verifies Zain's face using OpenCV and roasts anyone who isn't him 😆

---

## 💡 Features

- Face detection using OpenCV
- LBPH-based face recognition
- Roasts intruders with random messages
- Real-time webcam feed
- C++ launcher to run Python securely
- Personal welcome for Zain only

---

## 🚀 Tech Stack

- C++
- Python 3
- OpenCV
- LBPHFaceRecognizer
- `system()` command for C++ ⇨ Python

---

## 🛠 How to Run

### Step 1: Train the model (run separately beforehand)
> Save as `trainer.yml`

### Step 2: Setup paths in `main.cpp`

```cpp
std::string command = R"(python "full/path/to/face_unlock.py")";
Step 3: Compile and run C++:
bash
Copy
Edit
g++ main.cpp -o face_launcher
./face_launcher


🧑‍💻 Author
Syed Zain Ali Shah
GitHub Profile

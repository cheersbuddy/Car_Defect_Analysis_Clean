
# 🛠️ AI-Powered Car Defect Detection System using YOLOv7 & CNN

## 📌 Overview

Ensuring vehicle quality before sale is a critical requirement in automotive manufacturing. Surface defects like scratches, dirt, and paint overflow not only affect aesthetics but can also compromise overall performance. Traditional manual inspections are time-consuming, subjective, and error-prone.

This project introduces a fully automated image-based **defect detection system** that uses:
- **YOLOv7** for real-time defect localization
- **CNNs** for precise defect classification

By automating the inspection process, the system significantly reduces labor costs, inspection time, and inconsistency — improving accuracy and boosting customer satisfaction.

---

## 📊 Key Implementation Modules

| Module                    | Tool/Library               | Functionality                          | Outcome                                   |
|---------------------------|----------------------------|----------------------------------------|--------------------------------------------|
| Data Collection & Annotation | Roboflow, Lightroom        | Image capture and labeling             | Annotated dataset of car surface defects   |
| Image Classification (CNN)  | PyTorch, TensorFlow, Keras | Defect type recognition                | Classified image categories                |
| YOLOv7 Training             | YOLOv7, PyTorch             | Real-time defect localization          | Bounding boxes with labels                 |
| Web Integration & Deployment| Flask, HTML/CSS, Anaconda  | Web interface for image upload & result| Real-time detection on the website         |
| Algorithm Used              | CNN, YOLOv7                 | Image classification and detection     | Accurate and fast defect identification    |

---

## 🧠 Key Features

- ⚙️ Real-time defect detection and classification
- 🧠 Deep learning-powered accuracy with YOLOv7 + CNN
- 🖼️ Input via annotated car surface images
- 📊 Output includes bounding boxes, defect types, and severity levels
- 🌐 Flask-based web interface for easy access and testing

---

## 🔍 Sample Workflow

1. **Upload an image** of a car surface via the Flask web interface
   
3. The model detects regions with **scratches, dents, or paint issues**
   
5. Bounding boxes are drawn and classified in real time
   
7. Users can **review, validate, or download results**
   

---

> 📁 Note: Images and datasets have been excluded from this repo.  
> You can [download sample files here](https://your-google-drive-link) and place them in the appropriate folder.

---

## 📦 Setup & Run Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/car-defect-detection.git
   cd car-defect-detection


2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

4. **Open in browser**

   ```
   http://127.0.0.1:5000/
   ```

---

## 🧪 Performance Metrics

| Metric          | Score        |
| --------------- | ------------ |
| Precision       | 89%+         |
| Recall          | 87%+         |
| F1-Score        | 88%+         |
| Detection Speed | \~25ms/image |

---

## 📁 File Structure (Minimal)

```
├── app.py
├── main.py
├── detect.py
├── static/
│   └── [UI assets]
├── templates/
│   └── index.html
├── models/
│   └── [YOLO/CNN architecture]
├── utils/
│   └── [helper functions]
├── requirements.txt
└── README.md
```

---

## 🧠 Tech Stack

* **Languages**: Python, HTML/CSS
* **Libraries**: PyTorch, TensorFlow, OpenCV, Flask
* **Models**: YOLOv7, Convolutional Neural Networks (CNN)
* **Tools**: Roboflow, Lightroom, Anaconda

---

## 🙌 Acknowledgements

Special thanks to our mentor and the project review team for their guidance and support throughout the development of this solution.

---

## 🚀 Future Scope

* Deployment to cloud platforms (AWS EC2 / Azure)
* Integration with Manufacturing Execution Systems (MES)
* Support for real-time video defect analysis

---



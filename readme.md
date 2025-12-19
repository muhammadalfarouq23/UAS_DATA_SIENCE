# KLASIFIKASI PARFUM BERDASARKAN PEMBACAAN SENSOR BAU GENGGAM

## 👤 Informasi Proyek
- **Nama Mahasiswa** : Muhammad Aulia Al Farouq
- **Mata Kuliah**    : Data Science / Machine Learning
- **Repository**     : https://github.com/muhammadalfarouq23/UAS_DATA_SIENCE
- **Video Demo**     : https://youtu.be/MsR0Dn6DH0g

---

## 🎯 1. Ringkasan Proyek
Proyek ini bertujuan untuk melakukan **klasifikasi jenis parfum** berdasarkan **pembacaan sensor bau genggam (electronic nose)** menggunakan pendekatan Machine Learning dan Deep Learning.

Tahapan utama proyek:
- Data preparation & preprocessing
- Exploratory Data Analysis (EDA)
- Pembangunan 3 model:
  - Baseline Model
  - Advanced Machine Learning Model
  - Deep Learning Model (MLP)
- Evaluasi performa model
- Penentuan model terbaik

---

## 📄 2. Problem & Goals

### Problem Statement
1. Data pembacaan sensor bau memiliki pola kompleks dan sulit dibedakan secara manual.
2. Diperlukan model klasifikasi untuk mengenali jenis parfum berdasarkan sinyal sensor.

### Goals
1. Membangun sistem klasifikasi parfum berbasis data sensor bau.
2. Membandingkan performa model Machine Learning dan Deep Learning.
3. Menentukan model terbaik berdasarkan metrik evaluasi.

---

## 📁 3. Struktur Folder
project/
│
├── data/ # Dataset (tidak di-upload ke GitHub)
│
├── notebooks/ # Notebook eksperimen
│ └── parfum_classification.ipynb
│
├── src/ # Source code (opsional)
│
├── models/ # Model tersimpan
│ ├── model_baseline.pkl
│ ├── model_advanced.pkl
│ └── model_mlp.h5
│
├── images/ # Visualisasi hasil
│
├── requirements.txt
├── .gitignore
└── README.md


---

## 📊 4. Dataset

- **Sumber Dataset** : Data pembacaan sensor bau genggam
- **Jumlah Data**    : 19 baris
- **Jumlah Fitur**   : 29 fitur
- **Tipe Data**      : Tabular (Numerik + Label Kategori)
- **Ukuran File**    : ±61.4 KB
- **Format File**    : CSV / Excel

### Contoh Fitur
| Fitur | Deskripsi |
|------|-----------|
| S1 - S28 | Nilai sensor bau |
| Label | Jenis parfum |

---

## 🔧 5. Data Preparation

Tahapan preprocessing:
- Pengecekan missing value
- Normalisasi fitur menggunakan **StandardScaler**
- Encoding label target
- Pembagian data:
  - Training set
  - Validation set
  - Test set

---

## 🤖 6. Modeling

### Model 1 – Baseline
- **Algoritma**: Logistic Regression  
- **Tujuan**: Sebagai tolok ukur performa awal  
- **Kelebihan**: Sederhana dan cepat  

---

### Model 2 – Advanced Machine Learning
- **Algoritma**: Random Forest Classifier  
- **Alasan**: Mampu menangkap hubungan non-linear antar fitur sensor  

---

### Model 3 – Deep Learning (WAJIB)
- **Arsitektur**: Multilayer Perceptron (MLP)  
- **Jenis**: Deep Learning untuk data tabular  

**Arsitektur Singkat:**
- Input Layer
- Dense 64 (ReLU)
- Dropout 0.2
- Dense 32 (ReLU)
- Output Layer (Softmax)

---

## 🧪 7. Evaluation

### Metrik Evaluasi
- Accuracy
- Confusion Matrix
- Classification Report

### Ringkasan Hasil
| Model | Accuracy | Catatan |
|------|----------|--------|
| Baseline | Rendah | Model sederhana |
| Advanced | Lebih baik | Menangkap pola non-linear |
| Deep Learning | Terbaik | Performa paling stabil |

---

## 🏁 8. Kesimpulan
- **Model terbaik**: Multilayer Perceptron (MLP)
- **Alasan**: Memberikan akurasi tertinggi dan stabil
- **Insight penting**: Normalisasi data sangat berpengaruh pada performa Deep Learning

---

## 🔮 9. Future Work
- Menambah jumlah data sensor
- Feature engineering lanjutan
- Hyperparameter tuning
- Mencoba arsitektur Deep Learning lain
- Deployment sebagai aplikasi web/API

---

## 🔁 10. Reproducibility

### Environment
- Python 3.10

### Library Utama


numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
tensorflow==2.14.0
joblib==1.3.2

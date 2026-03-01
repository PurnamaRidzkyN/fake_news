# Fake News Detection System 🛡️

Project ini adalah sistem berbasis web yang dikembangkan untuk mengidentifikasi apakah sebuah berita bersifat asli atau palsu secara otomatis. Project ini dibuat untuk memenuhi tugas mata kuliah dan saat ini masih dalam status **Work in Progress (WIP)**.

---

## 📌 Deskripsi Project

Tujuan utama dari project ini adalah mengimplementasikan algoritma Machine Learning untuk melakukan klasifikasi teks pada artikel berita. Pengguna dapat memasukkan teks berita, dan sistem akan memberikan prediksi probabilitas keaslian berita tersebut.

> **Status:** ⚠️ *Under Development*. Fitur, model, dan tech stack masih dapat berubah.

---

## 🚀 Fitur Utama

* **Deteksi Otomatis:** Klasifikasi berita (Real vs Fake) secara instan
* **Web Interface:** Antarmuka sederhana menggunakan Flask
* **NLP Pipeline:** Preprocessing teks sebelum prediksi
* **Isolated Environment:** Menggunakan Python virtual environment (venv)

---

## 🛠️ Tech Stack (Subjek Perubahan)

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (dapat berubah)
* **Frontend:** HTML, CSS
* **Data Handling:** Pandas, NumPy
* **Environment:** venv (Python Virtual Environment)

---

## ⚙️ Prasyarat

Pastikan sudah terinstall:

* Python **3.10.x**
* pip

Cek versi:

```bash
python --version
pip --version
```

---

## ⚙️ Cara Menjalankan (Local Setup)

Ikuti urutan langkah berikut.

---

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/fake-news-detection.git
cd fake-news-detection
```

---

### 2️⃣ Buat Virtual Environment (Python 3.10)

**Windows**

```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3.10 -m venv venv
source venv/bin/activate
```

Verifikasi:

```bash
python --version
```

Harus menunjukkan **Python 3.10.x**

---

### 3️⃣ Install Dependencies (WAJIB)

Pastikan venv sudah aktif, lalu jalankan:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Jalankan Aplikasi

```bash
python app.py
```

Buka browser:

```
http://127.0.0.1:5000
```

---

## 📂 Struktur Folder

```text
fake-news-detection/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── model/
├── notebook/
├── static/
├── templates/
│
└── venv/   (tidak di-push ke Git)
```

> Folder `venv/` harus dimasukkan ke `.gitignore`.

---

## 👥 Tim Pengembang

| Nama                         | Peran        |
|------------------------------|--------------|
| Purnama Ridzky Nugraha       | Ketua Tim    |
| Anggota 2                    | Anggota      |
| Anggota 3                    | Anggota      |
| Anggota 4                    | Anggota      |
| Anggota 5                    | Anggota      |
---

## 📜 Lisensi & Hak Cipta

Project ini dikembangkan untuk tujuan akademik.

* **Kepemilikan:** Hak milik tim pengembang
* **Penggunaan:** Tidak untuk komersial tanpa izin
* **Modifikasi:** Diizinkan untuk pembelajaran dengan mencantumkan kredit

Detail lisensi tersedia pada file `LICENSE`.

---

## 🧪 Catatan Pengembangan

Project masih tahap awal dan dapat berubah:

* Model ML
* Dataset
* Tech stack
* Struktur aplikasi

Performa sistem akan terus ditingkatkan selama masa pengembangan.

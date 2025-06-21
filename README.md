# Discrete-Mathematics-Paper---Enemy-AI-Movement-in-Lethal-Company-as-a-Hamiltonian-Path-Heuristic-
# Analisis dan Visualisasi AI Musuh Lethal Company

Repositori ini berisi dekonstruksi, analisis, dan visualisasi dari mekanisme pencarian jalur (*pathfinding*) yang digunakan oleh AI musuh dalam game populer, **Lethal Company**. Tujuan utama proyek ini adalah untuk memahami logika di balik pergerakan AI, memodelkannya sebagai masalah teoretis, dan membandingkan efektivitasnya dengan algoritma standar.

Proyek ini terinspirasi dari makalah "Enemy AI Movement Model in Lethal Company as a Hamiltonian Path Heuristic with Precision Radius Analysis".

## 📜 Deskripsi

AI di Lethal Company menunjukkan perilaku patroli yang tampak acak namun metodis. Dengan menganalisis kode sumber `EnemyAI.cs`, kita dapat mengidentifikasi bahwa AI menggunakan varian dari algoritma **Nearest Neighbor (NN)** untuk menentukan jalur patrolinya, yang dapat dimodelkan sebagai upaya untuk menyelesaikan **Traveling Salesperson Problem (TSP)**.

Proyek ini membedah heuristik unik tersebut dan membandingkannya dengan implementasi NN klasik untuk mengevaluasi efisiensi dan tujuannya dari perspektif desain game.

## ✨ Fitur Utama

  * **Kode Sumber Referensi:** Berisi file `EnemyAI.cs` dari *Lethal Company* sebagai dasar analisis.
  * **Visualisasi Algoritma:** Script Python untuk memvisualisasikan lintasan yang dihasilkan oleh AI secara grafis.
  * **Analisis Komparatif:** Perbandingan *head-to-head* antara heuristik unik yang digunakan *Lethal Company* dengan algoritma klasik *Nearest Neighbor*.
  * **Model Teoretis:** Pembahasan dan visualisasi mengenai bagaimana perilaku AI dapat dimodelkan sebagai *Traveling Salesperson Problem* (TSP) dan jalur Hamiltonian.

## 📁 Isi Repositori

  * `EnemyAI.cs`: Kode C\# asli dari AI musuh di *Lethal Company*. Digunakan sebagai dasar untuk analisis logika pergerakan.
  * `visualize_ai_path.py` (atau nama file Python Anda): Script Python utama yang berisi logika untuk:
      * Menjalankan simulasi pergerakan AI.
      * Memvisualisasikan lintasan dengan heuristik **Klasik Nearest Neighbor**.
      * Memvisualisasikan lintasan dengan heuristik **Gaya Lethal Company**.
      * Menghitung dan membandingkan total bobot (jarak) dari kedua lintasan.

## 🚀 Memulai

Untuk menjalankan script visualisasi di komputer Anda, ikuti langkah-langkah berikut.

### Prasyarat

Pastikan Anda telah menginstal Python dan library yang dibutuhkan.

  * Python (3.7+ direkomendasikan)
  * Matplotlib
  * NetworkX
  * NumPy

Anda dapat menginstal semua library yang diperlukan dengan satu perintah:

```sh
pip install matplotlib networkx numpy
```

### Penggunaan

1.  **Clone repositori ini:**

    ```sh
    git clone https://github.com/NAMA_PENGGUNA_ANDA/NAMA_REPOSITORI_ANDA.git
    ```

2.  **Pindah ke direktori proyek:**

    ```sh
    cd NAMA_REPOSITORI_ANDA
    ```

3.  **Jalankan script visualisasi:**

    ```sh
    python visualize_ai_path.py
    ```

4.  Script akan menghasilkan dan menampilkan dua plot visualisasi yang membandingkan kedua algoritma. Total bobot (efisiensi) dari setiap lintasan akan ditampilkan pada judul plot dan di konsol.

## 📊 Hasil Analisis

Analisis dan simulasi menunjukkan temuan kunci sebagai berikut:

1.  **Heuristik Unik:** AI *Lethal Company* **tidak** menggunakan algoritma *Nearest Neighbor* (NN) klasik. Sebaliknya, ia menggunakan modifikasi unik di mana node target berikutnya dipilih berdasarkan kedekatannya dengan node yang **dikunjungi sebelumnya**, bukan dari node **saat ini**.

2.  **Suboptimal secara Matematis:** Heuristik ini terbukti menghasilkan lintasan yang **kurang optimal** dengan total bobot jarak yang lebih tinggi dibandingkan dengan NN klasik.

3.  **Efektif dalam Desain Game:** "Ketidakefisienan" ini tampaknya merupakan **pilihan desain yang disengaja**. Perilaku yang tidak dapat diprediksi dan jalur yang tidak logis membuat AI musuh terasa lebih organik, menantang, dan sulit dieksploitasi oleh pemain.

**Kesimpulan:** Pengembang game secara sadar mengorbankan efisiensi matematis demi menciptakan pengalaman bermain yang lebih dinamis dan menegangkan.

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detailnya.

## 🙏 Ucapan Terima Kasih

  * Kepada **Zeekerss**, pengembang *Lethal Company*, untuk telah menciptakan game dengan mekanik AI yang menarik untuk dianalisis.
  * Kepada komunitas *open-source* untuk library Python yang luar biasa seperti Matplotlib dan NetworkX.

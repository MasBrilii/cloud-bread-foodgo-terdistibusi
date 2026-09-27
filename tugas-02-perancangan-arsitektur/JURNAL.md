# Jurnal Proses — Tugas 2 Perancangan Arsitektur FoodGo

**Kelompok:** cloud-bread-foodgo-terdistibusi

| Nama | NIM | Kontribusi |
|---|---|---|
| SALMAN ALFARIZI | 103072400047 | Pemilihan arsitektur, API Gateway, dan diagram |
| MUHAMMAD AUBERT FAWWAZ PRAYITNO | 103072400169 | Komponen service dan komunikasi |
| BRILIANT DAHSYAT ANUGRAH | 103072400164 | Skenario end-to-end, trade-off, dan kesimpulan |

---

# 1. Diskusi Pemilihan Arsitektur

## 1.1 Masalah yang Dibawa dari Tugas 1

Kelompok kembali melihat hasil Tugas 1, terutama masalah karena
beberapa modul FoodGo masih berada dalam satu sistem monolithic.

Dari pembahasan tersebut, kelompok menyimpulkan bahwa modul Order,
Payment, Restaurant, dan Courier perlu dipisahkan agar tidak terlalu
bergantung pada satu bagian sistem.

## 1.2 Pilihan SOA

Kelompok membahas Service-Oriented Architecture karena SOA dapat
digunakan untuk memisahkan fungsi sistem menjadi beberapa service.

Dari sini kelompok menentukan beberapa service utama, yaitu Order,
Payment, Restaurant Catalog, dan Courier/Notification.

## 1.3 Pilihan Publish-Subscribe

Kelompok kemudian membahas Publish-Subscribe untuk komunikasi yang
tidak harus dilakukan secara langsung.

Kelompok mempertimbangkan penggunaan Message Broker sebagai perantara
event.

## 1.4 Keputusan Akhir

Setelah membandingkan kebutuhan FoodGo, kelompok memutuskan untuk
menggunakan kombinasi SOA + Publish-Subscribe.

SOA digunakan untuk memisahkan service utama, sedangkan
Publish-Subscribe digunakan untuk komunikasi berbasis event.

---

# 2. Penentuan Komponen

Komponen yang ditentukan kelompok:

1. API Gateway
2. Order Service
3. Payment Service
4. Restaurant Catalog Service
5. Courier/Notification Service
6. Message Broker

Kelompok tidak menambahkan terlalu banyak komponen lain agar rancangan
tetap sesuai dengan kebutuhan tugas dan tidak menjadi terlalu kompleks.

---

# 3. Penentuan Komunikasi

Kelompok menentukan bahwa Order Service dan Payment Service
menggunakan request-response karena Order membutuhkan hasil pembayaran.

Order Service juga melakukan request kepada Restaurant Catalog Service
untuk mendapatkan informasi katalog/menu.

Untuk komunikasi event, Order Service menghasilkan event `OrderCreated`
dan mengirimkannya melalui Message Broker.

Courier/Notification Service menjadi subscriber dari event tersebut.

---

# 4. Perancangan Diagram

Diagram dibuat menggunakan Mermaid.

Komponen yang dimasukkan ke diagram adalah API Gateway, Order Service,
Payment Service, Restaurant Catalog Service, Courier/Notification
Service, dan Message Broker.

Jenis komunikasi juga ditampilkan agar alur synchronous dan asynchronous
dapat dibedakan.

---

# 5. Review Terhadap Requirement

| Requirement | Status |
|---|---|
| Memilih SOA/Pub-Sub | Selesai |
| Menjelaskan alasan kombinasi | Selesai |
| Minimal 4 komponen | Selesai |
| Menunjukkan interaksi antar-komponen | Selesai |
| Skenario end-to-end | Selesai |
| Menjelaskan synchronous/asynchronous | Selesai |
| Menjelaskan request-response/event | Selesai |
| Analisis coupling | Selesai |
| Trade-off | Selesai |

---

# 6. Log Penggunaan AI

| Tanggal | Tool AI | Prompt / Penggunaan | Hasil yang Digunakan |
|---|---|---|---|
| 27 September 2026 | ChatGPT | Meminta penjelasan materi SOA, Publish-Subscribe, API Gateway, dan Message Broker untuk memahami tugas | Membantu memahami konsep dan menentukan pilihan arsitektur |
| 27 September 2026 | ChatGPT | Meminta bantuan menyusun rancangan arsitektur FoodGo berdasarkan requirement tugas | Membantu menentukan komponen dan pola komunikasi |
| 27 September 2026 | ChatGPT | Meminta penyusunan README dan jurnal berdasarkan hasil keputusan kelompok | Digunakan untuk membantu penyusunan dokumentasi tugas |
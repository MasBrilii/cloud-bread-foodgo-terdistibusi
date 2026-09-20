# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## 20 September 2026
- Peserta: Salman, Briliant, Fawwaz
- Poin diskusi: membaca skenario FoodGo dan menentukan masalah yang paling sesuai
  untuk dianalisis sebagai pitfall sistem terdistribusi.
- Awalnya kami membahas beberapa kemungkinan masalah dari skenario, kemudian
  membaginya menjadi tiga bagian agar setiap anggota memiliki satu pitfall.
- Salman membahas **The Network Is Reliable**, terutama bagian skenario yang
  menganggap network selalu reliable dan tidak membutuhkan retry. Pembahasan
  juga diarahkan ke penggunaan timeout dan retry serta trade-off dari keduanya.
- Fawwaz membahas **Latency Is Zero**, dengan fokus pada waktu yang dibutuhkan
  dalam komunikasi dan proses antar bagian sistem. Dampak yang dibahas adalah
  antrean yang dapat menumpuk dan response time yang semakin lama. Solusi yang
  dibahas adalah komunikasi asynchronous atau queue dengan konsekuensi
  kompleksitas sistem menjadi lebih tinggi.
- Briliant membahas **Single Point of Failure**, karena modul Order, Payment,
  dan Courier Notification masih berada dalam satu proses/server. Kami
  membahas risiko ketika satu bagian mengalami masalah sehingga bagian lain
  ikut terdampak. Solusi yang dibahas adalah memisahkan modul, dengan
  trade-off koordinasi antar modul menjadi lebih kompleks.
- Kebuntuan: sempat bingung apakah monolithic = pitfall atau bukan. Setelah
  membaca kembali soal, ternyata masalah desain arsitektur juga diperbolehkan
  untuk digunakan sebagai pitfall selain 8 Fallacies.
- Setelah pembahasan, kami menyepakati tiga pitfall yang digunakan adalah
  The Network Is Reliable, Latency Is Zero, dan Single Point of Failure. 

## [Tanggal diskusi 2]
- ...

## Review Silang
- [Nama] mengomentari analisis [Nama lain]: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 20 September 2026 | ChatGPT | Membantu memahami materi sistem terdistribusi dan menentukan pitfall yang relevan untuk skenario FoodGo | AI membantu menjelaskan konsep pitfall dan memberikan kerangka hubungan antara bukti skenario, alasan asumsi salah, dampak, solusi, dan trade-off | Kelompok membandingkan saran tersebut dengan skenario FoodGo dan menentukan tiga pitfall yang digunakan |
| 20 September 2026 | ChatGPT | Membantu mengecek dan merapikan struktur analisis tiga pitfall FoodGo serta kesimpulan kelompok | AI membantu mengecek konsistensi antara bukti, dampak, solusi, dan trade-off pada masing-masing pitfall | Kelompok melakukan pengecekan kembali terhadap skenario dan menyesuaikan isi analisis dengan hasil diskusi kelompok |

# Jurnal Proses — Tugas 5

## Implementasi Bully

- Kendala saat mengisi TODO 1–4: Awalnya saya masih bingung memahami cara kerja Bully Algorithm, terutama cara node mengirim pesan `ELECTION`, menerima `OK`, dan menentukan leader. Saat program dijalankan, beberapa node juga sempat melakukan election berulang kali sehingga saya perlu memeriksa kembali alur programnya.
- Perbaikan yang dilakukan: Saya memeriksa log pada setiap terminal dan mencoba memperbaiki alur pemilihan leader serta proses pemantauan leader ketika node berhenti.
- Hasil pengujian: Pada pengujian terakhir, Node 5 tercatat sebagai leader ketika semua node aktif. Pengujian ketika Node 5 dihentikan dilakukan untuk melihat apakah Node 4 dapat menjadi leader baru.

## Skenario 1: Start normal

- Leader yang terpilih: Node 5.
- Log/observasi: Saya menjalankan lima node menggunakan terminal yang berbeda. Setiap node berkomunikasi melalui port masing-masing. Dari log terminal, Node 5 menjadi leader karena ID-nya paling tinggi. Node lain kemudian menerima pesan `COORDINATOR` yang menunjukkan bahwa Node 5 menjadi leader.
- Bukti: `bukti/semua node dijalankan`

## Skenario 2: Leader dimatikan

- Leader baru yang terpilih: Node 4, jika hasil pengujian akhir menunjukkan Node 4 berhasil menjadi leader setelah Node 5 dihentikan.
- Berapa lama waktu sampai leader baru terdeteksi: Belum diukur secara pasti. Waktu akan dihitung dari saat Node 5 dihentikan sampai Node 4 menampilkan pesan bahwa dirinya menjadi leader.
- Log/observasi: Pada skenario ini, Node 5 dihentikan menggunakan `Ctrl+C`. Node lain kemudian diharapkan mendeteksi bahwa leader sudah tidak aktif dan memulai election kembali. Karena Node 4 memiliki ID tertinggi setelah Node 5 berhenti, Node 4 seharusnya menjadi leader baru.
- Bukti: `bukti/node 5 dihentikan/node5.png`

## Log Penggunaan AI (Level 1–2)

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 17 Oktober 2026 | ChatGPT | Meminta penjelasan tentang langkah-langkah pengerjaan Tugas 5 dan bukti screenshot yang perlu disiapkan. | Menjelaskan urutan pengerjaan, fungsi folder bukti, dan hasil yang perlu diamati pada setiap skenario. | Saya menggunakan penjelasan tersebut untuk menyusun urutan pengerjaan dan menyiapkan folder bukti sesuai skenario pengujian. |
| 18 Oktober 2026 | ChatGPT | Meminta penjelasan tentang Bully Algorithm dan cara membaca log pesan `ELECTION`, `OK`, dan `COORDINATOR`. | Menjelaskan fungsi ketiga pesan dan alasan node dengan ID tertinggi yang masih aktif dipilih sebagai leader. | Saya menggunakan penjelasan tersebut untuk memahami alur komunikasi antarnode dan memeriksa hasil pada terminal. |
| 19 Oktober 2026 | ChatGPT | Meminta bantuan menganalisis hasil pengujian dan anomali yang muncul saat menjalankan lima node. | Menunjukkan bagian log yang perlu diperiksa, seperti election berulang dan perubahan informasi leader. | Saya membandingkan saran dengan keluaran terminal dan menggunakan hasil pengujian untuk memperbarui catatan jurnal. |

## Kesimpulan

Dari praktikum ini, saya belajar bahwa Bully Algorithm digunakan untuk memilih leader berdasarkan ID node yang paling tinggi dan masih aktif. Saya juga belajar bahwa komunikasi antarnode perlu berjalan dengan benar agar setiap node mengetahui siapa leader saat ini. Pengujian dengan menghentikan Node 5 digunakan untuk memeriksa apakah sistem dapat memilih leader pengganti.
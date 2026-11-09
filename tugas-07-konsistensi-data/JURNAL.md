# Jurnal Proses — Tugas 7

## Diskusi Pemilihan Model Konsistensi

- **Argumen yang dipertimbangkan:**
  - Eventual Consistency memungkinkan setiap replika memiliki data yang berbeda untuk sementara waktu sampai proses replikasi selesai. Model ini cocok untuk data yang tidak terlalu sensitif, seperti jumlah like di media sosial.
  - Sequential Consistency menjaga agar semua replika melihat urutan operasi yang sama. Namun, untuk transaksi saldo e wallet, diperlukan jaminan yang lebih kuat agar saldo tidak salah dibaca atau digunakan dalam transaksi.
  - Read Your Writes dipilih sebagai pendekatan Client Centric Consistency karena memastikan pelanggan dapat membaca hasil perubahan data yang sebelumnya telah dilakukan, meskipun berpindah server.
  - Dalam sistem e wallet, ketepatan saldo sangat penting karena berkaitan langsung dengan transaksi keuangan dan kepercayaan pelanggan.

- **Kesimpulan akhir & alasan:**

  Eventual Consistency saja tidak cukup untuk diterapkan pada sistem saldo e-wallet FoodGo karena keterlambatan replikasi dapat menyebabkan pelanggan membaca saldo lama dan transaksi ditolak meskipun saldo sebenarnya mencukupi.

  Oleh karena itu, pendekatan Read Your Writes digunakan untuk memastikan pelanggan selalu mendapatkan informasi saldo terbaru setelah melakukan top up. Jika server yang diakses belum memiliki versi data terbaru, sistem akan mengarahkan permintaan ke server yang sudah memiliki data tersebut.

  Selain itu, transaksi pembayaran tetap perlu menggunakan mekanisme transaksi atomik untuk mencegah kesalahan saldo dan pengurangan saldo secara bersamaan.

## Simulasi (Jika Dikerjakan)

- **Hasil skenario naif vs Read Your Writes:**

  Pada skenario naif, pelanggan melakukan top up sebesar Rp50.000 melalui server Jakarta. Saldo Jakarta berhasil diperbarui menjadi Rp50.000, tetapi server Bandung masih menunjukkan saldo Rp0 karena proses replikasi mengalami keterlambatan selama 2 detik. Ketika pelanggan membaca saldo melalui Bandung, sistem masih menampilkan saldo lama. Kondisi ini disebut *inconsistent read*.

  Pada skenario Read Your Writes, pelanggan melakukan top up kembali sebesar Rp20.000 setelah replikasi pertama selesai. Saldo Jakarta menjadi Rp70.000 dengan versi data 2, sedangkan Bandung masih memiliki versi 1. Sistem mendeteksi bahwa versi Bandung tertinggal dan mengarahkan pembacaan ke Jakarta. Hasilnya, pelanggan berhasil mendapatkan saldo terbaru sebesar Rp70.000 tanpa harus menunggu replikasi selesai.

  **Kesimpulan simulasi:** Read Your Writes berhasil mengatasi masalah pembacaan saldo lama dengan memanfaatkan pengecekan versi data dan pengalihan permintaan ke server yang memiliki data terbaru.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 09-11-2026 | ChatGPT | Apa perbedaan Sequential Consistency, Eventual Consistency, dan Read Your Writes? | Memberikan gambaran konsep dan contoh penerapan konsistensi data dalam sistem e wallet. | Mempelajari kembali materi dan menyusun perbandingan serta kesimpulan berdasarkan pemahaman sendiri. |

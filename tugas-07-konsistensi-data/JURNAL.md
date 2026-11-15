# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan: ...
- Kesimpulan akhir & alasan: ...

## Simulasi (jika dikerjakan)
## Simulasi

- **Pengujian skenario naif:** Setelah pengguna melakukan top-up sebesar Rp50.000 di server Jakarta, server Bandung masih membaca saldo lama sebesar Rp0 karena proses replikasi belum selesai. Hal ini menunjukkan terjadinya *inconsistent read*.
- **Pengujian Read-Your-Writes:** Pengguna melakukan top-up tambahan sebesar Rp20.000 sehingga saldo di Jakarta menjadi Rp70.000. Ketika Bandung menerima permintaan pembacaan dengan versi data terbaru, sistem mendeteksi bahwa versi Bandung masih tertinggal dan mengalihkan pembacaan ke Jakarta. Hasilnya, saldo Rp70.000 berhasil diperoleh.
- **Hasil pengujian:** Kedua skenario berhasil dijalankan. Skenario naif menunjukkan masalah konsistensi data, sedangkan Read-Your-Writes berhasil mengatasi pembacaan data yang tertinggal dalam simulasi.
- **Kendala dan perbaikan:** Sempat terjadi kesalahan saat menjalankan program karena path file yang digunakan tidak sesuai dengan direktori aktif. Setelah menjalankan `py replica_simulation.py` dari folder `src`, program berhasil dieksekusi.
- **Bukti pengujian:** Screenshot hasil eksekusi program disimpan pada folder `bukti/` dengan nama `image.png`.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 15 November 2026 | ChatGPT | Membantu memahami studi kasus dan pemilihan model konsistensi. | Penjelasan Sequential Consistency, Eventual Consistency, dan Read-Your-Writes. | Digunakan sebagai referensi dalam menentukan solusi kasus FoodGo. |
| 15 November 2026 | ChatGPT | Membantu menyusun analisis dan sequence diagram. | Rancangan alur read/write untuk kondisi tanpa solusi dan dengan Read-Your-Writes. | Digunakan sebagai dasar penyusunan README.md. |
| 15 November 2026 | ChatGPT | Membantu menyusun struktur dan isi README.md. | Saran mengenai analisis, contoh penerapan, dan kesimpulan. | Hasil diperiksa dan disesuaikan dengan instruksi tugas. |
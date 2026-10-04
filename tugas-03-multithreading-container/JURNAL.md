# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock

* Hasil `processed_count` yang didapat: 100 dari 100 pesanan. Pada beberapa kali percobaan, hasil yang didapat tetap 100 sehingga race condition tidak terlihat pada saat pengujian.
* Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): Race condition dapat terjadi ketika beberapa thread mengakses dan mengubah `processed_count` secara bersamaan tanpa pengaman. Proses `processed_count += 1` terdiri dari membaca nilai, menambahkan 1, kemudian menyimpan kembali hasilnya. Jika dua thread melakukan proses tersebut pada waktu yang hampir bersamaan, salah satu perubahan dapat tertimpa oleh thread lain sehingga jumlah akhirnya bisa kurang dari jumlah pesanan yang sebenarnya. Pada percobaan ini kondisi tersebut tidak muncul dan hasil tetap 100.

## Percobaan dengan Lock

* Hasil `processed_count` setelah perbaikan: 100 dari 100 pesanan. Setelah menggunakan `threading.Lock()` dan membungkus proses increment dengan `with lock:`, hasil penghitungan menjadi terlindungi dari akses bersamaan sehingga hasil tetap sesuai dengan jumlah pesanan yang diproses.

## Kendala Docker

* Pada awal pengujian terdapat beberapa kendala pada `Dockerfile`, tetapi setelah diperbaiki image berhasil di-build dan container dapat dijalankan.
* Hasil pengujian di dalam container: `Total pesanan diproses: 100 (seharusnya 100)`.

## Log Penggunaan AI (Level 2)

| Tanggal    | Tool AI | Prompt yang diberikan                                            | Ringkasan saran/ide AI                                                          | Bagaimana diolah menjadi tulisan/kode sendiri              |
| ---------- | ------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| 04-10-2026 | ChatGPT | Meminta bantuan memahami alur pengerjaan Tugas 3 multithreading. | Membantu memahami tahapan pengerjaan dan konsep dasar `threading` serta `Lock`. | Digunakan sebagai panduan selama pengerjaan.               |
| 05-10-2026 | ChatGPT | Meminta bantuan memahami proses Docker pada Tugas 3.             | Membantu memahami langkah build dan menjalankan container.                      | Digunakan sebagai panduan saat melakukan pengujian Docker. |

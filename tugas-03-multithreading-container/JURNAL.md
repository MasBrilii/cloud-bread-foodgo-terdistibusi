# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock

* Hasil processed_count yang didapat: 100 dari 100 pesanan. Setelah dicoba beberapa kali, hasilnya selalu pas 100, sehingga masalah race condition belum sempat terlihat saat pengujian.
* Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): Angka hitungan bisa meleset karena perintah processed_count += 1 sebenarnya melewati tiga tahap: membaca angka yang ada, menambah 1, lalu menyimpan angka baru. Jika ada dua pekerja (thread) jalan barengan tanpa antrean (lock), keduanya bisa saja melihat angka yang sama secara serentak. Akibatnya, salah satu hasil hitungan tertimpa oleh yang lain dan total akhirnya jadi berkurang dari yang seharusnya. Pada pengujian saya, tabrakan ini belum sempat terjadi karena jumlah pesanannya masih sedikit dan komputernya bekerja terlalu cepat, sehingga hasil akhirnya masih tetap 100.
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

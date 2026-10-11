# Jurnal Proses — Tugas 4

## Jalur yang dipilih

- **Jalur MQ (Message Queue)**, karena modul pembayaran dapat mengirim notifikasi tanpa harus menunggu modul kurir memprosesnya. RabbitMQ digunakan sebagai perantara untuk menyimpan pesan sementara jika consumer belum aktif.

## Kendala teknis

- Saat pertama menjalankan RabbitMQ, Docker Engine belum aktif sehingga koneksi gagal. Setelah Docker Desktop dijalankan, container RabbitMQ berhasil berjalan.
- Aktivasi virtual environment melalui PowerShell gagal karena kebijakan eksekusi skrip. Solusinya adalah menggunakan Python langsung dari folder `venv`.
- Library `pika==1.3.2` berhasil dipasang dan program dapat dijalankan tanpa error koneksi RabbitMQ.

## Uji "pesan tidak hilang" (khusus Jalur B)

- **Langkah uji:** Menjalankan publisher dan consumer untuk pengujian normal. Setelah itu, consumer dihentikan, kemudian publisher dijalankan kembali untuk mengirim tiga pesan. Pesan diperiksa melalui dashboard RabbitMQ sebelum consumer dijalankan kembali.
- **Hasil yang diamati:** Saat consumer mati, dashboard RabbitMQ menunjukkan `Ready = 3`, `Unacked = 0`, dan `Total = 3`. Setelah consumer dijalankan kembali, tiga pesan untuk user1, user2, dan user3 berhasil diproses. Hal ini menunjukkan bahwa pesan tetap berada di antrean ketika consumer tidak aktif dan dapat diproses setelah consumer kembali berjalan.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.


| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 12 Oktober 2026 | ChatGPT | Meminta panduan pengerjaan Tugas 4 tentang RPC dan Message Queue, termasuk setup RabbitMQ, pengujian, dan dokumentasi. | Mendapat penjelasan mengenai perbedaan komunikasi sinkron dan asinkron, fungsi publisher dan consumer, serta urutan pengujian ketika consumer mati dan aktif kembali. | Panduan digunakan untuk memahami alur tugas dan melakukan pengujian di laptop. Implementasi kode dibantu AI, kemudian dijalankan dan hasilnya diperiksa melalui terminal serta dashboard RabbitMQ. Hasil pengujian dicatat berdasarkan output yang diperoleh. |

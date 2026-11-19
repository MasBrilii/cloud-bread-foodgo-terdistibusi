# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

## Identitas Anggota Kelompok

| No. | Nama Anggota | NIM |
|---|---|---|
| 1 | Farrel Athallah | 103072400136 |
| 2 | Misael Arafian Fonataba | 103072400017 |
| 3 | Briliant Dahsyat Anugrah | 103072400164 |

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.
2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

## Jawaban
## 1. Rekomendasi Deployment Model (Farrel)

Deployment Model yang paling tepat untuk Sistem Data Kependudukan adalah **Private Cloud**.

Private Cloud dipilih karena sistem mengelola informasi pribadi masyarakat yang sangat sensitif, seperti nama, NIK, alamat, dan data biometrik. Data tersebut membutuhkan perlindungan tinggi serta pengendalian infrastruktur oleh pemerintah agar keamanan, penyimpanan, dan hak akses dapat dikelola sesuai kebijakan negara.

Selain itu, Private Cloud tetap dapat mendukung kebutuhan skalabilitas dengan menyediakan penambahan resource, load balancing, dan autoscaling ketika terjadi lonjakan akses dari berbagai instansi.

Penerapan Private Cloud berdasarkan lima karakteristik NIST SP 800-145 adalah sebagai berikut:

| Karakteristik NIST | Penerapan pada Sistem Data Kependudukan |
|---|---|
| **On-demand self-service** | Pemerintah dapat menambah kapasitas komputasi, penyimpanan, dan resource lainnya sesuai kebutuhan tanpa harus melakukan pengadaan secara manual setiap kali terjadi peningkatan permintaan. |
| **Broad network access** | Sistem dapat diakses oleh berbagai instansi, seperti Dukcapil daerah, kepolisian, dan bank melalui jaringan yang aman dengan autentikasi dan otorisasi. |
| **Resource pooling** | Resource server, penyimpanan, dan jaringan dikelola secara terpusat untuk melayani berbagai instansi pemerintah secara efisien tanpa harus menyediakan server terpisah untuk setiap instansi. |
| **Rapid elasticity** | Kapasitas infrastruktur dapat ditingkatkan atau dikurangi sesuai kebutuhan. Misalnya, penambahan kapasitas server ketika terjadi lonjakan akses saat pemilu atau pendaftaran sekolah. |
| **Measured service** | Penggunaan resource seperti CPU, RAM, penyimpanan, dan bandwidth dapat dipantau serta diukur untuk mengetahui kebutuhan kapasitas dan menjaga efisiensi penggunaan infrastruktur. |

Berdasarkan kelima karakteristik tersebut, Private Cloud dinilai mampu menyeimbangkan kebutuhan kerahasiaan data dan skalabilitas sistem. Pemerintah tetap memiliki kendali terhadap infrastruktur, sekaligus dapat mengatur kapasitas layanan sesuai perubahan jumlah pengguna dan permintaan akses.

## 2. Rekomendasi Service Model (Farrel)

Service Model yang direkomendasikan adalah kombinasi IaaS, PaaS, dan SaaS. Penggunaan beberapa model ini bertujuan agar setiap komponen sistem mendapatkan layanan yang sesuai dengan kebutuhan pengelolaannya.

| Komponen Sistem | Service Model | Alasan Pemilihan |
|---|---|---|
| Database Data Kependudukan | **IaaS** | Memberikan kendali lebih besar kepada pemerintah terhadap server virtual, sistem operasi, penyimpanan, dan konfigurasi database sehingga keamanan data sensitif dapat dikelola secara khusus. |
| Backend dan API Sistem | **PaaS** | Memudahkan pengembangan, deployment, dan pengelolaan aplikasi tanpa harus mengelola seluruh infrastruktur server secara langsung. |
| Portal Layanan Instansi | **SaaS** | Instansi seperti Dukcapil, kepolisian, dan bank dapat menggunakan aplikasi yang telah disediakan pemerintah tanpa perlu membangun aplikasi sendiri. |
| Monitoring Infrastruktur | **PaaS** | Membantu pemerintah memantau penggunaan resource, performa server, kapasitas penyimpanan, serta kondisi jaringan secara terpusat. |

Dengan kombinasi tersebut, IaaS digunakan untuk komponen inti yang membutuhkan kendali tinggi, PaaS digunakan untuk mendukung pengembangan dan pengoperasian aplikasi, sedangkan SaaS digunakan untuk menyediakan layanan siap pakai bagi instansi yang membutuhkan akses ke sistem.

Seluruh komponen tetap ditempatkan dalam lingkungan Private Cloud yang dikendalikan pemerintah. Penggunaan SaaS pada portal instansi tidak berarti data kependudukan harus disimpan pada layanan pihak ketiga.

## 3. Risiko dan Mitigasi (Misael)

Meskipun Private Cloud memberikan kendali yang lebih besar terhadap keamanan dan pengelolaan infrastruktur, terdapat beberapa risiko yang perlu diperhatikan.

| Risiko | Dampak | Mitigasi |
|---|---|---|
| **Kegagalan server atau infrastruktur pusat** | Sistem tidak dapat diakses oleh ribuan instansi sehingga proses verifikasi data kependudukan terganggu. | Menyediakan server cadangan, replikasi database, sistem backup berkala, dan Disaster Recovery Center (DRC) untuk memulihkan layanan ketika terjadi gangguan. |
| **Lonjakan akses melebihi kapasitas infrastruktur** | Server mengalami overload sehingga respons sistem menjadi lambat atau bahkan downtime. | Menerapkan load balancing, autoscaling, menyediakan kapasitas cadangan, dan melakukan pengujian beban (load testing) secara berkala. |
| **Serangan siber dan kebocoran data** | Informasi pribadi seperti NIK, alamat, dan biometrik dapat dicuri atau disalahgunakan oleh pihak yang tidak berwenang. | Menerapkan enkripsi data, Multi-Factor Authentication (MFA), firewall, kontrol akses berbasis peran (RBAC), serta audit keamanan secara berkala. |

Dengan penerapan mitigasi tersebut, risiko gangguan layanan dan kebocoran informasi dapat dikurangi sehingga sistem tetap aman dan dapat diandalkan oleh berbagai instansi.

## 4. Perbandingan dengan Alternatif yang Ditolak (Briliant)

Alternatif yang tidak dipilih sebagai model utama adalah **Public Cloud**.

Public Cloud sebenarnya memiliki keunggulan dalam hal skalabilitas, fleksibilitas, dan kemudahan penyediaan resource. Model ini memungkinkan kapasitas infrastruktur ditingkatkan dengan cepat ketika terjadi lonjakan permintaan akses.

Namun, Public Cloud dinilai kurang tepat untuk dijadikan infrastruktur utama Sistem Data Kependudukan karena pemerintah tidak memiliki kendali langsung atas seluruh infrastruktur fisik yang disediakan oleh penyedia layanan cloud. Hal ini menjadi perhatian karena sistem menyimpan data pribadi yang sangat sensitif, termasuk NIK, alamat, dan data biometrik warga negara.

Sementara itu, Private Cloud memungkinkan pemerintah memiliki kendali lebih besar terhadap pengelolaan infrastruktur, kebijakan keamanan, penyimpanan data, dan pengaturan hak akses.

| Aspek Perbandingan | Private Cloud (Dipilih) | Public Cloud (Ditolak) |
|---|---|---|
| Kendali infrastruktur | Lebih besar dan dikelola khusus untuk pemerintah. | Bergantung pada penyedia layanan cloud. |
| Keamanan data | Kebijakan keamanan dapat dikendalikan pemerintah. | Bergantung pada pengaturan dan tanggung jawab bersama dengan penyedia. |
| Skalabilitas | Dapat ditingkatkan melalui pengelolaan kapasitas infrastruktur. | Umumnya lebih fleksibel dalam penambahan resource. |
| Pengelolaan | Membutuhkan pengelolaan infrastruktur sendiri. | Sebagian besar infrastruktur dikelola penyedia. |
| Kesesuaian kasus | Sangat sesuai untuk data kependudukan yang sensitif. | Kurang sesuai sebagai infrastruktur utama karena kebutuhan kendali pemerintah. |

Dengan demikian, Public Cloud tidak dipilih sebagai infrastruktur utama karena kebutuhan utama sistem bukan hanya skalabilitas, tetapi juga kerahasiaan dan pengendalian data oleh negara.

## Kesimpulan

Berdasarkan hasil analisis, kelompok kami merekomendasikan **Private Cloud sebagai Deployment Model** untuk Sistem Data Kependudukan karena mampu memberikan kendali yang lebih besar terhadap keamanan dan pengelolaan data sensitif masyarakat. Private Cloud juga dapat mendukung skalabilitas melalui penambahan resource, load balancing, dan autoscaling untuk menghadapi lonjakan akses dari berbagai instansi.

Untuk Service Model, kelompok kami merekomendasikan kombinasi IaaS, PaaS, dan SaaS sesuai kebutuhan masing-masing komponen sistem. Selain itu, penerapan mitigasi risiko seperti backup, Disaster Recovery Center, enkripsi, dan load balancing diperlukan agar sistem tetap aman, tersedia, dan dapat diandalkan.

Dengan rancangan tersebut, Sistem Data Kependudukan diharapkan mampu memenuhi kebutuhan kerahasiaan data sekaligus memberikan layanan yang stabil kepada ribuan instansi di Indonesia.

### Diagram Arsitektur Cloud


![Diagram Arsitektur](bukti/drawio.jpg)

## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.

# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** cloud-bread-foodgo-terdistibusi

| Nama | NIM | Kontribusi |
|---|---|---|
| SALMAN ALFARIZI | 103072400047 | The Network Is Reliable |
| MUHAMMAD AUBERT FAWWAZ PRAYITNO | 10307240164 | Latency Is Zero |
| BRILIANT DAHSYAT ANUGRAH | 103072400169 | Single Point of Failure |

## Pitfall 1: The Network Is Reliable — ditulis oleh SALMAN

**Bukti di skenario:** Di dalam skenario, tim menuliskan bahwa: "# network is always reliable, no need for retry" Kemudian di bagian berikutnya juga dijelaskan bahwa tidak ada timeout sama sekali pada pemanggilan antar-service, yaitu ketika modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu.

**Kenapa ini keliru:** Menurut saya, ini merupakan salah satu kesalahan dari tim FoodGo karena mereka menganggap bahwa network akan selalu berjalan dengan baik dan tidak membutuhkan retry. Padahal dalam sistem yang saling terhubung, network tidak selalu bisa berjalan sesuai yang diharapkan. Bisa saja terjadi gangguan atau proses pengiriman dan penerimaan data membutuhkan waktu lebih lama.

Kesalahan tersebut juga terlihat dari tidak adanya timeout sama sekali. Ketika modul pesanan memanggil modul pembayaran, proses tersebut tentunya membutuhkan waktu untuk mengirim permintaan, diproses oleh modul pembayaran, lalu mendapatkan hasilnya kembali. Kalau modul pembayaran sedang mengalami masalah atau prosesnya lama, modul pesanan akan terus menunggu karena tidak ada batas waktu yang ditentukan.

Menurut saya, hal ini akan menjadi masalah yang lebih besar ketika FoodGo digunakan dengan traffic yang semakin banyak. Kalau banyak request yang sama-sama menunggu response dari modul lain, tentunya proses yang berjalan juga akan semakin banyak dan dapat membuat server semakin terbebani.

**Dampak ke FoodGo:** Dampaknya adalah proses pemesanan bisa menjadi lambat karena harus menunggu modul pembayaran. Kalau modul pembayaran sedang bermasalah atau lambat memberikan response, pengguna juga akan merasakan proses yang lama.

Apalagi pada skenario sudah disebutkan bahwa aplikasi FoodGo memang mengalami kondisi sangat lambat dan beberapa request mengalami timeout. Jadi masalah network dan tidak adanya timeout ini bisa menjadi salah satu penyebab kenapa request yang masuk tidak dapat diproses dengan cepat.

Kalau kondisi tersebut terus terjadi ketika traffic meningkat, request yang masih menunggu bisa semakin banyak dan akhirnya membuat backend semakin terbebani. Dalam kondisi tertentu, hal ini juga bisa memperparah masalah yang sudah terjadi pada server FoodGo.

**Solusi desain awal:** Menurut saya, solusi awal yang dapat digunakan adalah memberikan timeout pada komunikasi antar-service, terutama ketika modul pesanan memanggil modul pembayaran. Jadi modul pesanan tidak akan menunggu terus-menerus jika modul pembayaran tidak memberikan response.

Selain itu, dapat digunakan retry apabila kegagalan yang terjadi hanya sementara. Tetapi retry juga tidak boleh dilakukan terus-menerus. Bisa diberikan jeda atau backoff supaya ketika modul pembayaran sedang bermasalah, FoodGo tidak malah mengirim request berkali-kali dalam waktu yang sama.

Untuk kondisi yang lebih parah, seperti modul pembayaran terus mengalami kegagalan, dapat juga digunakan circuit breaker agar sistem tidak terus mencoba menghubungi service yang sedang bermasalah.

**Trade-off:** Menurut saya, penggunaan timeout dan retry memang dapat membantu sistem ketika terjadi gangguan, tetapi juga mempunyai kekurangan. Retry yang terlalu sering justru bisa membuat jumlah request semakin banyak dan menambah beban pada service yang sedang bermasalah.

Selain itu, timeout juga harus ditentukan dengan tepat. Kalau waktunya terlalu pendek, request yang sebenarnya masih dalam proses bisa dianggap gagal. Tetapi kalau terlalu lama, masalahnya hampir sama karena sistem masih harus menunggu cukup lama sebelum mengetahui bahwa request tersebut gagal.

---

## Pitfall 2: Latency Is Zero — ditulis oleh FAWWAZ

**Bukti di skenario:** Di dalam skenario dijelaskan bahwa aplikasi FoodGo menjadi sangat lambat dan beberapa request mengalami timeout. Selain itu, modul pesanan harus memanggil modul pembayaran dan menunggu response. Pada skenario juga disebutkan bahwa tidak ada timeout sama sekali pada pemanggilan antar-service.

**Kenapa ini keliru:** Menurut saya, kesalahan tim FoodGo di bagian ini adalah mereka tidak memperhitungkan waktu yang dibutuhkan ketika satu modul berkomunikasi dengan modul lainnya. Ketika modul pesanan memanggil modul pembayaran, proses tersebut tentunya tidak langsung mendapatkan response karena request harus dikirim terlebih dahulu, kemudian diproses oleh modul pembayaran, lalu hasilnya dikembalikan lagi ke modul pesanan.

Hal ini menjadi masalah ketika modul pembayaran sedang sibuk atau membutuhkan waktu lebih lama untuk memproses request. Modul pesanan akan ikut menunggu dan akhirnya proses pemesanan menjadi lebih lama. Apalagi pada skenario sudah disebutkan bahwa aplikasi mengalami kondisi sangat lambat dan beberapa request mengalami timeout.

Menurut saya, semakin tinggi traffic yang masuk ke FoodGo, kemungkinan waktu tunggu juga dapat semakin terasa. Kalau banyak request melakukan komunikasi antar-service dalam waktu yang bersamaan, proses yang menunggu response bisa semakin banyak dan membuat sistem semakin terbebani.

**Dampak ke FoodGo:** Dampaknya adalah pengguna dapat merasakan proses pemesanan yang lebih lama karena proses Order bergantung pada response dari Payment. Kalau Payment membutuhkan waktu lama untuk memberikan response, Order juga ikut tertahan.

Jika kondisi tersebut terjadi pada banyak request secara bersamaan, jumlah proses yang menunggu dapat semakin banyak. Hal ini dapat meningkatkan beban backend dan pada akhirnya berkaitan dengan masalah yang sudah terjadi pada FoodGo, yaitu aplikasi menjadi lambat dan beberapa request mengalami timeout.

Selain itu, karena komunikasi antar-service membutuhkan waktu, keterlambatan pada satu bagian juga dapat ikut memengaruhi proses pada bagian lainnya. Jadi masalahnya bukan hanya pada modul Payment, tetapi bisa ikut dirasakan oleh proses Order yang bergantung kepadanya.

**Solusi desain awal:** Menurut saya, solusi awalnya adalah sistem perlu memperhitungkan latency dalam setiap komunikasi antar-service. Salah satunya dengan menetapkan timeout sehingga modul Order tidak terus menunggu response dari Payment.

Untuk proses yang tidak harus mendapatkan hasil secara langsung, FoodGo juga dapat mempertimbangkan komunikasi secara asynchronous atau menggunakan message queue. Dengan cara tersebut, modul yang mengirim request tidak harus selalu menunggu service lain selesai memprosesnya.

Selain itu, FoodGo juga dapat melakukan monitoring terhadap waktu response antar-service supaya ketika ada service yang terlalu lambat, bagian tersebut dapat diketahui dan ditangani.

**Trade-off:** Menurut saya, penggunaan komunikasi asynchronous atau message queue dapat mengurangi ketergantungan terhadap response secara langsung, tetapi membuat sistem menjadi lebih kompleks. Data yang dikirim tidak selalu langsung mendapatkan hasil sehingga perlu ada mekanisme untuk memastikan pesan tetap diproses.

Sedangkan penggunaan timeout juga mempunyai trade-off. Kalau timeout terlalu cepat, request yang sebenarnya masih dalam proses bisa dianggap gagal. Tetapi kalau timeout terlalu lama, pengguna tetap harus menunggu cukup lama sebelum sistem menyatakan bahwa request tersebut gagal.

---

## Pitfall 3: Single Point of Failure — ditulis oleh [BRILIANT]

**Bukti di skenario:** Di dalam skenario dijelaskan bahwa satu server menangani semua modul FoodGo, yaitu modul orders, payment, dan courier notifications. Selain itu, backend server juga terkadang mengalami crash dan harus dilakukan restart secara manual. Pada saat traffic meningkat, server tersebut juga dapat menjadi overwhelmed.

**Kenapa ini keliru:** Menurut saya, kesalahan tim FoodGo di bagian ini adalah semua modul utama masih dijalankan dalam satu server atau satu proses. Jadi ketika server tersebut mengalami masalah, bukan hanya satu bagian saja yang terkena dampaknya, tetapi beberapa fungsi FoodGo bisa ikut terganggu.

Hal ini menjadi lebih berisiko karena pada skenario sendiri sudah disebutkan bahwa backend server terkadang crash dan membutuhkan restart secara manual. Berarti server yang digunakan memang mempunyai kemungkinan mengalami kegagalan. Kalau semua modul masih berada pada server yang sama, ketika server tersebut crash maka modul Order, Payment, maupun Courier Notification juga bisa ikut tidak berjalan.

Selain itu, ketika traffic FoodGo semakin meningkat, satu server harus menangani pekerjaan dari berbagai modul sekaligus. Menurut saya, hal ini dapat membuat beban server semakin besar dan akhirnya menyebabkan server menjadi overwhelmed seperti yang sudah disebutkan pada skenario.

**Dampak ke FoodGo:** Dampaknya adalah ketika server utama mengalami masalah, banyak fungsi FoodGo dapat terganggu secara bersamaan. Misalnya proses pemesanan tidak berjalan, proses pembayaran ikut terganggu, dan notifikasi kepada kurir juga dapat terpengaruh.

Masalah ini juga dapat membuat FoodGo menjadi lebih sulit digunakan ketika traffic sedang tinggi. Karena semua modul bergantung pada server yang sama, peningkatan beban pada satu tempat dapat memengaruhi keseluruhan aplikasi.

Kalau server sampai crash, sistem juga membutuhkan restart manual seperti yang disebutkan dalam skenario. Artinya selama proses tersebut belum selesai, layanan yang bergantung pada server tersebut berpotensi tidak dapat digunakan dengan normal.

**Solusi desain awal:** Menurut saya, solusi awal yang dapat dilakukan adalah memisahkan modul-modul utama FoodGo menjadi beberapa service. Misalnya modul Order dibuat menjadi Order Service, modul Payment menjadi Payment Service, dan modul Courier Notification menjadi service tersendiri.

Dengan pemisahan tersebut, setiap modul tidak harus bergantung sepenuhnya pada satu proses yang sama. Beban dari masing-masing fungsi juga dapat dikelola secara lebih terpisah. Jika nantinya salah satu service mengalami masalah, dampaknya dapat dibatasi sehingga tidak otomatis membuat seluruh fungsi FoodGo ikut berhenti.

**Trade-off:** Menurut saya, pemisahan service memang dapat mengurangi ketergantungan pada satu server, tetapi sistem FoodGo juga menjadi lebih kompleks. Karena setiap service sekarang harus saling berkomunikasi melalui network, muncul masalah baru seperti komunikasi yang gagal atau response yang lambat.

Selain itu, jumlah service yang harus dikelola juga menjadi lebih banyak. FoodGo membutuhkan monitoring dan pengelolaan yang lebih baik agar setiap service dapat diketahui kondisinya. Jadi pemisahan service bukan berarti semua masalah langsung selesai, tetapi perlu diikuti dengan pengelolaan sistem yang baik.

---

## Kesimpulan Kelompok

Menurut kelompok kami, masalah yang terjadi pada FoodGo bukan hanya karena traffic yang semakin banyak, tetapi juga karena ada beberapa asumsi dan desain sistem yang kurang tepat. Network tidak seharusnya dianggap selalu reliable, komunikasi antar-service juga membutuhkan waktu, dan semua modul yang masih berada dalam satu server membuat sistem terlalu bergantung pada satu server tersebut.

Dari ketiga masalah tersebut, FoodGo perlu mulai menggunakan timeout dan retry yang sesuai untuk komunikasi antar-service, memperhitungkan latency dalam proses komunikasi, serta memisahkan modul seperti Order, Payment, dan Courier Notification agar tidak semuanya bergantung pada satu server. Dengan perubahan tersebut, sistem diharapkan dapat lebih siap menghadapi peningkatan traffic dan ketika salah satu bagian mengalami masalah, dampaknya tidak langsung mengganggu seluruh sistem.

Namun, perubahan tersebut juga membuat arsitektur FoodGo menjadi lebih kompleks karena setiap service harus saling berkomunikasi dan dikelola dengan baik. Oleh karena itu, hasil analisis dari Tugas 1 ini dapat menjadi dasar untuk menentukan dan membahas arsitektur yang lebih sesuai pada Tugas 2, terutama dalam menentukan bagaimana modul-modul FoodGo sebaiknya dipisahkan dan bagaimana komunikasi antar modul tersebut dilakukan.

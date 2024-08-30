# DanaKaget-QR-Generator
![Dana-Qr-Generator Image1](https://github.com/user-attachments/assets/f93b79af-6e0d-4d5b-a8da-4e8def35446d)

## Overview
**Dana Kaget QR Code Generator** adalah sebuah tool untuk menghasilkan kode QR dari link Dana Kaget, atau aplikasi Dana Indonesia. Alat ini juga mendukung pembuatan link Dana Kaget secara acak. Program ini didesain untuk edukasi dan demonstrasi, dan penggunaannya sepenuhnya merupakan tanggung jawab pengguna.

**Peringatan: Tool ini hanya untuk tujuan edukasi. Kami tidak bertanggung jawab atas penyalahgunaan yang terjadi dari penggunaan alat ini.**

## Fitur
- **QR Code Generation**: Buat kode QR dengan logo yang bisa dipilih dari empat opsi yang tersedia.
- **Multiple Iterations**: Mendukung pembuatan beberapa QR code dalam satu kali eksekusi.
- **Random Link Generation**: Buat link Dana Kaget acak dengan satu klik.

## Prasyarat
Pastikan Anda memiliki Python 3.x terinstal di sistem Anda. Tool ini membutuhkan beberapa pustaka Python berikut:

- `qrcode`
- `PIL (Pillow)`
- `argparse`
- `random`
- `string`
- `sys`
- `logging`

Jika Anda belum memiliki pustaka-pustaka tersebut, Anda bisa menginstalnya dengan menjalankan:
```
pip install qrcode[pil] pillow
```

## Instalasi
Clone repositori ini ke direktori lokal Anda:

```
git clone https://github.com/RozhakXD/DanaKaget-QR-Generator.git
cd DanaKaget-QR-Generator
```

Instal dependencies yang diperlukan:
```
pip install -r requirements.txt
```

## Cara Penggunaan
Jalankan program dengan perintah berikut:
```
python3 Run.py <COUNT> <PATH> <IMAGE> <LINK>
```

### Argumen
- `PATH` - Direktori di mana file gambar akan disimpan (misalnya: `/sdcard/Download/`).
- `IMAGE` - Nomor gambar yang akan digunakan sebagai logo pada QR (1, 2, 3, atau 4).
- `COUNT` - Jumlah iterasi untuk memproses link (misalnya: 10).
- `LINK` - Link yang akan diproses atau 'null' untuk menghasilkan link acak.

## Contoh Penggunaan
Untuk membuat 10 QR code dengan logo gambar nomor 2 dan menyimpan hasilnya di direktori `Downloads`, jalankan:

```
python3 Run.py 10 /sdcard/Download/ 2 https://link.dana.id/kaget?c=sqwdu4f4k
```

Atau, jika Anda ingin membuat QR code dengan link Dana Kaget acak:
```
python3 Run.py 1 /sdcard/Download/ 3 null
```

## Log Error
Jika terjadi kesalahan selama eksekusi, program ini akan memberikan log yang detail dan rapi untuk membantu Anda dalam proses debugging. Log mencakup waktu, level error, dan pesan error.

## Tangkapan Layar
![FunPic_20240830](https://github.com/user-attachments/assets/b701ffb5-a0c4-41f2-9693-d11394e3bf0f)

## Kontribusi
Kontribusi sangat terbuka! Jangan ragu untuk membuka issue atau pull request untuk perbaikan dan fitur baru.

## Donasi
Apabila proyek ini bermanfaat bagi Anda, dukungan Anda melalui donasi sangat dihargai:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

## Lisensi
Proyek ini berlisensi MIT. Untuk mempelajari lebih lanjut tentang hak dan batasan penggunaan, silakan lihat [LICENSE](https://github.com/RozhakXD/DanaKaget-QR-Generator?tab=GPL-3.0-1-ov-file).

CipherFile – Dosya Şifreleme Uygulaması


CipherFile, Python dili kullanılarak geliştirilmiş bir dosya şifreleme ve çözme uygulamasıdır. 
Bu proje, farklı şifreleme algoritmalarını kullanarak kullanıcıların dosyalarını güvenli bir şekilde şifrelemesini ve tekrar çözmesini sağlar.



Özellikler


AES şifreleme

DES3 şifreleme

Caesar şifreleme

XOR şifreleme

Dosya şifreleme ve çözme desteği

Grafiksel kullanıcı arayüzü (GUI)

Kullanıcı dostu arayüz



Kullanılan Teknolojiler


Python 3

Tkinter (GUI için)

PyCryptodome (AES ve DES3 için)

Standart Python kütüphaneleri



Proje Yapısı


CipherFile/
│
├── aes.py        # AES şifreleme algoritması
├── des3.py       # DES3 şifreleme algoritması
├── caesar.py     # Caesar şifreleme algoritması
├── xor.py        # XOR şifreleme algoritması
├── file.py       # Dosya okuma ve yazma işlemleri
├── gui.py        # Grafiksel kullanıcı arayüzü
└── README.md

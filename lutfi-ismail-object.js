// Membuat constructor function
function mahasiswa(nama, nim, kelas, email) {
  this.nama = nama;
  this.nim = nim;
  this.kelas = kelas;
  this.email = email;

  this.sapa = () => {
    return `Halo! Nama saya ${this.nama} dari kelas ${this.kelas}. Salam kenal ya!`;
  };
}

// Membuat objek mahasiswa1
const mahasiswa1 = new mahasiswa(
  "John Doe",
  12345678,
  "IF-III-A",
  "johndoe@example.com"
);

// Menampilkan value dari property nama
console.log(mahasiswa1.nama);
// Memanggil method mahasiswa1
console.log(mahasiswa1.sapa());

// Membuat objek mahasiswa2
const mahasiswa2 = new mahasiswa(
  "Jane Doe",
  87654321,
  "IF-III-B",
  "janedoe@example.com"
);

// Menampilkan value dari property nama
console.log(mahasiswa2.nama);
// Memanggil method mahasiswa2
console.log(mahasiswa2.sapa());

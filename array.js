// Membuat array kelompok 3
let kelompok3 = [
  {
    nama: "Lutfi Ismail Aliansah Putra",
    nim: "10224004",
    email: "lutfi10224004@student.sttcipasung.ac.id",
  },
  {
    nama: "Dede Here Rizqia Iswara",
    nim: "10224103",
    email: "dede10224103@student.sttcipasung.ac.id",
  },
  {
    nama: "Lutvi Maulana",
    nim: "10224005",
    email: "lutvi10224005@student.sttcipasung.ac.id",
  },
];

// Menampilkan anggota kelompok 3
kelompok3.forEach((element, index) => {
  console.log(`
    Anggota kelompok 3 ke-${index + 1}\n 
    Nama: ${element.nama}\n 
    NIM: ${element.nim}\n
    Email: ${element.email}\n
    --------------------
  `);
});

// Penambahan anggota baru kelompok 3
kelompok3.push({
  nama: "Yulia",
  nim: "10224016",
  email: "yulia10224016@student.sttcipasung.ac.id",
});

kelompok3.push({
  nama: "Jane Doe",
  nim: "",
  email: "",
});

console.log("Anggota kelompok 3 setelah diperbarui");
kelompok3.forEach((element, index) => {
  console.log(`
    Anggota kelompok 3 ke-${index + 1}\n 
    Nama: ${element.nama}\n 
    NIM: ${element.nim}\n
    Email: ${element.email}\n
    --------------------
  `);
});

console.log("Menghapus anggota yang tidak valid...");
kelompok3.pop([kelompok3.length]);

console.log("Anggota kelompok 3 valid terbaru");
kelompok3.forEach((element, index) => {
  console.log(`
    Anggota kelompok 3 ke-${index + 1}\n 
    Nama: ${element.nama}\n 
    NIM: ${element.nim}\n
    Email: ${element.email}\n
    --------------------
  `);
});

kelompok3.push({
  nama: "Rifan Fawaz Saefullah",
  nim: "10224158",
  email: "rifan10224158@student.sttcipasung.ac.id",
});

console.log("Ehh nambah satu anggota lagi :)");
kelompok3.forEach((element, index) => {
  console.log(`
    Anggota kelompok 3 ke-${index + 1}\n 
    Nama: ${element.nama}\n 
    NIM: ${element.nim}\n
    Email: ${element.email}\n
    --------------------
  `);
});

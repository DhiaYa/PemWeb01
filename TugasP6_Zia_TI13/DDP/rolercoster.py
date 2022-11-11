#Program Syarat Menaiki Roler Coster

#Input
print("========== Syarat Tinggi Badan ==========")
nama = input("masukan nama anda :")
umur = int(input("masukan umur anda"))
tinggi = int(input("masukan tinggi badan anda"))

#Condition IF
if tinggi > 90:
    ket = "=======Pengunjung Boleh Menaiki Wahana Roler Coster======="

else:
    ket = "===Pengunjung Tidak Boleh Menaiki Wahana Karena Tinggi Badan Dibawah 90 CM==="

#Output
print("========================")
print("Nama Penjunjung = ", nama)
print("Nama Pengunjung = ", nama, "tahun")
print("Tinggi Badan Pengunjung = ", tinggi, "centimeter")
print(ket)

print("=========Program Selesai=========")
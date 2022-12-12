

print ("==================input lama anda menelpon==================== ")
print ("================== JAM MULAI ANDA MENELPON====================")

jam_awal = int (input ("masukkan jam awal anda menelpon : "))
menit_awal = int (input ("masukkan menit : "))
detik_awal = int (input ("masukkan menit : "))
              
              
print ("================== JAM TERAKHIR ANDA MENELPON====================")

jam_akhir = int (input ("masukkan jam awal anda menelpon : "))
menit_akhir = int (input ("masukkan menit : "))
detik_akhir = int (input ("masukkan menit : "))

if jam_awal == 24:
    print ("MAAF, WARTEL TERTUTUP")

elif jam_awal and jam_akhir <= 23 :

  
    jam = (jam_akhir - jam_awal)*3600
    menit = (menit_akhir - menit_awal)*60
    detik = detik_akhir - detik_awal
                                                                            
    pulsa = jam / 5
    harga = pulsa * 150

    print ("JAM = ", jam ,"JAM" )
    print ("MENIT = ", menit, "MENIT" )
    print ("DETIK = ", detik, "DETIK" )
    print ("TOTAL BIAYA  = " ,harga, "Rp")
    

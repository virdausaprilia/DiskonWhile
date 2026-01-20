while True:
    try:
        total_pembelian = float(input("masukkan total pembelian: "))
        if total_pembelian > 500000:
            diskon_persen = 10
            nilai_diskon =total_pembelian * (diskon_persen / 100)
            harga_setelah_diskon = total_pembelian - nilai_diskon

            print(f"total pembelian: Rp{total_pembelian:,.2f}")
            print(f"diskon)({diskon_persen}%): Rp{nilai_diskon:,.2f}")
            print(f"harga setelah diskon: Rp{harga_setelah_diskon:,.2f}")
        else:
            print("jumlah pembelian tidak memenuhi syarat untuk diskon.")    
        break
    except ValueError:
        print("masukkan angka yang valid.")  
        
        






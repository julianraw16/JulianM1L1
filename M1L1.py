meme_dict = {
            "ROFL": "tanggapan terhadap lelucon",
            "LITERALLY": "sinonim exactly yang memiliki arti secara tepat",
            }
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Kata kata tersebut tidak ada di kamus!")
    

print("Uygulamamiza Hos Geldiniz Bu Uygulamada Pythondaki Veri Tutma Yapilari Hakkinda Bilgi Edinebilirisiniz")
secim=int(input("Seciminizi Yapiniz\n1-Listeler\n2-Sozlukler\n3-Setler\n4-Tuple\n"))
if secim==1:
    print("Veri Tutmak icin en cok kullanilan yapilardir girilen veri indexleme mantigiyla tek tek degistirilebbilir\n")
    print("Veri tekrarlamaya izin verir\n")
    print("Liste olusturmak icin koseli parantez -> [] kullanilir\n")
    print("Listeler list1+list2 seklinde birlestirilebilir , *x seklinde x kez tekrarlanabilir\n")
    print("Karisik liste olusturulabilir\n")
    print("ic ice listelerde veri cagirmak icin -> nestedList[0][2][1]\n")
    print("Onemli Metodlar\n1-list.append(x) -> x eklenir\n2-list.pop() -> sondan sil\n3-list.remove(x) -> x i sil\n4-list.count(x) -> x i sayar\n5-list.reverse() -> listeyi ters cevirir\n")
if secim==2:
    print("Anahtar ve onlara karsilik degerler vardir\n")
    print("icine liste sozluk gibi yapilar eklenebilir\n")
    print("Sozluk olusturmak icin suslu parantez -> {key : value} kullanilir\n")
    print("icindeki listedeki elemani cagirmak icin -> sozluk[Key][index]\n")
    print("Onemli Metodlar\n1-sozluk.keys() -> anahtarlari gosterir\n2-sozluk.values() -> degerleri gosterir\n")
if secim==3:
    print("Setlerde veri tekrari olmaz\n")
    print("Listeler sete cevrilir -> set(listem)\n")
    print("set olusturmak icin suslu parantez kullanilir -> setim={3,5,7,9}\n")
if secim==4:
    print("Degistirilemez verileri tutar icindeki verilere degistirmeye izin vermez\n")
    print("normal parantez ile olusturulur -> tuplem (3,5,4,7)\n")
    print("Onemli Metodlar\n1-tuplem.count(x) -> x den kac tane oldugu\n2-tuplem.index(x) -> x in indexi\n")

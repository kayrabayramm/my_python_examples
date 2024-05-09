metin=  "kayra python öğreniyor"
#stringlerde her karakterin bir index numarası vardır ve bu numaralar 0 dan başlayıp metnin uzunluğuna kadar gider
print(metin[0])


#negatif indexler metnin sonundan başına kadar -1 den başlayarak numaralandırılır
print(metin[-2])


#stringlerde slice işlemi ile stringlerden parça alabiliriz,araya iki nokta konularak başlangıç ve bitiş index değeri verilir başlangıç değeri baz alınır bitiş değeri baz alınmaz 
#negatif indexlerde kullanılabilir
print(metin[6:-10])

print(metin[0:])#eğer bitiş değeri verilmezse stringin sonuna kadar baz alınır 

print(metin[:11])#başlangıç değeri verilmezse girilen ikinci index numarasına kadar yazdırır

#stringlerde adımlama değeri
print(metin[0:5:2])#ikinci iki noktadan sonra yazılan değer adımlama değeridir ve belirtilen kısmı bu adımlama değeri kadar atlayarak baz alır
print(metin[::-1])
print(metin[5::-1])
print(len(metin))#len metodu  metnin uzunluğunu verir

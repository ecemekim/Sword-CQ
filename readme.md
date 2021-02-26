**Özet:**

users dizinindeki 10 adet json dosyasındaki tüm kayıtları gRPC server üzerinden redis "jsonrows" kuyruğuna aktarır. 
Bu sırada gRPC client servisi mesajı aldığını iletir. Connections dizinindeki redis_connection.py ise kuyruğu dinler ve 
kuyruktaki dataları birleştirerek final.json dosyasını oluşturur. Flask üzerinden tetikleme sonucu oluşturulan 
final.json dosyasının bir kısmı response olarak döner aynı zamanda dataların tamamı final.json olarak sunucuda 
("_Sword-CQ/SwordServer/users/final.json_") görüntülenebilir.

**Adımlar:**

1- sudo apt-get install docker komutu çalıştırılır.

2- sudo apt-get install docker-compose komutu çalıştırılır.

3- Sword-CQ dizinindeyken sudo docker-compose up -d --build komutu çalıştırılır.

4- Terminalde sudo docker container ls komutu ile çalışan 3 container görüntülenir.

5- sudo docker container exec -it `sword-client container id'nin ilk 3 karakteri` sh komutu çalıştırılır.

(Örneğin: sudo docker container exec -it b70 sh)

6- Artık server üzerinde komutları yürütüyoruz, ls komutu ile final.json dosyasını görebiliriz. echo final.json komutu
ile dosyanın içeriğini görebiliriz.

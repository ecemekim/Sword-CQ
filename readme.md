**Özet:**

_Sword-CQ/SwordServer/users_ dizinindeki 10 adet json dosyasındaki tüm kayıtları gRPC server üzerinden redis "jsonrows" kuyruğuna aktarır. 
Bu sırada gRPC client servisi mesajı aldığını iletir. Connections dizinindeki redis_connection.py ise kuyruğu dinler ve 
kuyruktaki dataları birleştirerek final.json dosyasını oluşturur. Flask üzerinden tetikleme sonucu oluşturulan 
final.json dosyası sunucuda 
("_Sword-CQ/Connections/final.json_") görüntülenebilir.

**Adımlar:**

1- sudo apt-get install docker komutu çalıştırılır.

2- sudo apt-get install docker-compose komutu çalıştırılır.

3- Sword-CQ dizinindeyken; sudo docker-compose up -d --build komutu çalıştırılır.

4- Terminalde sudo docker container ls komutu ile çalışan 4 container görüntülenir.

5- Lokalde curl localhost:5000/show komutu ile (Browser üzerinden aynı adrese istek atılabilir.) istek tetiklenir. (Flask'a giden istek, gRPC client üzerinden iletilir.)

6- sudo docker container exec -it `swordcq_redis-con_1 container id'nin ilk 3 karakteri` sh komutu çalıştırılır.

(Örneğin: sudo docker container exec -it b70 sh)

7- Artık server üzerinde komutları yürütüyoruz, ls komutu ile final.json dosyasını görebiliriz. cat final.json komutu
ile dosyanın içeriğini görebiliriz.

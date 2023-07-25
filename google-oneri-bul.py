import requests
import json
import string

def get_response_encoding(response):
    # İsteğin karakter kodlamasını tespit etmek için "charset" bilgisini kullanalım
    content_type = response.headers.get("content-type")
    if "charset=" in content_type:
        return content_type.split("charset=")[1]
    else:
        return "ISO-8859-1"  # Varsayılan olarak ISO-8859-1 kullanalım

def google_arama_onerileri(kelime):
    url = f"http://suggestqueries.google.com/complete/search?output=firefox&hl=tr&q={kelime}"
    response = requests.get(url)
    encoding = get_response_encoding(response)
    data = json.loads(response.content.decode(encoding))
    return data[1]

def onerileri_kaydet(giris):
    alfabe = string.ascii_lowercase

    with open('google_onerileri.txt', 'w', encoding='utf-8') as dosya:
        for harf in alfabe:
            kelime = f"{giris} {harf}"
            oneriler = google_arama_onerileri(kelime)
            dosya.write(f"{kelime} için öneriler:\n")
            dosya.write('\n'.join(oneriler) + '\n\n')

if __name__ == "__main__":
    kullanici_girisi = input("Lütfen aramak istediğiniz terimi girin: ")
    onerileri_kaydet(kullanici_girisi)
    print("Öneriler 'google_onerileri.txt' dosyasına kaydedildi.")

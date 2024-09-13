import requests

def get_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            print(f"IP адрес: {ip_address}")
            print(f"Страна: {data['country']}")
            print(f"Регион: {data['regionName']}")
            print(f"Город: {data['city']}")
            print(f"Почтовый индекс: {data['zip']}")
            print(f"Широта: {data['lat']}")
            print(f"Долгота: {data['lon']}")
            print(f"Часовой пояс: {data['timezone']}")
            print(f"Провайдер: {data['isp']}")
        else:
            print(f"Ошибка: {data['message']}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    ip_address = input("Введите IP адрес: ")
    get_location(ip_address)
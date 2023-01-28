import requests
import folium


def get_info_ip(ip):
    try:
        req = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': req.get('query'),
            '[Int prov]': req.get('isp'),
            '[Country]': req.get('country'),
            '[Region]': req.get('regionName'),
            '[ZIP]': req.get('zip'),
            '[Lat]': req.get('lat'),
            '[Lon]': req.get('lon'),
        }

        for k,v in data.items():
            print(f'{k}: {v}')
        area = folium.Map(location=[req.get('lat'),req.get('lon')])
        area.save(f'{req.get("query")}_{req.get("city")}.html')
    except:
        print()


def main():
    ip = (input('Введите ip-адрес:'))

    get_info_ip(ip=ip)


if __name__ == '__main__':
    main()
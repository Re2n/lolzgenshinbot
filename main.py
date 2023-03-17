from marketapi import LolzteamApi
import json
import time
token = LolzteamApi('lolz token')
legendary_list = ['Qiqi', 'Keqing', 'Jean', 'Mona', 'Yae Miko', 'Diluc', 'Klee', 'Tartaglia', 'Eula'
    , 'Shenhe', 'Xiao', 'Ayato', 'Itto', 'Kokomi', 'Venti', 'Albedo', 'Yoimiya', 'Zhongli', 'Hu Tao', 'Ayaka', 'Ganyu',
                  'Yelan', 'Kazuha', 'Raiden Shogun', 'Wanderer', 'Tighnari', 'Nahida']

def get_base():
    base = token.market_list(category='genshin-impact', pmax=250, optional={'legendary_min': 4, 'region': 'os_euro', 'ea': 'no'})
    data = base['items']
    result = []
    for genshinacc in data:
        legendary_list_acc = []
        id = genshinacc['item_id']
        url = 'https://zelenka.guru/market/' + str(genshinacc['item_id'])
        price = genshinacc['price']
        ar = genshinacc['genshin_level']
        region = genshinacc['genshin_region']
        numbers_legendary = genshinacc['genshin_legendary']
        for i in genshinacc['genshinCharacters']:
            if i['name'] in legendary_list:
                legendary_list_acc.append(i['name'])
        info_acc = {
            'id': id,
            'url': url,
            'price': price,
            'ar': ar,
            'region': region,
            'legendary': numbers_legendary,
            'name_of_legendary': legendary_list_acc
        }
        result.append(info_acc)
    with open('baza.json', 'w') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)


def get_fresh_accs():
    with open('baza.json') as f:
        result = json.load(f)
    base = LolzteamApi.market_list(token, category='genshin-impact', pmax=250, optional={'legendary_min': 4, 'region': 'os_euro', 'ea': 'no'})
    data = base['items']
    fresh_result = []
    old_id = []
    for i in range(len(result)):
        old_id.append(result[i]['id'])
    for genshinacc in data:
        legendary_list_acc = []
        id = genshinacc['item_id']
        if id in old_id:
            continue
        else:
            url = 'https://zelenka.guru/market/' + str(genshinacc['item_id'])
            price = genshinacc['price']
            ar = genshinacc['genshin_level']
            region = genshinacc['genshin_region']
            numbers_legendary = genshinacc['genshin_legendary']
            for i in genshinacc['genshinCharacters']:
                if i['name'] in legendary_list:
                    legendary_list_acc.append(i['name'])

            info_acc = {
                'id': id,
                'url': url,
                'price': price,
                'ar': ar,
                'region': region,
                'legendary': numbers_legendary,
                'name_of_legendary': legendary_list_acc
            }
            result.append(info_acc)

            fresh_accs = {
                'id': id,
                'url': url,
                'price': price,
                'ar': ar,
                'region': region,
                'legendary': numbers_legendary,
                'name_of_legendary': legendary_list_acc
            }
            fresh_result.append(fresh_accs)

    with open('baza.json', 'w') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    return fresh_result


def main():
    # get_base()
    print(get_fresh_accs())


if __name__ == '__main__':
    main()
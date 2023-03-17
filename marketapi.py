import requests


class LolzteamApi:
    def __init__(self, token: str, userid: int = None, baseUrl="https://api.zelenka.guru/"):
        self.token = token
        self.userid = userid
        self.baseUrl = baseUrl
        self.session = requests.session()
        self.session.headers = {'Authorization': f'Bearer {self.token}'}

    def get(self, url, params={}):
        return self.session.get(self.baseUrl + url, params=params).json()


    def market_list(self, category: str = None, pmin: int = None, pmax: int = None, title: str = None,
                    parse_sticky_items: str = None, optional: dict = None):
        """Displays a list of latest accounts
        Args:
            category (str, optional): Category on market. Defaults to None.
            pmin (int, optional): Min price for account. Defaults to None.
            pmax (int, optional): Max price for account. Defaults to None.
            title (str, optional): Title for account. Defaults to None.
            parse_sticky_items (str, optional): Condition for parse sticky items. Defaults to None.
            optional (dict, optional): Get from market url params. Defaults to None.
        """

        if category:
            data = {}
            if title: data['title'] = title
            if pmin: data['pmin'] = pmin
            if pmax: data['pmax'] = pmax
            if parse_sticky_items: data['parse_sticky_items'] = parse_sticky_items
            if optional: data = {**data, **optional}
            return self.get(f'market/{category}', data)
        else:
            return self.get('market')
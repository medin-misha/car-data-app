import aiohttp
from bs4 import BeautifulSoup


class CarScraper:
    """
    Класс-парсер автомобилей с сайта AutoRIA.

    После инициализации с параметром `autoria_url`, достаточно вызвать метод `get_full_info()`,
    и все данные будут автоматически спарсены и сохранены в экземпляре класса.

    Attributes:
        autoria_url (str): URL страницы AutoRIA, с которой начинается парсинг.
        links (list[str]): Ссылки на отдельные объявления автомобилей. Заполняются при работе get_auto_links.
        cars (list[dict]): Словари с данными об автомобилях. Заполняеться при работе get_full_info.

    Todo:
        - Убрать блоки try-except и реализовать корректную обработку ошибок.
        - Реализовать нормальную пагинацию.

    Methods:
        get_auto_links():
            Парсит все ссылки на карточки автомобилей по `autoria_url`.
            Сохраняет их в `links` и возвращает список.

        get_car_data_from_link(link: str) -> dict:
            Получает данные автомобиля по ссылке на карточку.
            Возвращает словарь с характеристиками авто.

        get_full_info():
            Если `links` пуст, вызывает `get_auto_links()` для получения всех ссылок.
            Далее проходит по каждой ссылке и вызывает `get_car_data_from_link()` для сбора информации.
            Сохраняет результат в `cars`.
    """

    def __init__(self, autoria_url: str):
        self.autoria_url: str = autoria_url
        self.links: list[str] | None = None
        self.cars: list[dict] | None = None

    async def get_full_info(self) -> list[dict]:
        if self.links is None:
            await self.get_auto_links()
        self.cars: list[dict] = [
            await self.get_car_data_from_link(link) for link in self.links
        ]
        return self.cars

    async def get_auto_links(self) -> list[str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.autoria_url) as response:
                text: str = await response.text()
                soap = BeautifulSoup(text, "html.parser")
                links = soap.find_all("a", class_="address")
                self.links = [tag.attrs.get("href") for tag in links]
                return self.links

    async def get_car_data_from_link(self, link: str) -> dict | None:
        car_data: dict = {}
        async with aiohttp.ClientSession() as session:
            async with session.get(url=link) as response:
                try:
                    text: str = await response.text()
                    soap = BeautifulSoup(text, "html.parser")

                    company_model_year: list = soap.find(
                        "h1",
                    ).text.split()
                    company: str = company_model_year[0]
                    model: str = "".join([i + " " for i in company_model_year[1:-1]])
                    production_year: str = company_model_year[-1]
                    price: str = (
                        soap.find("div", class_="price_value")
                        .find("strong")
                        .text.strip()[:-1]
                        .strip()
                    )
                    mileage: str = (
                        soap.find("dd", class_="mhide")
                        .find("span", class_="argument")
                        .text
                    )
                    engine: str = (
                        soap.find("div", id="details")
                        .find_all("dd")[2]
                        .find("span", class_="argument")
                        .text.strip()
                        .replace("\n", "")
                        .replace("•", "")
                        .replace(" ", "")
                    )
                    location: str = (
                        soap.find("div", id="breadcrumbs")
                        .find_all("div", class_="item")[3]
                        .text.strip()
                    )
                    photo_url: str = (
                        soap.find_all("picture")[0].find("img").attrs.get("src")
                    )
                    car_data["company"] = company
                    car_data["model"] = model
                    car_data["production_year"] = production_year
                    car_data["price"] = price
                    car_data["mileage"] = mileage
                    car_data["engine"] = engine
                    car_data["location"] = location
                    car_data["photo_url"] = photo_url
                    return car_data
                except AttributeError:
                    return

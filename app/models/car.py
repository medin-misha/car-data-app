from beanie import Document, Indexed, PydanticObjectId


class Car(Document):
    """
    Модель машины, которая храниться в базе данных.
    Поля company и production_year индексируються, для более быстрого поиска.
    """

    company: Indexed(str)
    model: str
    production_year: Indexed(int)
    price: float
    mileage: str
    engine: str
    location: str
    photo_url: str

    class Settings:
        name = "cars"

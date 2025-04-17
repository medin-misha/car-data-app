from beanie import Document, Indexed, PydanticObjectId


class Car(Document):
    """
    Модель машины, которая храниться в базе данных.
    Поля company и production_year индексируються, для более быстрого поиска.
    """

    company: Indexed(str)
    model: Indexed(str, unique=True)
    production_year: int
    price: float
    mileage: Indexed(str, unique=True)
    engine: str
    location: str
    photo_url: str

    class Settings:
        name = "cars"

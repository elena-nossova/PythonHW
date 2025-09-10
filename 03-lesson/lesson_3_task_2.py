from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79 122 22 22"))
catalog.append(Smartphone("Samsung", "Galaxy А06", "+79 222 22 22"))
catalog.append(Smartphone("Xiaomi", "Redmi 9T", "+79 322 22 22"))
catalog.append(Smartphone("Huawei", "Mate X6", "+79 422 22 22"))
catalog.append(Smartphone("OnePlus", "13", "+79 522 22 22"))


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")


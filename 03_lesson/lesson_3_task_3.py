from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Тургенева", "10" , "5")
from_addr = Address("147800", "Липецк", "Пушкина", "25" , "108")

mail = Mailing(to_address=to_addr, from_address=from_addr, cost=300.50, track="TRACK123456")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, "
      f"{mail.from_address.house} - {mail.from_address.flat} в "
      f"{mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
      f"{mail.to_address.house} - {mail.to_address.flat}. Стоимость {mail.cost} рублей.")

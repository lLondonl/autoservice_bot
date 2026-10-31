import os

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# ===== Тексты и варианты — всё, что меняется под клиента =====
COMPANY = "Автосервис «Мотор»"
WELCOME = "Здравствуйте! Запишу вас в автосервис за минуту."
ASK_CHOICE = "Какая услуга нужна?"
CHOICES = ["ТО и замена масла", "Диагностика", "Шиномонтаж", "Ремонт ходовой"]
ASK_AMOUNT = "Когда вам удобно? Напишите день и время"
ASK_PLACE = "Марка и модель автомобиля?"
ASK_PHONE = "Ваш телефон для связи?"
CONTACTS = "Звоните: +7 900 000-00-00\nАдрес: ул. Примерная, 1"

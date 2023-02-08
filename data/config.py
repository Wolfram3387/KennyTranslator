import os


BOT_TOKEN = '5420378076:AAEO0HOIckXciOSpaLAZ3aohJ7Sj4K4cYE0'
admins = [
    1099391285,  # Мой телеграм id
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

import os


BOT_TOKEN = ''
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

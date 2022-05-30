def progress(result: int, max=63, name='Шкала депресcии Бека') -> str:
    """Функция для построения индивидуальной шкалы депрессии Бека"""
    max_symbol = 20
    sumbol = '#'
    pass_sumbol = ' | '
    count_symbol = int(result * max_symbol / max)
    remainder = max_symbol - count_symbol
    answer = (name +
            pass_sumbol +
            (sumbol*count_symbol) +
            ('   ' * remainder) +
            pass_sumbol +
            f'{result}/{max}')

    return answer

def rating_scale(result: int) -> str:
    """Функция преобразования результата из шкалы Бека в диагноз"""
    if result in range(0, 10):
        diagnostic = 'отсутствие депрессивных симптомов.'
    elif result in range(10, 16):
        diagnostic = 'легкая депрессия(субдепрессия). Рекомендуется предпринять следующие шаги:\n\n'
        diagnostic += ' - Наладьте режим сна и бодрствования\n'
        diagnostic += ' - Обеспечьте себе сбалансированное и разнообразное питание\n'
        diagnostic += ' - Заботьтесь о своем теле\n'
        diagnostic += ' - Займитесь делом\n'
        diagnostic += ' - Общайтесь с окружающим миром\n'
        diagnostic += ' - Думайте о будущем\n\n'
        diagnostic += 'При ухудшении состояния стоит обратится за психологической помощью'
    elif result in range(16, 20):
        diagnostic = 'умеренная депрессия\nПо возможности стоит обратится за психологической помощью.\n'
        diagnostic += 'Также требуется изоляция от внешних раздражителей, психологическая поддержка, нормализация сна, по согласованию с врачем прием лекарств\n'
    elif result in range(20, 30):
        diagnostic = 'выраженная депрессия средней тяжести.\nНастоятельно рекомендуем обратится за психологической помощью.\n'
        diagnostic += 'Сайт для бесплтной психологической консультации:\nhttps://psyalter.ru/besplatnaya-psikhologicheskaya-pomosch'
    elif result in range(30, 64):
        diagnostic = 'тяжелая депрессия.\nНеобходимо обратится за психологической помощью.\n'
        diagnostic += 'Сайт для бесплтной психологической консультации:\nhttps://psyalter.ru/besplatnaya-psikhologicheskaya-pomosch'
    return diagnostic
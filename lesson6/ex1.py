def get_errors(*errors):

    output = []

    mistakes = {'out': 'Вы вышли из системы ',
                'noaccess': 'У вас нет доступа в этот раздел',
                'unknown': 'Неизвестная ошибка',
                'timeout': 'Система долго не отвечает',
                'robot': 'Ваши действия похожи на робота',
                }

    for i in errors:
        output.append(mistakes[i])

    return output

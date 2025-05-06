import json
import os
from datetime import datetime


keyboard_order = list("QWERTYUIOPASDFGHJKLZXCVBNM")


def save_creature_to_db(creature, filename="creature_database.json"):
    creature_id = 
    cells_data = [{
        "x": cell.x,
        "y": cell.y,
        "color": cell.color
    } for cell in creature.cells]
    rules_data = {}
    for color, rule in creature.rules.items():
        rules_data[color] = {
            "exist_with": rule.exist_with,
            "exist_color": rule.exist_color,
            "nonexist_with": rule.nonexist_with,
            "nonexist_color": rule.nonexist_color
        }
    creature_data = {
        "id": creature_id,
        "created_at": datetime.now().isoformat(),
        "cells": cells_data,
        "rules": rules_data
    }

    # Загружаем существующую базу
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                database = json.load(f)
            except json.JSONDecodeError:
                database = []
    else:
        database = []

    # Добавляем нового
    database.append(creature_data)

    # Сохраняем обратно
    with open(filename, "w") as f:
        json.dump(database, f, indent=2)

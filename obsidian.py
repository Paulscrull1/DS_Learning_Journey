import os

# Укажи корневую папку для Obsidian vault
VAULT_PATH = r"A:\Data_Science_Course\Obsidian-notes"

# Структура папок
FOLDERS = [
    "📚 Curriculum",
    "📖 Resources",
    "🧪 Concepts",
    "📝 Daily_Notes",  # можно использовать с плагином Daily Notes
]

# Файлы и их содержимое
FILES = {
    "📚 Curriculum/00_Intro_and_Tools.md": """# 📚 Модуль 0: Введение и инструменты

## Цель
Понять, что такое Data Science, и настроить рабочую среду.

## Ключевые понятия
- [[Data Science]]
- [[Machine Learning]]
- [[Data Analyst vs Data Scientist]]

## Что изучено
- [x] Что такое Data Science (IBM, Towards Data Science)
- [x] Основы Python (CS50P, Python Crash Course)
- [x] Установка Anaconda, VS Code, Git
- [x] Первый Python-скрипт: `stats_calculator.py`
- [x] Подключение к GitHub
- [x] Настройка Jupyter в VS Code
- [ ] Настройка Obsidian ✅

## Ресурсы
- [IBM: What is Data Science?](https://www.ibm.com/topics/data-science)
- [Python Crash Course — официальный репозиторий](https://ehmatthes.github.io/pcc_2e/)

## Связанные файлы
- [[Pandas]]
- [[Jupyter]]
- [[Git]]

## Теги
#module/0 #setup #tools
""",
    "📚 Curriculum/01_Data_Wrangling.md": "# 📚 Модуль 1: Работа с данными (Data Wrangling & EDA)\n\n## Цель\nНаучиться загружать, очищать, анализировать и визуализировать данные.\n\n## Теги\n#module/1 #pandas #eda",
    "📚 Curriculum/02_Statistics.md": "# 📚 Модуль 2: Статистика и выводы\n\n## Цель\nПонимать, как делать обоснованные выводы из данных.\n\n## Теги\n#module/2 #statistics #hypothesis-testing",
    "📚 Curriculum/03_Machine_Learning.md": "# 📚 Модуль 3: Машинное обучение (основы)\n\n## Цель\nПонимать и применять основные алгоритмы ML.\n\n## Теги\n#module/3 #machine-learning #scikit-learn",
    "📚 Curriculum/04_Advanced_Topics.md": "# 📚 Модуль 4: Продвинутые темы\n\n## Цель\nУглубиться в выбранное направление (DL, NLP, Time Series, Big Data).\n\n## Теги\n#module/4 #deep-learning #nlp #time-series",
    "📚 Curriculum/05_Portfolio_and_Career.md": "# 📚 Модуль 5: Портфолио, продакшн и карьера\n\n## Цель\nПодготовиться к рынку труда и построить личный бренд.\n\n## Теги\n#module/5 #portfolio #career",
    
    "📖 Resources/Books.md": "# 📖 Книги\n\n- *Python for Data Analysis* — Wes McKinney\n- *Practical Statistics for Data Scientists* — Bruce & Gedeck\n- *Hands-On Machine Learning* — Aurélien Géron\n\n## Теги\n#resources/books",
    "📖 Resources/Courses.md": "# 📖 Курсы\n\n- [Coursera: Statistics with Python (UMich)](https://www.coursera.org/specializations/statistics-with-python)\n- [Andrew Ng: Machine Learning](https://www.coursera.org/learn/machine-learning)\n- [Kaggle Learn](https://www.kaggle.com/learn)\n\n## Теги\n#resources/courses",
    "📖 Resources/Cheat_Sheets.md": "# 📖 Шпаргалки\n\n- Pandas Cheat Sheet\n- Scikit-learn Algorithm Map\n- SQL for Data Analysis\n\n## Теги\n#resources/cheatsheets",
    
    "🧪 Concepts/EDA.md": "# 🧪 EDA (Exploratory Data Analysis)\n\nПервичный анализ данных для понимания структуры, распределений, аномалий.\n\n## Теги\n#concept/eda",
    "🧪 Concepts/Hypothesis_Testing.md": "# 🧪 Проверка гипотез\n\nМетоды: t-test, chi-square, p-value, доверительные интервалы.\n\n## Теги\n#concept/statistics #hypothesis-testing",
    "🧪 Concepts/Pandas.md": "# 🧪 Pandas\n\nОсновная библиотека для работы с табличными данными в Python.\n\n## Теги\n#concept/pandas #python",
    ".Tags.md": "# 🏷️ Обзор тегов\n\n- `#module/0` … `#module/5` — модули курса\n- `#concept/...` — ключевые концепции\n- `#resources/...` — источники\n- `#setup`, `#tools`, `#portfolio` — прочие метки\n\n## Теги\n#meta/tags",
}

def create_structure():
    # Создаём корневую папку
    os.makedirs(VAULT_PATH, exist_ok=True)
    
    # Создаём папки
    for folder in FOLDERS:
        full_path = os.path.join(VAULT_PATH, folder)
        os.makedirs(full_path, exist_ok=True)
        print(f"✅ Папка создана: {full_path}")
    
    # Создаём файлы
    for relative_path, content in FILES.items():
        full_path = os.path.join(VAULT_PATH, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"📄 Файл создан: {full_path}")

if __name__ == "__main__":
    create_structure()
    print("\n🎉 Структура Obsidian vault успешно создана!")
    print(f"Открой Obsidian и выбери папку: {VAULT_PATH}")
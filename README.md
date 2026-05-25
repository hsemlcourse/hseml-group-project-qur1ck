[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kOqwghv0)

# ML Project — Прогноз глобальной температуры Земли

**Студент:** Куров Егор

**Группа:** БИВ234

## Оглавление

1. [Описание задачи](#описание-задачи)
2. [Структура репозитория](#структура-репозитория)
3. [Запуск](#запуск)
4. [Данные](#данные)
5. [Результаты](#результаты)
6. [Отчёт](#отчёт)

## Описание задачи

**Задача:** Регрессия — прогнозирование средней глобальной температуры Земли на следующий месяц

**Датасет:** Berkeley Earth Surface Temperature Data (Kaggle) — `GlobalTemperatures.csv`

**Целевая метрика:** MAE (средняя абсолютная ошибка) — интерпретируема в градусах Цельсия

**Дополнительные метрики:** RMSE, R²

## Структура репозитория
.
├── data
│ ├── raw # Исходный датасет GlobalTemperatures.csv
│ └── processed # Обработанные данные (при необходимости)
├── models # Сохранённые модели (LinearRegression.joblib)
├── notebooks
│ └── 01_eda.ipynb # Полный пайплайн: EDA, очистка, фичи, модели
├── presentation # Презентация для защиты
├── report
│ ├── images # Изображения для отчёта
│ └── report.md # Финальный отчёт
├── src
│ ├── preprocessing.py # Предобработка данных
│ └── modeling.py # Обучение и оценка моделей
├── tests
│ └── test.py # Тесты пайплайна
├── requirements.txt
└── README.md

## Запуск

### Локальный запуск (VS Code / терминал)

bash
# 1. Клонировать репозиторий
git clone https://github.com/hsemlcourse/hseml-group-project-qur1ck.git
cd hseml-group-project-qur1ck

# 2. Создать виртуальное окружение
python -m venv venv
source venv/Scripts/activate    # Windows
# source venv/bin/activate      # Linux/macOS

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить Jupyter и открыть notebooks/01_eda.ipynb
jupyter notebook

## Запуск в Google Colab
Проект разрабатывался в Google Colab. Ноутбук notebooks/01_eda.ipynb можно:

# Загрузить в Google Colab

# Загрузить датасет через from google.colab import files

# Выполнить все ячейки последовательно

# Данные
Источник: Berkeley Earth Climate Change Data

Файл: GlobalTemperatures.csv

Объём: 3,192 строки → после очистки 3,180 строк

Период: 1750–2015 гг.

Целевая переменная: LandAverageTemperature

Feature Engineering
Из даты: year, month, season

Лаговые признаки: temp_lag1, temp_lag2, temp_lag12

# Результаты
Модель	MAE (°C)	RMSE (°C)	R²
Linear Regression (Baseline)	0.329	0.415	0.990
Random Forest	0.449	0.570	0.981
XGBoost	0.332	0.418	0.990
LightGBM	0.337	0.425	0.989
Наивный прогноз (среднее)	3.804	-	-
🏆 Финальная модель: Linear Regression (MAE = 0.33°C)

# Коэффициенты модели:
text
Temperature = -0.435 + 0.0006×year - 0.0095×month + 0.5865×temp_lag1 - 0.3267×temp_lag2 + 0.6531×temp_lag12

# Выводы:
Модель предсказывает температуру с ошибкой всего 0.33°C

Самый важный признак — температура год назад (temp_lag12)

Глобальное потепление подтверждается, но очень слабо (+0.0006°C в год)

# Отчёт
Финальный отчёт: report/report.md

# Требования к окружению
Все зависимости указаны в requirements.txt. Основные библиотеки:

pandas, numpy — обработка данных

scikit-learn — Linear Regression, Random Forest

xgboost, lightgbm — градиентный бустинг

matplotlib, seaborn — визуализация

## Воспроизводимость

- **Seed:** 42 (фиксирован во всех экспериментах)
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 6)
pd.set_option('display.max_columns', None)

data_set = pd.read_excel("D:/prog/lab4/p4/data.xlsx", "DATA")

print("=== ИНФОРМАЦИЯ О ДАННЫХ ===")
print(f"Размер датасета: {data_set.shape}")
print(f"Колонки: {data_set.columns.tolist()}")
print("\nТипы данных:")
print(data_set.dtypes)
print("\nПервые 5 строк:")
display(data_set.head())

print("\n=== ПРОПУЩЕННЫЕ ЗНАЧЕНИЯ ===")
missing_data = data_set.isnull().sum()
missing_percent = (missing_data / len(data_set)) * 100
missing_info = pd.DataFrame({'Количество': missing_data, 'Процент': missing_percent})
display(missing_info[missing_info['Количество'] > 0])

print("\n=== ПРЕОБРАЗОВАНИЕ ДАННЫХ ===")
data_set['ISSUE_DATE'] = pd.to_datetime(data_set['ISSUE_DATE'])
data_set['FLIGHT_DATE_LOC'] = pd.to_datetime(data_set['FLIGHT_DATE_LOC'])

data_set['issue_month'] = data_set['ISSUE_DATE'].dt.month
data_set['issue_year'] = data_set['ISSUE_DATE'].dt.year
data_set['issue_quarter'] = data_set['ISSUE_DATE'].dt.quarter
data_set['issue_dayofweek'] = data_set['ISSUE_DATE'].dt.dayofweek

data_set['flight_month'] = data_set['FLIGHT_DATE_LOC'].dt.month
data_set['flight_year'] = data_set['FLIGHT_DATE_LOC'].dt.year
data_set['days_before_flight'] = (data_set['FLIGHT_DATE_LOC'] - data_set['ISSUE_DATE']).dt.days

print("\n=== ОБЩИЕ ДЕСКРИПТИВНЫЕ СТАТИСТИКИ ===")
numeric_columns = data_set.select_dtypes(include=[np.number]).columns
if len(numeric_columns) > 0:
    display(data_set[numeric_columns].describe())

print("\n=== АНАЛИЗ АЭРОПОРТОВ ===")

print("\n--- Топ-10 городов отправления ---")
orig_city_analysis = data_set.groupby('ORIG_CITY_CODE').agg({
    'ORIG_CITY_CODE': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'ORIG_CITY_CODE': 'count'}).reset_index()
orig_city_analysis = orig_city_analysis.sort_values('count', ascending=False)

display(orig_city_analysis.head(10))

print("\n--- Топ-10 городов назначения ---")
dest_city_analysis = data_set.groupby('DEST_CITY_CODE').agg({
    'DEST_CITY_CODE': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'DEST_CITY_CODE': 'count'}).reset_index()
dest_city_analysis = dest_city_analysis.sort_values('count', ascending=False)

display(dest_city_analysis.head(10))

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
top_orig = orig_city_analysis.head(10)
plt.bar(top_orig['ORIG_CITY_CODE'].astype(str), top_orig['count'])
plt.title('Топ-10 городов отправления по количеству продаж')
plt.xticks(rotation=45)
plt.ylabel('Количество продаж')

plt.subplot(2, 2, 2)
top_dest = dest_city_analysis.head(10)
plt.bar(top_dest['DEST_CITY_CODE'].astype(str), top_dest['count'])
plt.title('Топ-10 городов назначения по количеству продаж')
plt.xticks(rotation=45)
plt.ylabel('Количество продаж')

plt.subplot(2, 2, 3)
plt.bar(top_orig['ORIG_CITY_CODE'].astype(str), top_orig['REVENUE_AMOUNT'])
plt.title('Топ-10 городов отправления по выручке')
plt.xticks(rotation=45)
plt.ylabel('Сумма выручки')

plt.subplot(2, 2, 4)
plt.bar(top_dest['DEST_CITY_CODE'].astype(str), top_dest['REVENUE_AMOUNT'])
plt.title('Топ-10 городов назначения по выручке')
plt.xticks(rotation=45)
plt.ylabel('Сумма выручки')

plt.tight_layout()
plt.show()

print("\n=== АНАЛИЗ СЕЗОННОСТИ ===")

monthly_sales = data_set.groupby('issue_month').agg({
    'ISSUE_DATE': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'ISSUE_DATE': 'count'}).reset_index()

monthly_flights = data_set.groupby('flight_month').agg({
    'FLIGHT_DATE_LOC': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'FLIGHT_DATE_LOC': 'count'}).reset_index()

plt.figure(figsize=(15, 10))

months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

plt.subplot(2, 2, 1)
plt.bar(monthly_sales['issue_month'], monthly_sales['count'])
plt.title('Продажи по месяцам (покупка)')
plt.xlabel('Месяц')
plt.ylabel('Количество продаж')
plt.xticks(range(1, 13), months, rotation=45)

plt.subplot(2, 2, 2)
plt.bar(monthly_flights['flight_month'], monthly_flights['count'])
plt.title('Перелеты по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество перелетов')
plt.xticks(range(1, 13), months, rotation=45)

plt.subplot(2, 2, 3)
if 'issue_year' in data_set.columns:
    seasonality_heatmap = data_set.groupby(['issue_year', 'issue_month']).size().unstack(fill_value=0)
    sns.heatmap(seasonality_heatmap, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5)
    plt.title('Сезонность продаж по годам и месяцам')

plt.subplot(2, 2, 4)
plt.plot(monthly_sales['issue_month'], monthly_sales['REVENUE_AMOUNT'], marker='o', linewidth=2)
plt.title('Выручка по месяцам покупки')
plt.xlabel('Месяц')
plt.ylabel('Сумма выручки')
plt.xticks(range(1, 13), months, rotation=45)

plt.tight_layout()
plt.show()

print("\n=== АНАЛИЗ ТИПОВ ПАССАЖИРОВ ===")

pax_analysis = data_set['PAX_TYPE'].value_counts().reset_index()
pax_analysis.columns = ['PAX_TYPE', 'count']

pax_revenue = data_set.groupby('PAX_TYPE').agg({
    'REVENUE_AMOUNT': ['sum', 'mean', 'count']
}).round(2)
pax_revenue.columns = ['total_revenue', 'avg_revenue', 'count']
pax_revenue = pax_revenue.sort_values('total_revenue', ascending=False)

print("Анализ по типам пассажиров:")
display(pax_revenue)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.pie(pax_analysis['count'], labels=pax_analysis['PAX_TYPE'], autopct='%1.1f%%')
plt.title('Распределение по типам пассажиров')

plt.subplot(1, 3, 2)
plt.bar(pax_revenue.index.astype(str), pax_revenue['total_revenue'])
plt.title('Общая выручка по типам пассажиров')
plt.xticks(rotation=45)
plt.ylabel('Сумма выручки')

plt.subplot(1, 3, 3)
plt.bar(pax_revenue.index.astype(str), pax_revenue['avg_revenue'])
plt.title('Средний чек по типам пассажиров')
plt.xticks(rotation=45)
plt.ylabel('Средняя выручка')

plt.tight_layout()
plt.show()

print("\n=== АНАЛИЗ ПРОГРАММЫ ЛОЯЛЬНОСТИ ===")

ffp_analysis = data_set.groupby('FFP_FLAG').agg({
    'FFP_FLAG': 'count',
    'REVENUE_AMOUNT': ['sum', 'mean']
}).round(2)
ffp_analysis.columns = ['count', 'total_revenue', 'avg_revenue']
ffp_analysis = ffp_analysis.sort_values('count', ascending=False)

print("Анализ программы лояльности:")
display(ffp_analysis)

print("\n=== АНАЛИЗ СПОСОБОВ ОПЛАТЫ (ТОП-10) ===")

all_payments = data_set.groupby('FOP_TYPE_CODE').agg({
    'FOP_TYPE_CODE': 'count',
    'REVENUE_AMOUNT': ['sum', 'mean']
}).round(2)
all_payments.columns = ['count', 'total_revenue', 'avg_revenue']
all_payments = all_payments.sort_values('count', ascending=False)

payment_analysis = all_payments.head(10)

print("Топ-10 способов оплаты:")
display(payment_analysis)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.pie(payment_analysis['count'], labels=payment_analysis.index.astype(str), autopct='%1.1f%%')
plt.title('Топ-10 способов оплаты (распределение)')

plt.subplot(1, 3, 2)
plt.bar(payment_analysis.index.astype(str), payment_analysis['total_revenue'])
plt.title('Топ-10 способов оплаты по выручке')
plt.xticks(rotation=45)
plt.ylabel('Сумма выручки')

plt.subplot(1, 3, 3)
plt.bar(payment_analysis.index.astype(str), payment_analysis['avg_revenue'])
plt.title('Топ-10 способов оплаты по среднему чеку')
plt.xticks(rotation=45)
plt.ylabel('Средняя выручка')

plt.tight_layout()
plt.show()

print("\n=== АНАЛИЗ ТИПОВ ПЕРЕЛЕТОВ ===")

route_analysis = data_set.groupby('ROUTE_FLIGHT_TYPE').agg({
    'ROUTE_FLIGHT_TYPE': 'count',
    'REVENUE_AMOUNT': ['sum', 'mean']
}).round(2)
route_analysis.columns = ['count', 'total_revenue', 'avg_revenue']
route_analysis = route_analysis.sort_values('count', ascending=False)

print("Анализ типов перелетов:")
display(route_analysis)

print("\n=== АНАЛИЗ СПОСОБОВ ПОКУПКИ ===")

sale_analysis = data_set.groupby('SALE_TYPE').agg({
    'SALE_TYPE': 'count',
    'REVENUE_AMOUNT': ['sum', 'mean']
}).round(2)
sale_analysis.columns = ['count', 'total_revenue', 'avg_revenue']
sale_analysis = sale_analysis.sort_values('count', ascending=False)

print("Анализ способов покупки:")
display(sale_analysis)

print("\n=== ПРОГНОЗИРОВАНИЕ ОБЪЕМОВ ПРОДАЖ ===")

daily_sales_ts = data_set.groupby('ISSUE_DATE').agg({
    'ISSUE_DATE': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'ISSUE_DATE': 'ticket_count'}).reset_index()

daily_sales_ts = daily_sales_ts.sort_values('ISSUE_DATE')

daily_flights_ts = data_set.groupby('FLIGHT_DATE_LOC').agg({
    'FLIGHT_DATE_LOC': 'count'
}).rename(columns={'FLIGHT_DATE_LOC': 'flight_count'}).reset_index()
daily_flights_ts = daily_flights_ts.sort_values('FLIGHT_DATE_LOC')

daily_sales_ts['ticket_ma_7'] = daily_sales_ts['ticket_count'].rolling(window=7).mean()
daily_sales_ts['ticket_ma_30'] = daily_sales_ts['ticket_count'].rolling(window=30).mean()
daily_sales_ts['revenue_ma_7'] = daily_sales_ts['REVENUE_AMOUNT'].rolling(window=7).mean()

daily_flights_ts['flight_ma_7'] = daily_flights_ts['flight_count'].rolling(window=7).mean()
daily_flights_ts['flight_ma_30'] = daily_flights_ts['flight_count'].rolling(window=30).mean()

plt.figure(figsize=(16, 12))

plt.subplot(3, 1, 1)
plt.plot(daily_sales_ts['ISSUE_DATE'], daily_sales_ts['ticket_count'],
         alpha=0.3, label='Фактические продажи', linewidth=1, color='blue')
plt.plot(daily_sales_ts['ISSUE_DATE'], daily_sales_ts['ticket_ma_7'],
         label='Тренд (7 дней)', linewidth=2, color='red')
plt.plot(daily_sales_ts['ISSUE_DATE'], daily_sales_ts['ticket_ma_30'],
         label='Тренд (30 дней)', linewidth=2, color='green')
plt.title('Динамика продаж билетов и тренды')
plt.xlabel('Дата')
plt.ylabel('Количество билетов')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(3, 1, 2)
plt.plot(daily_sales_ts['ISSUE_DATE'], daily_sales_ts['REVENUE_AMOUNT'],
         alpha=0.3, label='Фактическая выручка', linewidth=1, color='orange')
plt.plot(daily_sales_ts['ISSUE_DATE'], daily_sales_ts['revenue_ma_7'],
         label='Тренд выручки (7 дней)', linewidth=2, color='red')
plt.title('Динамика выручки')
plt.xlabel('Дата')
plt.ylabel('Сумма выручки')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(3, 1, 3)
plt.plot(daily_flights_ts['FLIGHT_DATE_LOC'], daily_flights_ts['flight_count'],
         alpha=0.3, label='Фактические перелеты', linewidth=1, color='purple')
plt.plot(daily_flights_ts['FLIGHT_DATE_LOC'], daily_flights_ts['flight_ma_7'],
         label='Тренд (7 дней)', linewidth=2, color='red')
plt.plot(daily_flights_ts['FLIGHT_DATE_LOC'], daily_flights_ts['flight_ma_30'],
         label='Тренд (30 дней)', linewidth=2, color='green')
plt.title('Динамика количества перелетов и тренды')
plt.xlabel('Дата')
plt.ylabel('Количество перелетов')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n--- Прогноз на основе сезонных patterns ---")

monthly_avg = data_set.groupby('issue_month').agg({
    'ISSUE_DATE': 'count',
    'REVENUE_AMOUNT': 'sum'
}).rename(columns={'ISSUE_DATE': 'avg_tickets', 'REVENUE_AMOUNT': 'avg_revenue'})

monthly_avg['avg_tickets'] = monthly_avg['avg_tickets'] / len(data_set['issue_year'].unique())
monthly_avg['avg_revenue'] = monthly_avg['avg_revenue'] / len(data_set['issue_year'].unique())

print("Среднемесячные показатели:")
display(monthly_avg.round(2))

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.bar(monthly_avg.index, monthly_avg['avg_tickets'])
plt.title('Среднемесячное количество продаж (для прогнозирования)')
plt.xlabel('Месяц')
plt.ylabel('Среднее количество билетов')
plt.xticks(range(1, 13), months, rotation=45)

plt.subplot(1, 2, 2)
plt.bar(monthly_avg.index, monthly_avg['avg_revenue'])
plt.title('Среднемесячная выручка (для прогнозирования)')
plt.xlabel('Месяц')
plt.ylabel('Средняя выручка')
plt.xticks(range(1, 13), months, rotation=45)

plt.tight_layout()
plt.show()

if len(daily_sales_ts) > 60:
    last_30_days = daily_sales_ts['ticket_count'].tail(30).mean()
    prev_30_days = daily_sales_ts['ticket_count'].tail(60).head(30).mean()

    growth_rate = ((last_30_days - prev_30_days) / prev_30_days) * 100

    print(f"\n--- Анализ динамики ---")
    print(f"Средние продажи за последние 30 дней: {last_30_days:.1f} билетов/день")
    print(f"Средние продажи за предыдущие 30 дней: {prev_30_days:.1f} билетов/день")
    print(f"Темп роста: {growth_rate:+.1f}%")

if 'ticket_ma_30' in daily_sales_ts.columns:
    current_trend = daily_sales_ts['ticket_ma_30'].dropna().iloc[-1]
    print(f"\n--- Базовый прогноз ---")
    print(f"Текущий тренд продаж: {current_trend:.1f} билетов/день")
    print(f"Прогноз на следующий месяц: {current_trend * 30:.0f} билетов")

print("\n=== СВОДНЫЙ АНАЛИЗ ===")

print("1. ОБЩИЕ СТАТИСТИКИ:")
print(f"   - Всего записей: {len(data_set):,}")
print(f"   - Период данных: {data_set['ISSUE_DATE'].min().strftime('%Y-%m-%d')} - {data_set['ISSUE_DATE'].max().strftime('%Y-%m-%d')}")
print(f"   - Общая выручка: {data_set['REVENUE_AMOUNT'].sum():,.2f}")
print(f"   - Средний чек: {data_set['REVENUE_AMOUNT'].mean():.2f}")
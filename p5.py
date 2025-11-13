import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import warnings

warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (12, 8)
sns.set_style("whitegrid")

data = pd.read_excel("lab_4_part_5.xlsx", "Данные", skiprows=1)
print("Данные загружены")

data['Средняя_цена'] = data['Продажи'] / data['Количество']
data['Прибыль'] = data['Продажи'] - data['Себестоимость']
data['Рентабельность'] = (data['Прибыль'] / data['Продажи'] * 100).round(2)

print("\n=== ОБЩИЙ АНАЛИЗ ===")
total_sales = data['Продажи'].sum()
print(f"Товарооборот: {total_sales:,.0f} руб.")
print(f"Прибыль: {data['Прибыль'].sum():,.0f} руб.")
print(f"Точки: {data['точка'].nunique()}, Товары: {data['товар'].nunique()}")

print("\n=== АНАЛИЗ ПО ТОЧКАМ ===")
point_stats = data.groupby('точка').agg({
    'Продажи': 'sum', 'Прибыль': 'sum', 'Рентабельность': 'mean', 'Количество': 'sum'
}).round(2).sort_values('Продажи', ascending=False)
print(point_stats)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
point_stats['Продажи'].plot(kind='bar', ax=axes[0, 0], title='Продажи по точкам', color='skyblue')
point_stats['Прибыль'].plot(kind='bar', ax=axes[0, 1], title='Прибыль по точкам', color='lightgreen')
point_stats['Рентабельность'].plot(kind='bar', ax=axes[1, 0], title='Рентабельность по точкам (%)', color='coral')
point_stats['Количество'].plot(kind='bar', ax=axes[1, 1], title='Количество продаж по точкам', color='gold')
plt.tight_layout()
plt.show()

print("\n=== АНАЛИЗ ПО ТОВАРАМ (ТОП-10) ===")
product_stats = data.groupby('товар').agg({
    'Продажи': 'sum', 'Прибыль': 'sum', 'Рентабельность': 'mean',
    'Количество': 'sum', 'Средняя_цена': 'mean'
}).round(2).sort_values('Продажи', ascending=False)

top_products = product_stats.head(10)
print(top_products)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
top_products['Продажи'].plot(kind='bar', ax=axes[0, 0], title='Топ-10 товаров по продажам', color='lightblue')
top_products['Рентабельность'].plot(kind='bar', ax=axes[0, 1], title='Топ-10 по рентабельности', color='lightcoral')
top_products['Количество'].plot(kind='bar', ax=axes[1, 0], title='Топ-10 по количеству', color='lightgreen')
top_products['Средняя_цена'].plot(kind='bar', ax=axes[1, 1], title='Средняя цена топ-10', color='khaki')
plt.tight_layout()
plt.show()

print("\n=== ДИНАМИКА ПРОДАЖ С ПРОГНОЗОМ ===")
monthly_data = data.groupby('Год-мес').agg({
    'Продажи': 'sum', 'Прибыль': 'sum', 'Количество': 'sum', 'Рентабельность': 'mean'
}).round(2)

monthly_data.index = pd.to_datetime(monthly_data.index.astype(str), format='%Y%m')
monthly_data = monthly_data.sort_index()


def forecast_timeseries(series, periods=3):
    if len(series) < 2:
        return None, None

    x = np.array(range(len(series))).reshape(-1, 1)
    y = series.values

    model = LinearRegression()
    model.fit(x, y)

    future_x = np.array(range(len(series), len(series) + periods)).reshape(-1, 1)
    model_forecast = model.predict(future_x)

    return model_forecast, model


forecast_periods = 3
future_dates = [monthly_data.index[-1] + pd.DateOffset(months=i + 1) for i in range(forecast_periods)]

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

sales_forecast, sales_model = forecast_timeseries(monthly_data['Продажи'])
axes[0, 0].plot(monthly_data.index, monthly_data['Продажи'] / 1000, marker='o', label='История', linewidth=2,
                color='blue')
if sales_forecast is not None:
    axes[0, 0].plot(future_dates, sales_forecast / 1000, marker='s', label='Прогноз', linestyle='--', linewidth=2,
                    color='red')
axes[0, 0].set_title('Динамика товарооборота с прогнозом\n(тыс. руб.)')
axes[0, 0].legend()
axes[0, 0].tick_params(axis='x', rotation=45)

profit_forecast, profit_model = forecast_timeseries(monthly_data['Прибыль'])
axes[0, 1].plot(monthly_data.index, monthly_data['Прибыль'] / 1000, marker='o', label='История', linewidth=2,
                color='orange')
if profit_forecast is not None:
    axes[0, 1].plot(future_dates, profit_forecast / 1000, marker='s', label='Прогноз', linestyle='--', linewidth=2,
                    color='red')
axes[0, 1].set_title('Динамика прибыли с прогнозом\n(тыс. руб.)')
axes[0, 1].legend()
axes[0, 1].tick_params(axis='x', rotation=45)

qty_forecast, qty_model = forecast_timeseries(monthly_data['Количество'])
axes[1, 0].plot(monthly_data.index, monthly_data['Количество'], marker='o', label='История', linewidth=2, color='green')
if qty_forecast is not None:
    axes[1, 0].plot(future_dates, qty_forecast, marker='s', label='Прогноз', linestyle='--', linewidth=2, color='red')
axes[1, 0].set_title('Динамика количества продаж с прогнозом')
axes[1, 0].legend()
axes[1, 0].tick_params(axis='x', rotation=45)

rent_forecast, rent_model = forecast_timeseries(monthly_data['Рентабельность'])
axes[1, 1].plot(monthly_data.index, monthly_data['Рентабельность'], marker='o', label='История', linewidth=2,
                color='purple')
if rent_forecast is not None:
    axes[1, 1].plot(future_dates, rent_forecast, marker='s', label='Прогноз', linestyle='--', linewidth=2, color='red')
axes[1, 1].set_title('Динамика рентабельности с прогнозом\n(%)')
axes[1, 1].legend()
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print("\n=== ПРОГНОЗ ПРОДАЖ ПО ТОВАРАМ ===")


def forecast_product_sales(product_name, periods=3):
    product_data = data[data['товар'] == product_name]
    monthly = product_data.groupby('Год-мес')['Продажи'].sum().reset_index()

    if len(monthly) < 2:
        return None, None, None

    monthly = monthly.sort_values('Год-мес')
    monthly['date'] = pd.to_datetime(monthly['Год-мес'].astype(str), format='%Y%m')

    x = np.array(range(len(monthly))).reshape(-1, 1)
    y = monthly['Продажи'].values

    model = LinearRegression()
    model.fit(x, y)

    future_x = np.array(range(len(monthly), len(monthly) + periods)).reshape(-1, 1)
    model_forecast = model.predict(future_x)
    
    future_dates = [monthly['date'].iloc[-1] + pd.DateOffset(months=i + 1) for i in range(periods)]

    return monthly, model_forecast, future_dates


top_6 = product_stats.head(6).index

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.ravel()

for i, product in enumerate(top_6):
    historical, model_forecast, future_dates = forecast_product_sales(product)

    if historical is not None:
        axes[i].plot(historical['date'], historical['Продажи'] / 1000,
                     marker='o', label='История', linewidth=2, color='blue')
        axes[i].plot(future_dates, model_forecast / 1000, marker='s',
                     label='Прогноз', linestyle='--', linewidth=2, color='red')

        growth = ((model_forecast[0] - historical['Продажи'].iloc[-1]) / historical['Продажи'].iloc[-1]) * 100
        axes[i].set_title(f'{product[:15]}...\nПрогноз роста: {growth:+.1f}%', fontsize=10)
        axes[i].set_ylabel('Тыс. руб.')
        axes[i].legend(fontsize=8)
        axes[i].tick_params(axis='x', rotation=45)
    else:
        axes[i].text(0.5, 0.5, 'Недостаточно данных', ha='center', va='center')
        axes[i].set_title(f'{product[:15]}...')

plt.tight_layout()
plt.show()

print("\n=== ПРОГНОЗ ПО ТОЧКАМ РЕАЛИЗАЦИИ ===")


def forecast_point_sales(point_name, periods=3):
    point_data = data[data['точка'] == point_name]
    monthly = point_data.groupby('Год-мес')['Продажи'].sum().reset_index()

    if len(monthly) < 2:
        return None, None, None

    monthly = monthly.sort_values('Год-мес')
    monthly['date'] = pd.to_datetime(monthly['Год-мес'].astype(str), format='%Y%m')

    x = np.array(range(len(monthly))).reshape(-1, 1)
    y = monthly['Продажи'].values

    model = LinearRegression()
    model.fit(x, y)

    future_x = np.array(range(len(monthly), len(monthly) + periods)).reshape(-1, 1)
    model_forecast = model.predict(future_x)

    future_dates = [monthly['date'].iloc[-1] + pd.DateOffset(months=i + 1) for i in range(periods)]

    return monthly, model_forecast, future_dates


points = data['точка'].unique()

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.ravel()

for i, point in enumerate(points[:4]):  # Показываем первые 4 точки
    historical, model_forecast, future_dates = forecast_point_sales(point)

    if historical is not None:
        axes[i].plot(historical['date'], historical['Продажи'] / 1000,
                     marker='o', label='История', linewidth=2, color='green')
        axes[i].plot(future_dates, model_forecast / 1000, marker='s',
                     label='Прогноз', linestyle='--', linewidth=2, color='red')

        growth = ((model_forecast[0] - historical['Продажи'].iloc[-1]) / historical['Продажи'].iloc[-1]) * 100
        axes[i].set_title(f'Точка: {point}\nПрогноз роста: {growth:+.1f}%')
        axes[i].set_ylabel('Тыс. руб.')
        axes[i].legend()
        axes[i].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print("\n=== СВОДНЫЕ ДАННЫЕ ===")

top_10 = product_stats.head(10).index
pivot_table = data[data['товар'].isin(top_10)].pivot_table(
    values='Продажи', index='товар', columns='точка', aggfunc='sum', fill_value=0
)

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table / 1000, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Продажи топ-10 товаров по точкам (тыс. руб.)')
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("ИТОГОВЫЙ ОТЧЕТ С ПРОГНОЗАМИ")
print("=" * 50)

print(f"\n ОСНОВНЫЕ ПОКАЗАТЕЛИ:")
print(f" Товарооборот: {total_sales:,.0f} руб.")
print(f" Прибыль: {data['Прибыль'].sum():,.0f} руб.")
print(f" Средняя рентабельность: {data['Рентабельность'].mean():.1f}%")

if sales_forecast is not None:
    print(f"\n ПРОГНОЗ НА СЛЕДУЮЩИЕ {forecast_periods} МЕСЯЦА:")
    print(f" Средний прогноз товарооборота: {sales_forecast.mean():,.0f} руб./мес")
    print(f" Средний прогноз прибыли: {profit_forecast.mean():,.0f} руб./мес")
    print(
        f" Прогноз роста товарооборота: {((sales_forecast.mean() - monthly_data['Продажи'].mean()) / monthly_data['Продажи'].mean() * 100):+.1f}%")

print(f"\n ЛИДЕРЫ:")
print(f" Лучшая точка: {point_stats.index[0]}")
print(f" Топ-товар: {product_stats.index[0]}")
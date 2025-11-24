import csv
import sys
import time
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

cache = {}


def get_page(url):
    if url in cache:
        print(f"Using cached page: {url}")
        return cache[url]

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка HTTP ошибок
        cache[url] = response
        time.sleep(10/200)  # Пауза чтобы не перегружать сервер
        return response
    except requests.RequestException as e:
        print(f"Error loading page {url}: {e}")
        return None


def capital_from_data(dataset):
    try:
        capital_arr = []
        capital = ""
        table_data = dataset.find_all('tr')
        checker = False
        for data in table_data:
            if "Capital" in data.text:
                checker = True
            if checker:
                capital_arr = data
                break

        for data in capital_arr:
            if "Capital" not in data.text:
                capital = data.text


        i = 0
        for ch in capital:
            if ch.isdecimal():
                break
            i += 1
        capital = capital[:i]
        if "(" in capital:
            capital = capital[:capital.index("(")]
        elif "{" in capital:
            capital = capital[:capital.index("{")]
        elif "[" in capital:
            capital = capital[:capital.index("[")]
        return capital[:i].strip()
    except Exception as e:
        print(f"Error extracting capital: {e}")
        return "N/A"


def area_from_data(dataset):
    try:
        area_arr = []
        area = ""
        table_data = dataset.find_all('tr', class_="mergedrow")
        for data in table_data:
            if "km2" in data.text:
                area_arr.append(data)

        if not area_arr:
            return "N/A"

        area_arr_split = area_arr[0].text.split()
        i = 0
        for item in area_arr_split:
            if "km2" in item:
                break
            i += 1

        area = area_arr_split[i - 1]
        area = area.replace(",", "")

        for ch in area:
            if ch.isalpha():
                area = area.replace(ch,"")

        ch_id = 0
        for ch in area:
            if not ch.isdecimal():
                ch_id = area.index(ch)
                break
        if ch_id == 0:
            ch_id = len(area)
        clean_area = area[:ch_id]

        for ch in area:
            if not ch.isdecimal():
                clean_area = clean_area.replace(ch,"")

        return clean_area if clean_area else "N/A"
    except Exception as e:
        print(f"Error extracting area: {e}")
        return "N/A"


def population_from_data(dataset):
    million_check = False
    population = dataset.find('th', string='Population').find_next('td').get_text().strip()
    if "million" in population:
        million_check = True
    population =    population.replace(",", "")
    i = 0
    for ch in population:
        if not ch.isdigit():
            break
        i+=1

    population = population[:i]
    if million_check:
        population = population + "000000"
    return population


def process_country(country_name):
    try:
        encoded_country = quote(country_name)
        country_URL = f"https://en.wikipedia.org/wiki/{encoded_country}"

        print(f"Processing: {country_name}")

        page = get_page(country_URL)
        if page is None:
            return None

        soup = BeautifulSoup(page.content, 'html.parser')

        capital = capital_from_data(soup)
        area = area_from_data(soup)
        population = population_from_data(soup)

        return {
            'country': country_name,
            'city': capital,
            'area': area,
            'population': population
        }
    except Exception as e:
        print(f"Error processing country {country_name}: {e}")
        return None


# ДОБАВИЛ: функция для чтения стран из файла
def read_countries(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            countries = [line.strip() for line in f if line.strip()]
        return countries
    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found")
        return []


# ДОБАВИЛ: функция для записи в CSV
def write_to_csv(data, output_file):
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['country', 'city', 'area', 'population'])
            writer.writeheader()
            for row in data:
                if row:  # Пропускаем неудачные запросы
                    writer.writerow(row)
        print(f"Data successfully written to {output_file}")
    except Exception as e:
        print(f"Error writing to CSV: {e}")


# ДОБАВИЛ: главная функция
def main():
    # Обработка аргументов командной строки
    input_file = "countries.txt"
    output_file = "countries_data.csv"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

    # Чтение списка стран
    countries = read_countries(input_file)
    if not countries:
        return

    # Обработка каждой страны
    results = []
    for country in countries:
        result = process_country(country)
        if result:
            results.append(result)
            print(
                f"Completed: {country} - Capital: {result['city']}, Area: {result['area']}, Population: {result['population']}")
        else:
            print(f"Failed to process: {country}")

    # Запись результатов
    write_to_csv(results, output_file)


# ИСПРАВИЛ: убрал старый код и добавил вызов main
if __name__ == "__main__":
    main()
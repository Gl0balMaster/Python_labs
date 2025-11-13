from faker import Faker
from faker.providers import BaseProvider
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


fake = Faker('ru_RU')

class DateProvider(BaseProvider):
    def date_obuch(self):
        return fake.random_int(min=2021, max=2025)

    def studiying_form(self):
        return  "Очная" if fake.random_int(0,1)  else "Заочная"

    def CT(self):
        return fake.random_int(min=0, max=100)

    def speciality(self):
        specialties = [
            "Прикладная механика",
            "Механика и математическое моделирование",
            "Физика (научно-производственная деятельность)",
            "Физика (научно-педагогическая деятельность)",
            "Физика (физика наноматериалов и нанотехнологий)",
            "Компьютерная физика",
            "Ядерная физика и технологии",
            "Физика (медицинская физика)",
            "Аэрокосмические радиоэлектронные и информационные системы",
            "Радиофизика",
            "Электронные системы и технологии",
            "Информационные системы и технологии (в обеспечении безопасности)",
            "Квантовая радиофизика и наноэлектроника",
            "Лазерная физика и спектроскопия",
            "Физическая электроника",
            "Компьютерная безопасность",
            "Прикладная математика",
            "Информатика",
            "Актуарная математика",
            "Экономическая кибернетика"
        ]
        return self.random_element(specialties)


fake.add_provider(DateProvider)

def generate_user():
    name = fake.name()
    date = fake.date_obuch()
    form = fake.studiying_form()
    ct_lang = fake.CT()
    ct_first_prof = fake.CT()
    ct_second_prof = fake.CT()
    avg_grade = fake.random_int(0, 100)/10
    total_pts = ct_lang+ct_second_prof+ct_first_prof + avg_grade
    specialty = fake.speciality()
    address = fake.address()
    phone = fake.phone_number()
    user = {
        "name": name,
        "date_obuch": date,
        "form" : form,
        "ct_lang": ct_lang,
        "ct_first_prof": ct_first_prof,
        "ct_second_prof": ct_second_prof,
        "avg_grade" :  avg_grade,
        "total_pts" : total_pts,
        "specialty" : specialty,
        "address" : address,
        "phone" : phone }
    return user



users= [generate_user() for _ in range(1000)]
df = pd.json_normalize(users, sep='_')

penguins = sns.load_dataset('penguins')


fig, axes = plt.subplots(2, 3, figsize = (15,12) )
sns.barplot(data=df, x='date_obuch', y='ct_lang',ax=axes[0,0])
axes[0,0].set_title('ct_lang')
axes[0,0].set_xlabel('year')
axes[0,0].set_ylabel('grade')

sns.barplot(data=df, x='date_obuch', y='ct_first_prof', estimator='mean',ax=axes[0,1])
axes[0,1].set_title('ct_first_prof')
axes[0,1].set_xlabel('year')
axes[0,1].set_ylabel('grade')

sns.barplot(data=df, x='date_obuch', y='ct_second_prof', estimator='mean',ax=axes[1,0])
axes[1,0].set_title('ct_second_prof')
axes[1,0].set_xlabel('year')
axes[1,0].set_ylabel('grade')

sns.barplot(data=df, x='date_obuch', y='avg_grade', estimator='mean',ax=axes[1,1])
axes[1,1].set_title('avg_grade')
axes[1,1].set_xlabel('year')
axes[1,1].set_ylabel('grade')

heatmap_data_form = df.groupby(['date_obuch', 'form']).size().unstack(fill_value=0)

sns.heatmap(heatmap_data_form, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5,ax=axes[1,2])
axes[1,2].set_title('Количество студентов по специальностям и годам обучения')
axes[1,2].set_xlabel('Специальность')
axes[1,2].set_ylabel('Год обучения')
plt.tight_layout()
plt.show()




heatmap_data_spec = df.groupby(['date_obuch', 'specialty']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data_spec, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5)
plt.title('Количество студентов по специальностям и годам обучения')
plt.xlabel('Специальность')
plt.ylabel('Год обучения')
plt.tight_layout()
plt.show()


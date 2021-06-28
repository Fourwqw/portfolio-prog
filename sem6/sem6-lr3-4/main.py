# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 1

""""
1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части.


"""
from typing import Tuple

import numpy as np
import pandas as pd

N_DIGITS_FLOAT = 2


def get_sex_distrib(data: 'pd.DataFrame') -> 'np.ndarray':
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """
    return data["Sex"].value_counts().values


def get_port_distrib(data: 'pd.DataFrame') -> 'np.ndarray':
    """
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """
    return data["Embarked"].value_counts().values


def get_surv_percent(data: 'pd.DataFrame') -> Tuple[int, float]:
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """
    nd, ns = data["Survived"].value_counts()[0:2]  # Survived -> 0 || 1

    total = nd + ns
    return nd, round(nd / total, N_DIGITS_FLOAT)


def get_class_distrib(data: 'pd.DataFrame') -> Tuple[float, ...]:
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?
    """
    nbs = data["Pclass"].value_counts()  # Classes: {1, 2, 3}
    classes = [nbs[i] for i in range(1, 4)]  # Classes are not ordered

    total = sum(classes)

    return tuple(map(lambda c: round(c / total, N_DIGITS_FLOAT), classes))


def find_corr_sibsp_parch(data: 'pd.DataFrame') -> float:
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    return round(data["SibSp"].corr(data["Parch"]), N_DIGITS_FLOAT)


def find_corr_age_survival(data: 'pd.DataFrame') -> float:
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - возрастом и параметром survival;
    """
    return round(data["Age"].corr(data["Survived"]), N_DIGITS_FLOAT)


def find_corr_sex_survival(data: 'pd.DataFrame') -> float:
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - полом человека и параметром survival;
    """
    return round(
        data["Sex"].astype("category").cat.codes.corr(data["Survived"]),
        N_DIGITS_FLOAT
    )


def find_corr_class_survival(data: 'pd.DataFrame') -> float:
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    - классом, в котором пассажир ехал, и параметром survival.
    """
    return round(data["Pclass"].corr(data["Survived"]), N_DIGITS_FLOAT)


def find_pass_mean_median(data: 'pd.DataFrame') -> Tuple[float, float]:
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """
    mean = round(data["Age"].mean(), N_DIGITS_FLOAT)
    median = round(data["Age"].median(), N_DIGITS_FLOAT)

    return mean, median


def find_ticket_mean_median(data: 'pd.DataFrame') -> Tuple[float, float]:
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """
    mean = round(data["Fare"].mean(), N_DIGITS_FLOAT)
    median = round(data["Fare"].median(), N_DIGITS_FLOAT)

    return mean, median


def find_popular_name(data: 'pd.DataFrame') -> str:
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    is_male = data["Sex"] == "male"
    return data[is_male].mode().at[0, "Name"]


def find_popular_adult_names(data: 'pd.DataFrame') -> Tuple[str, str]:
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    is_15_yo = data["Age"] > 15
    is_male = data["Sex"] == "male"
    is_female = data["Sex"] == "female"

    male_name = data[is_15_yo & is_male].mode().at[0, "Name"]
    female_name = data[is_15_yo & is_female].mode().at[0, "Name"]

    return male_name, female_name


def join_str(*args, delimiter=" ") -> str:
    return delimiter.join(map(lambda a: str(a), args))


def main():
    data = pd.read_csv("train.csv", index_col="PassengerId")

    # 1
    print(join_str(*get_sex_distrib(data)))
    # 2
    print(join_str(*get_port_distrib(data)))
    # 3
    print(get_surv_percent(data))
    # 4
    print(get_class_distrib(data))
    # 5
    print(find_corr_sibsp_parch(data))
    # 6
    print(find_corr_age_survival(data))
    # 2) 
    print(find_corr_sex_survival(data))
    # 3) 
    print(find_corr_class_survival(data))
    # 7
    print(find_pass_mean_median(data))
    # 8
    print(find_ticket_mean_median(data))
    # 9
    print(find_popular_name(data))
    # 10
    print(find_popular_adult_names(data))


# Executable
if __name__ == "__main__":
    main()
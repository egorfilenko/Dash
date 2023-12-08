import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

# Загрузка данных из файла CSV
data = pd.read_csv('https://raw.githubusercontent.com/egorfilenko/Dash/main/Dash.csv')

# Создание экземпляра приложения Dash
app = dash.Dash(__name__)

# Определение макета приложения
app.layout = html.Div(children=[
    html.H1(children='Интерактивный дашборд'),

    # Выпадающий список (Dropdown) для фильтрации по типу услуги
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': value, 'value': value} for value in data['Тип услуги'].unique()
        ],
        value=data['Тип услуги'].unique()[0]
    ),

    # График временного ряда
    dcc.Graph(id='time-series-chart'),

    # Круговая диаграмма
    dcc.Graph(id='pie-chart'),

    # Таблица с данными
    html.Table(id='data-table'),

    # График рассеяния
    dcc.Graph(id='scatter-plot'),

])



# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
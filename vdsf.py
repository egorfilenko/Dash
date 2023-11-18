import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

# Создание экземпляра приложения Dash
app = dash.Dash(__name__)



# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)


def csv_file():
    df = pd.read_csv('C:\\Users\\savio\\PROJECTS\\PYTHON\\DASHBOARDPERFORMACETEST\\app\\files\\resultados.csv')
    return df


def gerar_dashboard():
    app.layout = html.Div(children=[
        html.H1(children='Sistema para controle de homologação em tempo real'),

        html.Div(children='''
        Dashboard para monitoramento de estatísticas de api de biblioteca em tempo real.
    '''),

        dcc.Graph(
            id='responseCode-graph',
            figure=px.pie(csv_file(), values='responseCode', names='label')
        ),
        dcc.Graph(
            id='success-graph',
            figure=px.line(csv_file(), x='timeStamp', y='success', title='Success')
        ),
        dcc.Graph(
            id='failureMessage-graph',
            figure=px.line(csv_file(), x='timeStamp', y='failureMessage', title='Failure Message')
        )
    ])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gerar_dashboard()
    app.run_server(port=3000, debug=True, host='localhost')

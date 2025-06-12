import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import requests
from dash import dash_table


# 1. Conectar à API Django
def fetch_data():
    try:
        response = requests.get('http://localhost:8000/api/morador/?format=json')
        moradores = response.json()
        # Garante que todos os campos existem, mesmo que estejam ausentes em alguns registros
        for m in moradores:
            m.setdefault('abastecimento_agua', 'Não informado')
        return pd.DataFrame(moradores)
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return pd.DataFrame()
    
# 2. Inicializar o app Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 3. Layout do Dashboard com abas e tabela
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Painel do Censo 2022 - IBGE", className="text-center my-4"))),
    dcc.Tabs([
        dcc.Tab(label='Gráficos', children=[
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='sexo-filter',
                        options=[
                            {'label': 'Masculino', 'value': 'M'},
                            {'label': 'Feminino', 'value': 'F'},
                            {'label': 'Outro', 'value': 'O'}
                        ],
                        multi=True,
                        placeholder="Selecione o sexo..."
                    )
                ], width=6),
                dbc.Col([
                    dcc.Slider(
                        id='age-slider',
                        min=0,
                        max=100,
                        step=5,
                        value=100,
                        marks={i: str(i) for i in range(0, 101, 10)}
                    )
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='pirâmide-etária'), width=6),
                dbc.Col(dcc.Graph(id='sexo-bar'), width=6)
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id='infraestrutura'), width=12)
            ]),
        ]),
        dcc.Tab(label='Dados Brutos', children=[
            dbc.Row([
                dbc.Col(dash_table.DataTable(
                    id='moradores-table',
                    columns=[
                        {"name": "ID", "id": "id"},
                        {"name": "Nome", "id": "nome"},
                        {"name": "Idade", "id": "idade"},
                        {"name": "Sexo", "id": "sexo"},
                        {"name": "Ensino Superior Completo", "id": "concluiu_superior"},
                    ],
                    page_size=10,
                    style_table={'overflowX': 'auto'},
                    style_cell={'textAlign': 'left'},
                ), width=12)
            ])
        ])
    ]),
    dcc.Interval(id='update-interval', interval=60*1000)
], fluid=True)

# 4. Callbacks (Interatividade)
@app.callback(
    [Output('pirâmide-etária', 'figure'),
     Output('sexo-bar', 'figure'),
     Output('infraestrutura', 'figure'),
     Output('moradores-table', 'data')],
    [Input('sexo-filter', 'value'),
     Input('age-slider', 'value'),
     Input('update-interval', 'n_intervals')]
)
def update_charts(selected_sexos, max_age, _):
    df = fetch_data()
    if df.empty:
        return px.bar(), px.bar(), px.pie(), []

    # Filtros
    if selected_sexos:
        df = df[df['sexo'].isin(selected_sexos)]
    df = df[df['idade'] <= max_age]

    # Gráfico 1: Pirâmide Etária
    bins = [0, 5, 12, 18, 30, 60, 100]
    labels = ['0-4', '5-11', '12-17', '18-29', '30-59', '60+']
    if not df.empty:
        df['faixa_etaria'] = pd.cut(df['idade'], bins=bins, labels=labels)
        pyramid = px.bar(
            df.groupby(['faixa_etaria', 'sexo'], observed=False).size().unstack(fill_value=0),
            barmode='group',
            title="Pirâmide Etária"
        )
    else:
        pyramid = px.bar(title="Pirâmide Etária")

    # Gráfico 2: Moradores por Sexo
    if not df.empty:
        sexo_bar = px.bar(
            df.groupby('sexo').size().reset_index(name='count'),
            x='sexo',
            y='count',
            title="Moradores por Sexo"
        )
    else:
        sexo_bar = px.bar(title="Moradores por Sexo")

    # Gráfico 3: Infraestrutura (Conclusão de Ensino Superior)
    if not df.empty:
        # Traduz valores booleanos para texto para melhor visualização
        df['concluiu_superior_str'] = df['concluiu_superior'].map({True: 'Sim', False: 'Não'})
        infra = px.pie(
            df.groupby('concluiu_superior_str').size().reset_index(name='count'),
            names='concluiu_superior_str',
            values='count',
            title="Moradores que Concluíram o Ensino Superior"
        )
    else:
        infra = px.pie(title="Moradores que Concluíram o Ensino Superior")

    # Dados para tabela
    if not df.empty:
        table_data = df[['id', 'nome', 'idade', 'sexo', 'concluiu_superior']].to_dict('records')
    else:
        table_data = []
    return pyramid, sexo_bar, infra, table_data

# 5. Executar o app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
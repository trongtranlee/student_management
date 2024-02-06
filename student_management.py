from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

app = Dash()
server = app.server

df = pd.read_csv('D:\\PythonFramework\\LeaningDash\\student_management\\fake_data.csv', delimiter=',')

# thêm cột điểm gpa
df['student_gpa'] = (df['student_mathScore'] + df['student_chemScore'] + df['student_phyScore'] + df[
    'student_engScore'] + df['student_litScore']) / 4 * 0.4

# Thiết lập hiển thị để hiển thị toàn bộ nội dung của DataFrame
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

app.layout = html.Div(
    [
        html.H1("Quản lý sinh viên ", style={'textAlign': 'center', 'color': 'green'}),
        html.Div(
            [
                html.Div('Nhập mã sinh viên', ),
                dcc.Input(
                    id="STUDENT_ID",
                    type="text",
                    value='',
                    placeholder='Nhập mã sinh viên...',
                    debounce=True
                )
            ], style={'textAlign': 'center', 'color': 'green'}
        ),
        html.Div(
            [
                html.Span(
                    [
                        html.Div(id='STUDENT_NAME', style={'color': 'green'})
                    ]
                ),
                html.Span(''),
                html.Span(
                    [
                        html.Div(id='STUDENT_GENDER', style={'color': 'green'}),
                    ]
                ),
                html.Span(
                    [
                        html.Div(id='STUDENT_AGE', style={'color': 'green'})
                    ]
                ),
                html.Span(''),
                html.Span(
                    [
                        html.Div(id='STUDENT_PHONENUMBER', style={'color': 'green'}),
                    ]
                ),
                html.Span(
                    [
                        html.Div(id='STUDENT_EMAIL', style={'color': 'green'})
                    ]
                ),
                html.Span(''),
                html.Span(
                    [
                        html.Div(id='STUDENT_CITY', style={'color': 'green'}),
                    ]
                ),
                html.Span(
                    [
                        html.Div(id='STUDENT_GPA', style={'color': 'green'})
                    ]
                ),
            ]
        ),
        dcc.Graph(
            id="GPA_RADARCAHRT"
        )
    ]
)


# Call back
@app.callback(
    Output('STUDENT_NAME', 'children'),
    Output('STUDENT_GENDER', 'children'),
    Output('STUDENT_AGE', 'children'),
    Output('STUDENT_PHONENUMBER', 'children'),
    Output('STUDENT_EMAIL', 'children'),
    Output('STUDENT_CITY', 'children'),
    Output('STUDENT_GPA', 'children'),
    Input('STUDENT_ID', 'value')
)
def update_infor(STUDENT_ID):
    f_df = df.astype(str)

    if len(STUDENT_ID) > 0:
        f_df = f_df[f_df.student_id == STUDENT_ID]
        # Kiểm tra xem có dữ liệu trả về không
        if not f_df.empty:
            # Trả về các trường dữ liệu
            STUDENT_NAME = f_df.iloc[0]['student_name']
            STUDENT_GENDER = f_df.iloc[0]['student_gender']
            STUDENT_AGE = f_df.iloc[0]['student_age']
            STUDENT_PHONENUMBER = f_df.iloc[0]['student_phoneNumber']
            STUDENT_EMAIL = f_df.iloc[0]['student_email']
            STUDENT_CITY = f_df.iloc[0]['student_city']
            STUDENT_GPA = f_df.iloc[0]['student_gpa']
            return f'Tên sinh viên: {STUDENT_NAME}', \
                   f'Giới tính: {STUDENT_GENDER}', \
                   f'Tuổi: {STUDENT_AGE}', \
                   f'Số điện thoại: {STUDENT_PHONENUMBER}', \
                   f'Email: {STUDENT_EMAIL}', \
                   f'Quê quán: {STUDENT_CITY}', \
                   f'Điểm GPA: {STUDENT_GPA}'
        else:
            # Trả về thông báo nếu không tìm thấy sinh viên
            return 'Không tìm thấy sinh viên', '', '', '', '', '', ''
    else:
        # Trả về None nếu không tìm thấy sinh viên
        return None, None, None, None, None, None, None


@app.callback(
    Output('GPA_RADARCAHRT', 'figure'),
    Input('STUDENT_ID', 'value')
)
def update_radar_chart(STUDENT_ID):
    f_df = df.astype(str)
    if len(STUDENT_ID) > 0:
        f_df = f_df[f_df.student_id == STUDENT_ID]
        categories = ['Math Score', 'Chem Score', 'Phy Score', 'Eng Score', 'Lit Score']
        values = [f_df.iloc[0]['student_mathScore'].astype(int),
                  f_df.iloc[0]['student_chemScore'].astype(int),
                  f_df.iloc[0]['student_phyScore'].astype(int),
                  f_df.iloc[0]['student_engScore'].astype(int),
                  f_df.iloc[0]['student_litScore'].astype(int)]
        return {
            'data': [
                go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself',
                    name='Biểu đồ radar'
                )
            ],
            'layout': go.Layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 5]  # Phạm vi của trục radial
                    )
                ),
                title=f'Biểu đồ Radar của {df.iloc[0]["student_name"]}'
            )
        }


app.run_server(port=8051, debug=True)

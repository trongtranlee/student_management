import numpy as np
import matplotlib.pyplot as plt
from dash import dcc
import student_management

# Dữ liệu
categories = ['Math Score', 'Chem Score', 'Phy Score', 'Eng Score', 'Lit Score']
values = [student_management.df.iloc[0]['student_mathScore'],
          student_management.df.iloc[0]['student_chemScore'],
          student_management.df['student_phyScore'],
          student_management.df['student_engScore'],
          student_management.df['student_litScore']]

radar_chart = dcc.Graph(
    id='radar-chart',
    figure={
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
            title=f'Biểu đồ Radar của {default_student}'
        )
    }
)
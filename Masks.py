#!/usr/bin/env python
# coding: utf-8

# In[133]:


import pandas as  pd


# In[134]:


df= pd.read_csv('https://raw.githubusercontent.com/Carolsila/gownss/main/gowns.csv')
df


# In[135]:


import plotly.express as px


# In[136]:


fig= px.bar(df, x='Gowns(1000  units)', y='CO2e(KGs)',color='Gowns(1000  units)',
           color_discrete_map={'Single Use':'#770737','Reusable':'#FFBF00','Revolution-Zero':'#2A537A','Revolution-Zero Forecasts':'#367D77'},
            
            title='CO2e(equivalents) of 1000 gowns.')
fig.show()


# In[137]:


m=pd.read_csv('https://raw.githubusercontent.com/Carolsila/gownss/main/Mask.csv')
m


# In[ ]:





# In[138]:


fig= px.bar(m, x='Masks', y='CO2e',color='Masks',
           color_discrete_map={'Single Use- Air flight-China':'#722F37','Single Use-Sea freight-China':'#DE3163','Single Use-Road-Turkey':'#A42A04','Revolution-ZERO-Road-Portugal':'#2A537A'})
            
            #title='CO2e(equivalents) of Masks')
fig.show()


# In[62]:


#pip install jupyter-dash


# In[149]:


#from jupyter_dash import JupyterDash
import plotly.express as px
import dash
from dash import dcc
from dash import  html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.express as px
def drawFigure1():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(df, x='Gowns(1000  units)', y='CO2e(KGs)',color='Gowns(1000  units)',
                                  
                                  
                           color_discrete_map={'Single-use':'#770737','Reusable':'#FFBF00','Revolution-ZERO':'#2A537A','Revolution-ZERO Forecasts':'#367D77'},
                           labels={'Gowns(1000  units)':'Gowns (1000 units)'})
            
                           #title='Disposable/Reusable/Revolution-ZERO Gowns.')
                    

                    .update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(8, 73, 123, 2)',
                        #paper_bgcolor= 'rgba(0,0,0,0)',
                        font=dict(
                            family='Helvetica',
                            size=18                      
                        )
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])


def drawFigure2():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                   figure= px.bar(m, x='Masks',y='CO2e',color='Masks',
                                  
                                  labels={'CO2e':'CO2e (KGs)','Masks':'Masks (1000 units)'},
                                  
                                  color_discrete_map={'Single-use (China, Air)':'#770737',
                                                              'Single-use (China, Sea)':'#FFBF00',
                                                              'Single-use (Turkey, Road)':'#2A537A',
                                                               'Revolution-ZERO (Road, Portugal)':'#367D77'
 
                                                              }
                                  
                                 #title=' Single Use vs Revolution-ZERO '
             )
                    
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(8, 73, 123, 2)',
                        #paper_bgcolor= 'rgba(9, 74, 123, 1)',
                        font=dict(
                            family='Helvetica',
                            size=18                   
                        )
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])



#draw text1
def drawText1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Environmental Impact (CO2e) of 1000 Sterile Gowns"),
                ], style={'font_family':'Helvetica','textAlign': 'left','font':12})
            ])
        ),
    ])


# Drawtext2
def drawText2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Environmental Impact (CO2e) of 1000 Masks"),
                ], style={'font_family':'Helvetica','textAlign': 'left','font':12})
            ])
        ),
    ])


app = dash.Dash(__name__,
                  
    external_stylesheets=[dbc.themes.BOOTSTRAP],
                  meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                 )
server=app.server
                 
colors={'background':'#000000','text':'#000000'}

app.layout = html.Div(style={'backgroundColor':colors['background']},children=[
    
    html.Div([ 
        html.H1("Environmental Impact of Medical Devices")
        
    ],style={'font_family':'Helvetica','textAlign':'center','color':'#FFFFFF'}),
    

 dbc.Card(         
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText1()
                ],xs=12,md=6, lg=6),
                dbc.Col([
                    drawText2()
                ],xs=12,md=6, lg=6),
                
                ],align='center'),            
            html.Br(),
            
            dbc.Row([
                dbc.Col([
                    drawFigure1() 
                ], xs=12,md=6, lg=6),
                
                dbc.Col([
                    drawFigure2() 
                ], xs=12,md=12, lg=6),
                
              ], align='center'), 
            html.Br(),
            dbc.Row([               
                 dbc.Col([
                    '' 
                ], xs=12,md=6, lg=6),
                 dbc.Col([ 

                   html.Img(src = app.get_asset_url('logo.jpg'),style={'height':'100%','width':'100%'}),
                    
                ],style={'textAlign':'bottom'},xs=12,md=12, lg=6),
                 ],align='center'),
            
            
                ]), color = 'dark'
    )
])
            

    
    
    
#app.run_server( debug = True)

if __name__ == '__main__':
    app.run_server(debug=True)



# In[ ]:





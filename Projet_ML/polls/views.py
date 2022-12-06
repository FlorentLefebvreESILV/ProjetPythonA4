from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

 
#les import dont on a besoin
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import ast
import plotly.express as px
import mpld3

def index(request):
    context = {}
    return render(request, 'template_intro.html', context)
    #return HttpResponse(template.render(context, request))
    
def index0(request):
    #charger données, etc
    df2 = pd.read_csv('transcoding_mesurment.tsv', sep='\t', header=0)
    df1 = pd.read_csv('youtube_videos.tsv', sep='\t', header=0)
    df2_numerique = df2.drop(labels = ['id','codec','o_codec'], axis=1, inplace=False)
    df2 = df2.dropna(axis=0)
    df1 = df1.dropna(axis=0)
    df2.drop(labels = ['b_size'], axis=1, inplace=True)
    Rapport_hauteur_io = df2['height']/df2['o_height']

    
    fig1 = plt.figure()
    p=sns.set(rc = {'figure.figsize':(5,8)})
    p=sns.histplot(data=df1['codec'])
 
    fig2 = plt.figure()    
    p=sns.set(rc = {'figure.figsize':(2,9)})
    p=sns.barplot(data= df2[['i','p','b']])
    
    fig3 = plt.figure()
    p=sns.set(rc = {'figure.figsize':(15,15)})
    p=plt.pie(df2[['i','p','b']].sum().tolist(),labels=df2[['i','p','b']].columns.tolist(),autopct=lambda x:'{:1.0f}%'.format(x))
    
    fig6 = plt.figure()
    p=sns.displot(df2[df2['utime']<60]['utime'], kde=True, bins=12)
    
    fig7 = plt.figure()
    p=sns.set(rc = {'figure.figsize':(10,1)})
    p=sns.displot(Rapport_hauteur_io)
    
    
    plt_html1 = mpld3.fig_to_html(fig1)
    plt_html2 = mpld3.fig_to_html(fig2)
    plt_html3 = mpld3.fig_to_html(fig3)
    plt_html6 = mpld3.fig_to_html(fig6)
    plt_html7 = mpld3.fig_to_html(fig7)

    context={
        'plt_html1':plt_html1,
        'plt_html2':plt_html2,
        'plt_html3':plt_html3,
        'plt_html6':plt_html6,
        'plt_html7':plt_html7,
        
    }
    return render(request, 'template_visu.html', context)
    
def index1(request):
    #charger données, etc
    df = pd.read_csv('transcoding_mesurment.tsv', sep='\t', header=0)
    df2 = pd.read_csv('youtube_videos.tsv', sep='\t', header=0)
    #template = loader.get_template('template0.html')
    df_duration = df.duration.unique()
    context={
        'dfduration':df_duration
    }
    return render(request, 'template_model.html', context)
    #return HttpResponse(template.render(context, request))

#import + faire une fonction pour chaque model
def KnnOnIris():
    df = pd.read_csv('transcoding_mesurment.tsv', sep='\t', header=0)
    df3 = px.data.iris() # iris is a pandas DataFrame
    fig = px.scatter(df3, x="sepal_width", y="sepal_length")
    plot_html = fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html

def KMeansOnIris():
    df = pd.read_csv('transcoding_mesurment.tsv', sep='\t', header=0)
    df3 = px.data.iris() # iris is a pandas DataFrame
    fig = px.scatter(df3, x="sepal_length", y="sepal_width")
    plot_html = fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html

def index2(request):
    #charger données, etc
    template = loader.get_template('template_model.html')
    #reprendre les variables rentrées par l'utilisateurs
    if(request.GET['model']=="RandomForestRegressor"):
        plot_html=KnnOnIris()
    if(request.GET['model']=="KNeighborsRegressor"):
        plot_html=KMeansOnIris()
    context={
        'plot_html':plot_html,
   }
    return HttpResponse(template.render(context, request))

def index3(request):
    context={}
    return render(request, 'template_pred.html', context)

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

def analyzeSocialMediaData(csv_url):
    csv = pd.read_csv(csv_url)

    csv = csv.dropna()
    encoder = LabelEncoder()
    csv['tipo'] = encoder.fit_transform(csv['tipo'])

    # ESTOU PEGANDO REAÇÕES BOAS
    features = csv[['tipo', 'num_reacoes', 'num_comentarios', 'num_compartilhamentos', 'num_likes', 'num_loves', 'num_wows', 'num_hahas', 'num_angrys']].values

    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(features)

    csv['grupo'] = kmeans.labels_

    group_labels = {0: 'Não receberá divulgação', 1: 'Irá receber divulgação baixa', 2: 'Irá receber divulgação alta'}
    csv['grupo'] = csv['grupo'].map(group_labels)

    group_counts = csv['grupo'].value_counts()
    min_count = group_counts.min()

    result = {
        'Não receberá divulgação': csv[csv['grupo'] == 'Não receberá divulgação'].head(min_count),
        'Irá receber divulgação baixa': csv[csv['grupo'] == 'Irá receber divulgação baixa'].head(min_count),
        'Irá receber divulgação alta': csv[csv['grupo'] == 'Irá receber divulgação alta'].head(min_count)
    }

    for group_name, group_data in result.items():
        print(f"\n{group_name}:")
        print(group_data)

analyzeSocialMediaData('https://pastebin.com/raw/JTKAcY0W')


# FICOU RUIM DE VER NO TERMINAL, FIZ UM OUTRO CÓDIGO QUE MOSTRA TODO O DADO SEM QUE APARECESSE OS ..., MAS FICOU PIOR AINDA DE ENTENDER KKKKKKKKK
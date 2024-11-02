import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

def analyzeSocialMediaData(csv_url):
    csv = pd.read_csv(csv_url)

    csv = csv.dropna()

    encoder = LabelEncoder()
    csv['tipo'] = encoder.fit_transform(csv['tipo'])

    features = csv[['tipo', 'num_reacoes', 'num_comentarios', 'num_compartilhamentos', 'num_likes']].values

    kmeans = KMeans(n_clusters=3, random_state=42)  
    kmeans.fit(features)

    csv['grupo'] = kmeans.labels_

    for grupo in range(3):
        group_data = csv[csv['grupo'] == grupo]
        if grupo == 0:
            print("\nGrupo 'Não receberá divulgação':")
        elif grupo == 1:
            print("\nGrupo 'Irá receber divulgação baixa':")
        else:
            print("\nGrupo 'Irá receber divulgação alta':")

        print(group_data[['tipo', 'num_reacoes', 'num_comentarios', 'num_compartilhamentos', 'num_likes']])

analyzeSocialMediaData('https://pastebin.com/raw/JTKAcY0W')

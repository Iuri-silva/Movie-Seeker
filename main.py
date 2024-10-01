import pandas as pd

#Importando o dataset movies
df = pd.read_csv(r"C:\Users\iuri.santos\Documents\PROGRAMAÇÃO\Python\PROJETO\BRANCH_TEST\movies.csv")

unique_genres = set()

#Função que separa todos os gêneros contidos no dataset movies
def filter_genres():
    df['genres'] = df['genres'].fillna('')  #Removendo campos vazios
    for genres in df['genres']:
        for genre in genres.split(', '):  #Separando os gêneros nos intervalos de virgula
            if genre:
                unique_genres.add(genre)

#Função que mostra um menu para o usuário informar os gêneros preferidos
def menu():
    filter_genres()
    genre_list = sorted(unique_genres)

    print("Gêneros:")
    for index, genre in enumerate(sorted(unique_genres), start=1): #Listando os gêneros
        print(f"{index}. {genre}")
    
    selected_genres = input("\n \nINFORME QUAIS SEUS GÊNEROS FAVORITOS\n(ex: 1, 5, 8, 12)\n--> ")

    #Separando os valores informados
    selected_genres = [i.strip() for i in selected_genres.split(',')] 

    #Convertendo os valores para inteiro
    selected_genres = [int(i) for i in selected_genres if i.isdigit()] 
    
    #Cria uma lista e adiciona os gêneros de acordo com os números informados
    selected_genre_names = [genre_list[i-1] for i in selected_genres if 1 <= i <= len(genre_list)]

    return selected_genre_names
    
def recomendation():
    ...


print(menu())

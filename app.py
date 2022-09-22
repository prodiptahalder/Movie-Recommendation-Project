from flask import Flask, jsonify, request
import pickle
import pandas as pd
import requests
import bz2

app = Flask(__name__)

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

ifile = bz2.BZ2File('BinaryData', 'rb')
similarity = pickle.load(ifile)
ifile.close()

def fetch_details(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8d9a8cdb3e15410333f7168f539bdfeb'.format(movie_id))
    data = response.json()
    return data

def recommend(movie):
    res = []
    movie_index = movies[movies['title'] == movie]
    if movie_index.size==0:
        return []
    movie_index = movie_index.index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_details(movie_id)
        res.append({'name': movies.iloc[i[0]].title,
                    # 'details': details,
                    'poster': "https://image.tmdb.org/t/p/w500/"+details['poster_path']})

    return res


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})

@app.route('/recommend/<string:movie>', methods=['GET'])
def disp(movie):
    recommended_movie = recommend(movie)
    if len(recommended_movie)==0:
        return jsonify({'err': 'Please enter a valid movie name'})
    return jsonify({'data': recommended_movie})

if __name__ == '__main__':
    app.run(debug=True)
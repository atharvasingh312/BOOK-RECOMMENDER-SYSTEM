

from flask import Flask, render_template,request
import pickle
import numpy as np


popular_df=pickle.load(open('popularity.pkl', 'rb'))
pt=pickle.load(open('pt.pkl', 'rb'))
similarity_score=pickle.load(open('similarity_score.pkl', 'rb'))
books=pickle.load(open('books.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    #need to pass popular_df of top 100
    return render_template('index.html',
                           bookname=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           vote=list(popular_df['num_rating'].values),
                           rating=list(popular_df['avg_rating'].values),
                           image=list(popular_df['Image-URL-M'].values)
                           )
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods = ['post'])
def recommend():
    user_input = request.form.get('user_input')
    # fetching index
    data = []
    index = np.where(pt.index == user_input)
    if(len(index[0])==0):
        return render_template('not_found.html')
    ind=index[0][0]
    distance=list(enumerate(similarity_score[ind]))
    # reverse sorting
    distance=sorted(distance,key=lambda x:x[1],reverse=True)
    suggestion=distance[0:100]
    for i in suggestion:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    #print(data)
    return render_template('recommend.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)

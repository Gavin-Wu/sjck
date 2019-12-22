#coding:utf-8
from flask import Flask, request,jsonify
from flask_cors import cross_origin
from py2neo import Graph,Node,Relationship,NodeMatcher
import datetime

app = Flask(__name__)
graph = Graph('bolt://localhost:7687',username='neo4j',password='1')

# director = "Migdalia Etheridge"
# st = "Match (d:Director)-[]-(m:Movie) where d.name=\""+director+"\" return m"
# test = graph.run(st);
# print(test)

@app.route('/getMovieByDirector', methods=['POST'])
@cross_origin()
def getMovieByDirector():
    a = datetime.datetime.now()
    director = request.form['director']
    st = "Match (d:Director)-[]-(m:Movie) where d.name=\""+director+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now()-a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getMovieByActor', methods=['POST'])
@cross_origin()
def getMovieByActor():
    a = datetime.datetime.now()
    actor = request.form['actor']
    st = "Match (a:Actor)-[]-(m:Movie) where a.name=\""+actor+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getMovieByGenre', methods=['POST'])
@cross_origin()
def getMovieByGenre():
    a = datetime.datetime.now()
    genre = request.form['genre']
    st = "Match (g:Genre)-[]-(m:Movie) where g.name=\""+genre+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getMovieByLanguage', methods=['POST'])
@cross_origin()
def getMovieByLanguage():
    a = datetime.datetime.now()
    language = request.form['language']
    st = "Match (l:Language)-[]-(m:Movie) where l.name=\""+language+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getMovieByStudio', methods=['POST'])
@cross_origin()
def getMovieByStudio():
    a = datetime.datetime.now()
    studio = request.form['studio']
    st = "Match (s:Studio)-[]-(m:Movie) where s.name=\""+studio+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})




@app.route('/getMovieByVersion', methods=['POST'])
@cross_origin()
def getMovieVersion():
    a = datetime.datetime.now()
    movie = request.form['movie']
    st = "Match (m:Movie) where m.name =~\""+movie+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getMovieByTime', methods=['POST'])
@cross_origin()
def getMovieByTime():
    a = datetime.datetime.now()
    begin = request.form['begin']
    end = request.form['end']
    st = "match (m:Movie) where m.time>= \""+begin+"\" and m.time<= \""+end+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})




@app.route('/getActorByGenre', methods=['POST'])
@cross_origin()
def getActorByGenre():
    a = datetime.datetime.now()
    actor = request.form['actor']
    genre = request.form['genre']
    st = "match (g:Genre)-[]-(m:Movie)-[]-(a:Actor) where g.name=\""+genre+"\" and a.name=\""+actor+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getDirectorByGenre', methods=['POST'])
@cross_origin()
def getDirectorByGenre():
    a = datetime.datetime.now()
    director = request.form['director']
    genre = request.form['genre']
    st = "match (g:Genre)-[]-(m:Movie)-[]-(d:Director) where g.name=\""+genre+"\" and d.name=\""+director+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getDirectorByActor', methods=['POST'])
@cross_origin()
def getDirectorByActor():
    a = datetime.datetime.now()
    director = request.form['director']
    actor = request.form['actor']
    st = "match (d:Director)-[]-(m:Movie)-[]-(a:Actor) where d.name=\""+director+"\" and a.name=\""+actor+"\" return m as movie"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})


@app.route('/getActorByGenrePro', methods=['POST'])
@cross_origin()
def getActorByGenrePro():
    a = datetime.datetime.now()
    actor = request.form['actor']
    genre = request.form['genre']
    st = "match (g:Genre)-[r]-(a:Actor) where g.name=\""+genre+"\" and a.name=\""+actor+"\" return count(r) as count"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getDirectorByGenrePro', methods=['POST'])
@cross_origin()
def getDirectorByGenrePro():
    a = datetime.datetime.now()
    director = request.form['director']
    genre = request.form['genre']
    st = "match (g:Genre)-[r]-(d:Director) where g.name=\""+genre+"\" and d.name=\""+director+"\" return count(r) as count"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})

@app.route('/getDirectorByActorPro', methods=['POST'])
@cross_origin()
def getDirectorByActorPro():
    a = datetime.datetime.now()
    director = request.form['director']
    actor = request.form['actor']
    st = "match (d:Director)-[r]-(a:Actor) where d.name=\""+director+"\" and a.name=\""+actor+"\" return count(r) as count"
    test = graph.run(st)
    b = datetime.datetime.now() - a
    print(b)
    return jsonify({'list':test.data(),'time':b.microseconds})


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()

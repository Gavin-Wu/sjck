import csv
import datetime

file = open("./total.csv", "r", newline='',encoding='gb18030', errors = 'ignore')
source = csv.reader(file,delimiter=',', quotechar='"')

total_write = 0

# 临时变量
productId = ''
title = ''
imdb_rate = ''
time = ''
actors = []
directors = []
languages = []
studios = []
genres = []

# csv文件
productCsv = open('movieCsv.csv','w',newline='',encoding='gb18030')
actorCsv = open('actorCsv.csv','w',newline='',encoding='gb18030')
directorCsv = open('directorCsv.csv','w',newline='',encoding='gb18030')
languageCsv = open('languageCsv.csv','w',newline='',encoding='gb18030')
studioCsv = open('studioCsv.csv','w',newline='',encoding='gb18030')
genreCsv = open('genreCsv.csv','w',newline='',encoding='gb18030')


actCsv = open('actCsv.csv','w',newline='',encoding='gb18030')
directCsv = open('directCsv.csv','w',newline='',encoding='gb18030')
speakCsv = open('speakCsv.csv','w',newline='',encoding='gb18030')
makeCsv = open('makeCsv.csv','w',newline='',encoding='gb18030')
styleCsv = open('styleCsv.csv','w',newline='',encoding='gb18030')
directorGenreCsv = open('directorGenreCsv.csv','w',newline='',encoding='gb18030')
actorGenreCsv = open('actorGenreCsv.csv','w',newline='',encoding='gb18030')
directorActorCsv = open('directorActorCsv.csv','w',newline='',encoding='gb18030')



product = csv.writer(productCsv)
actor = csv.writer(actorCsv)
act = csv.writer(actCsv)
director = csv.writer(directorCsv)
direct = csv.writer(directCsv)
language = csv.writer(languageCsv)
speak = csv.writer(speakCsv)
studio = csv.writer(studioCsv)
make = csv.writer(makeCsv)
genre = csv.writer(genreCsv)
style = csv.writer(styleCsv)
director_genre = csv.writer(directorGenreCsv)
actor_genre = csv.writer(actorGenreCsv)
director_actor = csv.writer(directorActorCsv)


# 用来存储之前行的数据
actorMap = {}
directorMap = {}
genreMap = {}
languageMap = {}
studioMap = {}

actor_count = 0
director_count = 0
genre_count = 0
language_count = 0
studio_count = 0


# 开始查询
start = datetime.datetime.now()
print("start")

for line in source:
    # 处理行
    productId = line[0]
    title = ' '.join(line[1].split(','))
    title = ''.join(title.split('\n'))
    title = ' '.join(title.split('\\'))
    if line[2] != 'None':
        imdb_rate = line[2]
    if line[3] != 'None':
        time = line[3]

    actors = line[4].split(',')
    if len(actors) == 1:
        actors = line[4].split('\n')
    else:
        for i in range(len(actors)):
            actors[i] = ''.join(actors[i].split('\n'))
    for i in range(len(actors)):
        actors[i] = actors[i].strip()
    
    directors = line[5].split(',')
    if len(directors) == 1:
        directors = line[5].split('\n')
    else:
        for i in range(len(directors)):
            directors[i] = ''.join(directors[i].split('\n'))
    for i in range(len(directors)):
        directors[i] = directors[i].strip()
    
    languages = line[6].split(',')
    studios = line[7].split(',')
    genres = line[8].split(',')
    

    # 写数据

    product.writerow([productId,title,imdb_rate,time])

    for a in actors:
        if a not in actorMap:
            actor_count += 1
            actorMap[a] = actor_count
        act.writerow([actorMap[a],productId])
        
    for d in directors:
        if d not in directorMap:
            director_count += 1
            directorMap[d] = director_count
        direct.writerow([directorMap[d],productId])
    
    for l in languages:
        if l not in languageMap:
            language_count += 1
            languageMap[l] = language_count
        speak.writerow([productId,languageMap[l]])

    for s in studios:
        if s not in studioMap:
            studio_count += 1
            studioMap[s] = studio_count
        make.writerow([studioMap[s],productId])
    
    for g in genres:
        if g not in genreMap:
            genre_count += 1
            genreMap[g] = genre_count
        style.writerow([productId,genreMap[g]])

    for x in directors:
        for y in genres:
            director_genre.writerow([directorMap[x],genreMap[y]])

    for x in actors:
        for y in genres:
            actor_genre.writerow([actorMap[x],genreMap[y]])

    for x in directors:
        for y in actors:
            director_actor.writerow([directorMap[x],actorMap[y]])
    
    total_write += 1
    if total_write % 10000 == 0:
        print(total_write)

# 写map数据
for a in actorMap.keys():
    actor.writerow([actorMap[a],a])

for d in directorMap.keys():
    director.writerow([directorMap[d],d])

for l in languageMap.keys():
    language.writerow([languageMap[l],l])

for s in studioMap.keys():
    studio.writerow([studioMap[s],s])

for g in genreMap.keys():
    genre.writerow([genreMap[g],g])

# 结束
end = datetime.datetime.now()
print(end-start)

file.close()
productCsv.close()
actorCsv.close()
directorCsv.close()
languageCsv.close()
studioCsv.close()
genreCsv.close()

actCsv.close()
directCsv.close()
speakCsv.close()
makeCsv.close()
styleCsv.close()
directorGenreCsv.close()
actorGenreCsv.close()
directorActorCsv.close()




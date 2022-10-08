"# Movie-Recommendation-Project" 

Recommender.ipynb file contains jupyter notebook code where I trained the model for this content Based Recommendation.
BinaryData file contains compressed data which is actually 5000 dimensional vector for all movies in the movies_dict.pkl file.
mypython is the virtual env directory.
app.py is the main file which is to be executed.

The project is a RESTful API service in which we have one route:
BASE address + "/recommend/:movie name" [GET]
  which will return 5 recommendation for viewers of movie name movie.
  
In order to run the project, execute :~ python app.py ~:  command.

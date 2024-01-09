# Book Recommender System


Welcome to the Book Recommender System project! This end-to-end machine learning application is designed to recommend books to users based on their similarity using collaborative filtering methods. The project utilizes various technologies and frameworks, such as Python, Numpy, Pandas, Scikit-learn, Flask, HTML, CSS, and Bootstrap.

## Project Overview

- **Collaborative Filtering Method:** The project is based on collaborative filtering approach, which analyzes user behavior and preferences to recommend books that similar users have enjoyed.

- **Web Application:** The project includes a user-friendly web application built using the Flask framework. The frontend is developed with a combination of HTML, CSS, and Bootstrap, providing visually appealing interface for users to interact with the recommendation system.

## Demo

https://github.com/atharvasingh312/Book-Recommender-System/assets/111992277/ed4c23dd-57e6-46e9-ada4-0ec06866e492
<center><bold>video of working model of the book recommender</bold></center>

## Deployment

To run this project on your system follow the following steps:

1. Clone the repository to your local machine.
```bash
   git clone  https://github.com/atharvasingh312/Book-Recommender-System.git
```

2. The pickle files contain data that are already preprocessed in this project which are [Books.pkl](https://github.com/atharvasingh312/Book-Recommender-System/blob/main/books.pkl), [popularity.pkl](https://github.com/atharvasingh312/Book-Recommender-System/blob/main/popularity.pkl), [pt.pkl](https://github.com/atharvasingh312/Book-Recommender-System/blob/main/pt.pkl), [similarity_score.pkl](https://github.com/atharvasingh312/Book-Recommender-System/blob/main/similarity_score.pkl). If you are intrested to know how the data has been processed and what machine learning algorithm have been used kindly refer the jupyter notebook [recommender.ipynb](https://github.com/atharvasingh312/Book-Recommender-System/blob/main/recommender.ipynb).

3. Install the required dependencies  
```bash
   pip install -r requirements.txt
```

4. Run the Flask application
```bash
   run app.py
```


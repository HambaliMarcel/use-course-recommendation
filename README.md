# USE Course Recommendation: Efficient Course Matching
CourseIdentifier is a straightforward model designed to match courses based on a Power Summary. This summary integrates the course description, outline, objectives, and difficulty level. Utilizing text embeddings from the Universal Sentence Encoder, this tool aims to provide accurate course identification easily.

## Features
Text Embeddings: Uses Universal Sentence Encoder to embed text data.
Course Matching: Identifies and recommends courses based on the input text.
Visualization: Displays the embedding space using PCA.

## Requirements
- Python 3.x
- Jupyter Notebook or Google Colab
- TensorFlow
- TensorFlow Hub
- Matplotlib
- Pandas
- Scikit-learn

## How to Run

Clone the repository:
```
git clone https://github.com/HambaliMarcel/use-course-recommendation.git
cd use-course-recommendation
```
Install the required libraries:
```
pip install -r requirements.txt
```

Open RecommendationCourseUSE.ipynb in Jupyter Notebook:
```
jupyter notebook use-course-recommendation.ipynb
```
Follow the instructions within the notebook to run each cell.

Upload the dataset DatasetCourse.csv to your Colab environment.
```
Create your dataset. We just need 3 features:
Name | Power Summary | Platform

```
Or you can scrape any courses with this scraper:

https://github.com/HambaliMarcel/Course-Scraping-2024
```
git clone https://github.com/HambaliMarcel/Course-Scraping-2024.git
```

Sample Output:
<img width="1018" alt="Screenshot 2024-05-24 at 22 09 44" src="https://github.com/HambaliMarcel/use-course-recommendation/assets/67316752/026304b8-9f34-4e2f-9a6c-6c27ad136177">

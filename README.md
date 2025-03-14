# 📚 ShowMyBooks - Book Recommendation System 📚

![Python](https://img.shields.io/badge/python-%23386C6C.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

## 🚀 Overview

Welcome to **ShowMyBooks**, your ultimate destination for discovering the perfect book! This project presents a Book Recommendation System, namely ShowMyBooks, which leverages machine learning to deliver personalized book suggestions to users based on their unique preferences and reading habits. This is measured using a dataset where users(readers) have rated various books, and the ratings as well as the votes are used to recommend books accordingly.

## 🌟 Key Features

- **📚 Personalized Book Recommendations**: Utilizes collaborative and content-based filtering to provide precise book suggestions tailored to your tastes.
- **📈 Comprehensive Dataset**: Leverages a large Kaggle dataset with detailed book information and user ratings.
- **🎨 Interactive Interface**: Originally built with Flask, HTML, and CSS for a robust web interface, now enhanced with Streamlit for a sleek, dynamic experience.
- **🌐 Scalable Deployment**: Initially deployed on Render for Flask and now on Streamlit Sharing for improved scalability and performance.

## 🛠️ Technical Details

### 🔄 Data Ingestion

- Imported and processed datasets from Kaggle, including book information and user ratings.
- Data preprocessing and feature engineering handled with Pandas, NumPy, and Scikit-learn.

### 🤖 Recommendation Engine

- **Collaborative Filtering**: Finds patterns in user ratings to suggest books based on what similar users have enjoyed.
- **Content-Based Filtering**: Analyzes book features (e.g., genre, author) to recommend books similar to those you’ve liked.

### 🖥️ Full-Stack Development

- **Initial Development**:
  - **Flask**: Used for server-side logic.
  - **HTML/CSS**: Designed the user interface for an engaging experience.
- **Current Development**:
  - **Streamlit**: Updated for a more interactive and user-friendly web application.
  - **Python**: Continued use for backend logic, data processing, and machine learning.

### 🚀 Deployment

- **Render**: Originally deployed the Flask version on Render, ensuring high availability and scalability.
- **Streamlit Sharing**: Currently deployed a new version on Streamlit Sharing, providing a seamless and scalable user experience.

## 🏆 Showcase

This project highlights my expertise in:

- **Machine Learning**: Crafting recommendation systems with advanced algorithms.
- **Data Analysis**: Handling and analyzing large datasets for actionable insights.
- **Full-Stack Development**: Transitioning from Flask, HTML, and CSS to a modern Streamlit application.
- **Deployment**: Successfully deploying and scaling live applications for real-world use.

## 📁 Repository Contents

- `app.py`: Original Flask application code.
- `artifacts`: List of the pickle files that imported after analysis
- `data/`: Datasets and data processing scripts.
- `templates/`: HTML templates (for Flask version).
- `requirements.txt`: Python dependencies.

## 🏁 Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AashishPathak1/ShowMyBooks.git
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   ```bash
   flask run
   ```

## 🔍 Explore the Application

Dive right into discovering your next favorite book!

Click the link below to access the live ShowMyBooks app:
[**ShowMyBooks**](https://showmybooks.onrender.com/)

### 📂 Check Out My Current Version of Project

Currently new updated version in ui with some features
Visit [**ShowMyBooks2.O**](https://aashishpathak1-showmybooks2-o-innewui.streamlit.app/)

Enjoy personalized book recommendations and more in both versions!

## 💬 Feedback & Contributions

Got ideas or feedback? Feel free to [open an issue](https://github.com/AashishPathak1/ShowMyBooks/issues) or [submit a pull request](https://github.com/AashishPathak1/ShowMyBooks/compare). Happy reading!

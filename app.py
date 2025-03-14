from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

popular_df = pickle.load(open("artifacts/popular.pkl", "rb"))
book_pivot_table = pickle.load(open("artifacts/book_pivot_table.pkl", "rb"))
books = pickle.load(open("artifacts/books.pkl", "rb"))
similarity_scores = pickle.load(open("artifacts/similarity_scores.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        book_name=list(popular_df["Book-Title"].values),
        author=list(popular_df["Book-Author"].values),
        image=list(popular_df["Image-URL-M"].values),
        votes=list(popular_df["num_ratings"].values),
        rating=list(popular_df["avg_ratings"].values),
    )


@app.route("/recommend")
def recommend_ui():
    return render_template("recommend.html")


@app.route("/recommend_books", methods=["POST"])
def recommend_books():
    user_input = request.form.get("user_input")

    # Check if the user_input exists in the index
    if user_input not in book_pivot_table.index:
        return jsonify({"error": "Book not found in index."}), 400

    # Index fetch
    index = np.where(book_pivot_table.index == user_input)[0]

    # Check if index is empty
    if len(index) == 0:
        return (
            jsonify(
                {
                    "error": "Pivot table operation failed due to embook_pivot_tabley data."
                }
            ),
            500,
        )

    index = index[0]

    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
    )[1:5]

    data = []
    for i in similar_items:
        if i[0] < len(book_pivot_table.index):
            item = []
            temp_df = books[books["Book-Title"] == book_pivot_table.index[i[0]]]
            item.extend(
                list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values)
            )
            item.extend(
                list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values)
            )
            item.extend(
                list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values)
            )
        data.append(item)
    print(data)
    return render_template("recommend.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)

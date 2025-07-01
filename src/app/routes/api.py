from flask import Blueprint, request, make_response, jsonify
from src.components.recommendation_engine import RecommendationEngine

api = Blueprint('api', __name__)
recommendation_engine : RecommendationEngine = RecommendationEngine()

@api.route('/')
def top_books():
    Books = recommendation_engine.top_books()
    response = make_response({"Top-Books" : Books}, 200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@api.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    Book = request.get_json()
    Book_Title = Book['name']
    recommended_books = recommendation_engine.recommendation(book_name=Book_Title)
    response = make_response({"Recommended-Books" : recommended_books}, 200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response
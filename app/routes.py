from http.client import responses

from flask import Blueprint, jsonify, request

from .services import get_all_recipes, get_recipe_by_id, create_recipe, delete_recipe, update_recipe

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return {"message": "RecipeShare API is running"}


@main.route("/api/recipes", methods=["GET"])
def list_recipes():
    """Return a JSON array of all recipes."""
    recipes = get_all_recipes()
    return jsonify(recipes)


@main.route("/api/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id: int):
    """Return a single recipe as JSON."""
    recipe = get_recipe_by_id(recipe_id)
    return jsonify(recipe), 200


@main.route("/api/recipes", methods=["POST"])
def add_recipe():
    """Create a new recipe.

    Steps:
        1. Parse the JSON body from the request.
        2. Validate that required fields are present:
           title, description, instructions, prep_time, user_id.
           If any are missing, return a 400 error with a message listing them.
        3. Call create_recipe() from services and return the result with status 201.
    """
    # TODO: Implement this route
    response = request.get_json()
    fields = ["title", "description", "instructions", "prep_time", "user_id"]
    issues = ""
    for field in fields:
        if field not in response:
            issues += f"{field} missing,"
    if issues != "":
        return {"Error:" : 400, "Issues": f"{issues}"}
    else:
        return {"Result" : create_recipe(response), "Status" : 201}, 201




@main.route("/api/recipes/<int:recipe_id>", methods=["PUT"])
def modify_recipe(recipe_id: int):
    """Update an existing recipe.

    Steps:
        1. Parse the JSON body from the request.
        2. Call update_recipe() from services with the recipe_id and data.
        3. Return the updated recipe as JSON.
    """
    # TODO: Implement this route
    response = request.get_json()
    new_recipe = update_recipe(recipe_id, response)
    return new_recipe, 200


@main.route("/api/recipes/<int:recipe_id>", methods=["DELETE"])
def remove_recipe(recipe_id: int):
    """Delete a recipe.

    Steps:
        1. Call delete_recipe() from services with the recipe_id.
        2. Return a 204 No Content response.
    """
    # TODO: Implement this route
    delete_recipe(recipe_id)
    return "No content response", 204

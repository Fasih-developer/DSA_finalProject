
from flask import Flask, render_template, request, redirect, url_for
from database import get_connection

app = Flask(__name__)


# =====================================
# READ + DASHBOARD
# =====================================

@app.route("/")
def home():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM food_donations ORDER BY id DESC")
    donations = cursor.fetchall()

    cursor.close()
    connection.close()

    # Dashboard statistics
    total_count = len(donations)

    available_count = sum(
        1 for d in donations
        if d["status"].lower() == "available"
    )

    completed_count = sum(
        1 for d in donations
        if d["status"].lower() == "completed"
    )

    return render_template(
        "donations.html",
        donations=donations,
        total_count=total_count,
        available_count=available_count,
        completed_count=completed_count
    )


# =====================================
# CREATE
# =====================================

@app.route("/add-donation", methods=["POST"])
def add_donation():

    food_name = request.form["food_name"]
    quantity = request.form["quantity"]
    unit = request.form["unit"]
    location = request.form["location"]
    expiry_time = request.form["expiry_time"].replace("T", " ")
    description = request.form["description"]

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO food_donations
        (food_name, quantity, unit, location, expiry_time, description)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        food_name,
        quantity,
        unit,
        location,
        expiry_time,
        description
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("home"))


# =====================================
# UPDATE
# =====================================

@app.route("/update-donation/<int:donation_id>", methods=["POST"])
def update_donation(donation_id):

    food_name = request.form["food_name"]
    quantity = request.form["quantity"]
    unit = request.form["unit"]
    location = request.form["location"]
    expiry_time = request.form["expiry_time"].replace("T", " ")
    description = request.form["description"]

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE food_donations
        SET food_name = %s,
            quantity = %s,
            unit = %s,
            location = %s,
            expiry_time = %s,
            description = %s
        WHERE id = %s
    """

    values = (
        food_name,
        quantity,
        unit,
        location,
        expiry_time,
        description,
        donation_id
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("home"))


# =====================================
# DELETE
# =====================================

@app.route("/delete-donation/<int:donation_id>", methods=["POST"])
def delete_donation(donation_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM food_donations WHERE id = %s"

    cursor.execute(query, (donation_id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("home"))


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

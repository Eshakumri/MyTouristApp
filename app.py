from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    city = request.args.get("city", "").lower()

    # Map city names to routes
    if city == "delhi":
        return redirect(url_for("delhi"))
    elif city == "mumbai":
        return redirect(url_for("mumbai"))
    elif city == "kolkata":
        return redirect(url_for("kolkata"))
    elif city == "chennai":
        return redirect(url_for("chennai"))
    elif city == "hyderabad":
        return redirect(url_for("hyderabad"))
    elif city == "bangalore":
        return redirect(url_for("bangalore"))
    elif city == "jaipur":
        return redirect(url_for("jaipur"))
    elif city == "agra":
        return redirect(url_for("agra"))
    elif city == "varanasi":
        return redirect(url_for("varanasi"))
    elif city == "goa":
        return redirect(url_for("goa"))
    else:
        return "City not found! Try Delhi, Mumbai, Kolkata, Chennai, Hyderabad, Bangalore, Jaipur, Agra, Varanasi, or Goa."

@app.route("/delhi")
def delhi():
    return render_template("delhi.html")

@app.route("/mumbai")
def mumbai():
    return render_template("mumbai.html")

@app.route("/kolkata")
def kolkata():
    return render_template("kolkata.html")

@app.route("/chennai")
def chennai():
    return render_template("chennai.html")

@app.route("/hyderabad")
def hyderabad():
    return render_template("hyderabad.html")

@app.route("/bangalore")
def bangalore():
    return render_template("bangalore.html")

@app.route("/jaipur")
def jaipur():
    return render_template("jaipur.html")

@app.route("/agra")
def agra():
    return render_template("agra.html")

@app.route("/varanasi")
def varanasi():
    return render_template("varanasi.html")

@app.route("/goa")
def goa():
    return render_template("goa.html")

if __name__ == "__main__":
    app.run(debug=True)
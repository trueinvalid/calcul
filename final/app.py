from flask import Flask, request,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculator", methods = ['GET', 'POST'])
def calculator():
    expression = ""
    result = ""
    if request.method == 'POST':
        expression = request.form.get("expression","")
        button = request.form.get("button","")
        if button == "AC":
            expression=""
        elif button == "=":
            try:
                result = str(eval(expression))
                expression = result
            except:
                result = "Ошибка"
                expression = ""
        else:
            expression = expression + button
            result = expression

    return render_template("calculator.html",result=result,expression=expression)


if __name__ == '__main__':
    app.run(debug = True)



    #  ______     __  __     __  __     __         ______
    # /\  ___\   /\ \/ /    /\ \_\ \   /\ \       /\  ___\
    # \ \___  \  \ \  _"-.  \ \____ \  \ \ \____  \ \  __\
     # \/\_____\  \ \_\ \_\  \/\_____\  \ \_____\  \ \_____\
      # \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_____/



from flask import Flask, request, render_template, flash, redirect, url_for, session
from objective import ObjectiveTest
from subjective import SubjectiveTest

app = Flask(__name__)

app.secret_key = 'aica2'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_generate', methods=["POST"])
def test_generate():
    if request.method == "POST":
        inputText = request.form["itext"]
        testType = request.form["test_type"]
        noOfQues = request.form["noq"]
        if testType == "objective":
            objective_generator = ObjectiveTest(inputText, noOfQues)
            question_list = objective_generator.generate_test()
            return render_template('generatedtestdata.html', cresults=question_list)
        elif testType == "subjective":
            subjective_generator = SubjectiveTest(inputText, noOfQues)
            question_list = subjective_generator.generate_test()
            return render_template('generatedtestdata.html', cresults=question_list)
        else:
            flash('Error Occurred!')
            return redirect(url_for('/'))

if __name__ == "__main__":
    app.run()


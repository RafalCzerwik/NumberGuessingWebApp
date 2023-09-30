from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main endpoint that handles the game logic for the reversed guessing game.
    The computer tries to guess the number thought by the user based on the feedback
    provided by the user through form buttons.
    """

    min_val = 1
    max_val = 1000
    message = ""

    if request.method == 'POST':
        min_val = int(request.form['min_val'])
        max_val = int(request.form['max_val'])
        user_response = request.form['action']

        try:
            # Adjust the guessed range based on user feedback
            if user_response == "Too small":
                min_val = (min_val + max_val) // 2 + 1
            elif user_response == "Too big":
                max_val = (min_val + max_val) // 2 - 1
            else:
                return "You win!"

            # If min_val exceeds max_val, then user has likely given inconsistent feedback
            if min_val > max_val:
                return "You cheated!"
        except Exception as e:
            # Catch any unexpected error and print the error message
            return f"An error occurred: {e}"

    # Computer makes a guess in the middle of the current range
    guess = (min_val + max_val) // 2

    return render_template('index.html', guess=guess, min_val=min_val, max_val=max_val)


if __name__ == "__main__":
    while True:
        try:
            app.run(debug=True)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Restarting the app...")
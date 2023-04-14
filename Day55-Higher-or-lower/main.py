from flask import Flask
from random import randint


app = Flask(__name__)


@app.route('/')
def home_page():
    return "<div style = 'text-align:center'>" \
           "<h1 >Guess a number between 0 and 9</h1>" \
           "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' height=200px width=200px>" \
           "</div>"

random_number = randint(1,10)


@app.route('/<number>')
def guess_page(number):
    global random_number
    number = int(number)
    if number > random_number:
        return "<div styles = 'text-align:center'>" \
               "<h1>TOO HIGH, AIM LOWER</h1>" \
               "<img src = 'https://media3.giphy.com/media/VRvFAP4CXxUQw/giphy.gif?cid=ecf05e47kb832nrm1cx48ngjy6apyg24e1gu2nwtvzuykepr&rid=giphy.gif&ct=g'>" \
               "</div>"

    elif number < random_number:
        return "<div styles = 'text-align:center'>" \
               "<h1>TOO low, AIM higher</h1>" \
               "<img src = 'https://media1.giphy.com/media/gmAGepsUn5kVq/giphy.gif?cid=ecf05e47jhb30aht1bn8tpfe8rty9ud6c9ly117ur57l5a56&rid=giphy.gif&ct=g'>" \
               "</div>"

    else:
        return "<div styles = 'text-align:center'>" \
               "<h1>BINGO</h1>" \
               "<img src = 'https://media4.giphy.com/media/1hMk0bfsSrG32Nhd5K/giphy.gif?cid=ecf05e470zb5zqoa1fb77ac8kq9b2nd31lfpvyr9ykip4is1&rid=giphy.gif&ct=g'" \
               "</div>"



if __name__ == '__main__':
    app.run(debug= True)








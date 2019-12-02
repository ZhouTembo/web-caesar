from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post" action='/encrypt'>
        <label for="rotate-by">
            Rotate by:
            <input type="text"  value="0" id="rotate" name="rot"/>
            
        </label>
        <br>
        <textarea name="message" style="width:400px; height:200px;" >{0}
        </textarea>
        <br>
        <input type="submit" value="submit query"/>
    </form>
    </body>
</html>


"""
@app.route("/encrypt",methods=['POST'])
def encrypt():
    text=request.form['message']
    rot=request.form['rot']
    rot=int(rot)
    return form.format(rotate_string(text,rot))


@app.route("/",methods=['GET'])
def index():
    return form.format('')

app.run()
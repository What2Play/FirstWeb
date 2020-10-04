from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app=Flask(__name__)

app.config['SECRET_KEY'] = '8c9b785df2b5b2be5f5c6844cc3a37ad'

posts = [
    {
        'author': 'Peter Lyl',
        'title': 'Peters anbefaling',
        'content': 'First post',
        'date_posted': 'September 30, 2020'
    },
    {
        'author': 'Tim Xow',
        'title': 'Tims anbefaling',
        'content': 'Second post',
        'date_posted': 'September 30, 2020'
    }
]

games = [
    {
        'company': 'Riot Games',
        'title': 'League of Legends',
        'content': 'MOBA',
        'date_posted': 'September 30, 2020',
        'image': 'https://cdn.vox-cdn.com/thumbor/KS55nlwSXYKYYTcpavCnj7Pxw9E=/0x0:1000x563/1600x900/cdn.vox-cdn.com/uploads/chorus_image/image/1520305/league_of_legends_negativity.0.jpg'
    },
    {
        'company': 'Blizzard Entertainment',
        'title': 'World of Warcraft',
        'content': 'MMORPG',
        'date_posted': 'September 30, 2020',
        'image': 'https://images.blz-contentstack.com/v3/assets/blt3452e3b114fab0cd/blt03dc217d0e54036a/5dbb29281b83a568128c8c9d/Shadowlands_Logo.png'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/top_games')
def top_games():
    return render_template ("top_games.html", title='Top Games', posts=games)

@app.route('/about')
def about():
    return render_template("about.html", title='About')

@app.route('/jul_stinker')
def jul_stinker():
    return render_template("jul_stinker.html", title='Jul stinker')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been loggin in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css') }}">
    {% if title %}
        <title>BLOG - {{ title }}</title>
    {% else %}
        <title>BLOG</title>
    {% endif %}
</head>
<body>
    <header class="site-header">
      <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
          <a class="navbar-brand mr-4" href="/">Weplay.GG</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav mr-auto">
              <a class="nav-item nav-link" href="{{ url_for('home') }}">Home</a>
              <a class="nav-item nav-link" href="{{ url_for('top_games') }}">Top Games</a>
              <a class="nav-item nav-link" href="{{ url_for('about') }}">Recommendations</a>
              <a class="nav-item nav-link" href="{{ url_for('jul_stinker') }}">Jul stinker</a>
              <a class="nav-item nav-link" href="{{ url_for('about') }}">Contact Us</a>
            </div>
            <!-- Navbar Right Side -->
            <div class="navbar-nav">
              <a class="nav-item nav-link" href="{{ url_for('login') }}">Login</a>
              <a class="nav-item nav-link" href="{{ url_for('register') }}">Register</a>
            </div>
          </div>
        </div>
      </nav>
    </header>
    <main role="main" class="container">
      <div class="row">
        <div class="col-md-8">
          {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
              {% for category, message in messages %}
                <div class="alert alert-{{ category }}">
                  {{ message }}
                </div>
              {% endfor %}
            {% endif %}
          {% endwith %}
          {% block content %}{% endblock %}
        </div>
        <div class="col-md-4">
          <div class="content-section">
            <h3>Game Settings</h3>
            <p class='text-muted'>Apply fields of desired genre
              <ul class="list-group">
                <li class="list-group-item list-group-item-light">MMO</li>
                <li class="list-group-item list-group-item-light">FPS</li>
                <li class="list-group-item list-group-item-light">MOBA</li>
                <li class="list-group-item list-group-item-light">RTS</li>
              </ul>
            </p>
          </div>
        </div>
      </div>
    </main>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>
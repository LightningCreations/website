# Website
Website for Lightning Creations

## NOTE:
Before being able to run this website, make sure you copy `secrets_example.json` and create a file named `secrets.json` with your own generated secret key (can be anything).

# Contributing Guide
Before contributing, there are a few prerequesites:
1. Make sure you have a fairly up to date Python3 installation. 3.6+ is probably fine
2. Make sure you have pip/pip3 installed
3. Make sure you install the required pip packages:  
```pip3 install flask flask-wtf flask-sqlalchemy gunicorn flask-login```
4. To run the app, `cd` into the directory and run the `app.py` file  
##### I recommend checking out [this tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) before proceeding  

### Where to put HTML files
HTML files must go in the `templates` directory.  
For each template, make sure you extend the `layout.html` file to automatically get the navbar and all boilerplate code.  
Example `about.html`
```html
{% extends 'layout.html' %}

{% block content %}
    <!-- Insert Your Content Here-->
    <div class="container">
        <h1>About Us</h1>
    </div>
    <!-- ... -->
{% endblock %}
```  

### Where to put static files
Any other files (images, js files, css files, etc) must be put in the `static` directory.
When you are referencing static files in an html file, you must use the `url_for()` function to accomplish this.  
An example link to `style.css` in the `static` directory:
```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

### How to link different routes/pages
Different routes/pages must be linked using the `url_for()` function, similar to above.  
Before you can link to a page though, you need to create the route in the `app.py` file, like so:  
```python
# sample route for an "about.html" page
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
```
  
When you link to this page, you must reference the **function** defined by the route.  
In this case, we say `def about():`, which means we must reference the route as "about".  
An example link to `about.html` using the route we just defined:
```html
<a href="{{url_for('about')}}">About Us</a>
```

### Other Questions?
I recommend first consulting [this tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) before proceeding. It's only 47 minutes long and will clear up most, if not all of your doubts.
Otherwise, feel free to create an issue. (And if you're a part of the Discord Server, ping the project lead)
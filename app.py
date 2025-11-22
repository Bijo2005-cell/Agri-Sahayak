from flask import Flask, g, session, request, render_template, redirect, url_for
import os, json
import datetime  # <-- 1. IMPORT DATETIME

_cache = {}
def load_lang(lang):
    if lang not in _cache:
        path = os.path.join(os.path.dirname(__file__), 'i18n', f'{lang}.json')
        with open(path, 'r', encoding='utf-8') as f:
            _cache[lang] = json.load(f)
    return _cache[lang]

def t(key, lang):
    data = load_lang(lang)
    cur = data
    for p in key.split('.'):
        cur = cur.get(p, {})
    return cur if isinstance(cur, str) else key

def create_app():
    # 2. CORRECTED TYPO: 'tempates' -> 'templates'
    app = Flask(__name__, template_folder='tempates') 
    app.secret_key = os.getenv('SECRET_KEY', 'dev-key')

    # 3. ADDED THIS FUNCTION:
    # This makes 'current_year' available in all your templates.
    @app.context_processor
    def inject_current_year():
        return {'current_year': datetime.datetime.now().year}

    @app.before_request
    def set_lang():
        lang = session.get('lang') or request.args.get('lang') or 'en'
        if lang not in ['en','hi']:
            lang = 'en'
        g.lang = lang
        session['lang'] = lang

    @app.get('/')
    def index():
        return render_template('index.html', t=t, lang=g.lang)

    @app.post('/set-lang')
    def set_lang_post():
        # This is a small improvement:
        # It tries to send the user back where they came from.
        referrer = request.headers.get("Referer") or url_for('index')
        # Update session, as the redirect might not have the 'lang' param
        session['lang'] = request.form.get('lang', 'en')
        return redirect(referrer)

    @app.get('/farmer/dashboard')
    def farmer_dashboard():
        return render_template('farmer_dashboard.html', t=t, lang=g.lang)

    @app.get('/researcher')
    def researcher():
        return render_template('researcher.html', t=t, lang=g.lang)

    @app.get('/student')
    def student():
        return render_template('student.html', t=t, lang=g.lang)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=8000)
from flask import Flask, request, render_template
import ply.lex as lex

app = Flask(__name__)

# Definición de tokens
tokens = (
    'FOR',
    'HOLA_MUNDO',
    'HOLA',
    'MUNDO',
)

# Reglas de los tokens
t_FOR = r'\bfor\b'
t_HOLA_MUNDO = r'\bhola mundo\b'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Token no reconocido: {t.value[0]}")
    t.lexer.skip(1)

def iniciar_lexico(texto):
    lexer = lex.lex()
    lexer.input(texto)
    
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break  
        tokens.append((tok.type, tok.value))  # Guardar tipo y valor
    return tokens

@app.route('/', methods=['GET', 'POST'])
def indext():
    if request.method == 'POST':
        text = request.form['text']
        tokens = iniciar_lexico(text)
        return render_template('index.html', tokens=tokens, text=text)
    return render_template('index.html', tokens=None, text=None)

if __name__ == '__main__':
    app.run(debug=True)

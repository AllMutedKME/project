from flask import render_template, Flask, request
from Decrypted.Symmetry import atbash, caesar, caesar_dec, polybian, polybian_dec, numbers, numbers_dec, gronsfeld, gronsfeld_dec
from Decrypted.Asymmetry import diffie_hellman, diffie_hellman_des, RSA, RSA_des, ElGamal, ElGamal_des, ECDSA, ECDSA_des
from Decrypted.Нashing import SHA384, SHA224, SHA256, SHA1, MD5
from Decrypted.eds import eds

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/atbash', methods =["GET", "POST"])
def get_freq():
    if request.method == "POST":
        mesege = request.form['mesege']
        cryt = atbash(mesege)
        return render_template('atbash.html', title="Атбаш", cryt=cryt, mesege=mesege)
    else:
        return render_template('atbash.html', title="Атбаш")
    
@app.route('/caesar', methods =["GET", "POST"])
def get_caesar():
    if request.method == "POST":
        mesege = request.form['mesege']
        key = request.form['key']
        if key == '': key = 0
        cryt = caesar(mesege, int(key))
        key_des = request.form['key_des']
        if key_des == '': key_des = key
        cry_mesege = request.form["cry_mesege"]
        decrypt = caesar_dec(cry_mesege, int(key_des))
        return render_template('caesar.html', title="Шифр Цезаря", cryt=cryt, mesege=mesege, key=key, cry_mesege=cry_mesege, decrypt=decrypt, key_des=key_des)
    else:
        return render_template('caesar.html', title="Шифр Цезаря")


@app.route('/polybian', methods =["GET", "POST"])
def get_polybian():
    if request.method == "POST":
        mesege = request.form['mesege']
        cryt = polybian(mesege)
        cry_mesege = request.form["cry_mesege"]
        decrypt = polybian_dec(cry_mesege)
        return render_template('polybian.html', title="Квадрат Полибия", cryt=cryt, mesege=mesege, cry_mesege=cry_mesege, decrypt=decrypt)
    else:
        return render_template('polybian.html', title="Квадрат Полибия")
    
@app.route('/numbers', methods =["GET", "POST"])
def get_numbers():
    if request.method == "POST":
        mesege = request.form['mesege']
        key = request.form['key']
        cryt = numbers(key, mesege)
        key_des = request.form['key_des']
        cry_mesege = request.form["cry_mesege"]
        decrypt = numbers_dec(key_des, cry_mesege)
        return render_template('numbers.html', title="Шифровка цифр", cryt=cryt, mesege=mesege, key=key, cry_mesege=cry_mesege, decrypt=decrypt, key_des=key_des)
    else:
        return render_template('numbers.html', title="Шифровка цифр")


@app.route('/gronsfeld', methods =["GET", "POST"])
def get_gronsfeld():
    if request.method == "POST":
        mesege = request.form['mesege']
        key = request.form['key']
        cryt = gronsfeld(key, mesege)
        key_des = request.form['key_des']
        cry_mesege = request.form["cry_mesege"]
        decrypt = gronsfeld_dec(key_des, cry_mesege)
        return render_template('gronsfeld.html', title="Шифр Гронсфельда", cryt=cryt, mesege=mesege, key=key, cry_mesege=cry_mesege, decrypt=decrypt, key_des=key_des)
    else:
        return render_template('gronsfeld.html', title="Шифр Гронсфельда")

#АССИМЕТРИЯ

@app.route('/diffie_hellman', methods =["GET", "POST"])
def get_diffie_hellman():
    
    if request.method == "POST":
        message = request.form['message']
        s_public = int(request.form['s_public'])
        s_private = int(request.form['s_private'])
        m_public, m_private = 151, 157
        cryt = diffie_hellman(message, s_public, s_private, m_public, m_private)
        cry_message = request.form["cry_message"]
        decrypt = diffie_hellman_des(cry_message,  s_public, s_private, m_public, m_private)
        return render_template('diffie_hellman.html', title="Шифр diffie hellman", message=message, s_public=s_public,
                               s_private=s_private, m_public=m_public, cryt=cryt, decrypt=decrypt, cry_message=cry_message)
    else:
        return render_template('diffie_hellman.html', title="Шифр diffie hellman")

@app.route('/RSA', methods =["GET", "POST"])
def get_RSA():
    if request.method == "POST":
        message = int(request.form['message'])
        p_public = int(request.form['p_public'])
        q_public = int(request.form['q_public'])
        e_public = int(request.form['e_public'])
        cryt, d, n = RSA(message, p_public, q_public, e_public)
        cry_message = request.form["cry_message"]
        if cry_message != '':
            decrypt = RSA_des(int(cry_message), d, n,  p_public, q_public, e_public)
        else:
            decrypt = ''
        return render_template('RSA.html', title="Шифр RSA", message=message, p_public=p_public, cry_message=cry_message,
                               q_public=q_public, e_public=e_public, cryt=cryt, decrypt=decrypt)
    return render_template('RSA.html', title="Шифр RSA")
    
@app.route('/ElGamal', methods =["GET", "POST"])
def get_ElGamal():
    if request.method == "POST":
        message = request.form['message']
        q_public = int(request.form['q_public'])
        g_public = int(request.form['g_public'])
        cryt, p, key, q = ElGamal(message, q_public, g_public)
        cry_message = request.form["cry_message"]
        decrypt = ElGamal_des(cryt, p, key, q)
        return render_template('ElGamal.html', title="Шифр ElGamal", message=message, key=key, q_public=q_public,
                               g_public=g_public, cry_message=cry_message, cryt=cryt, decrypt=decrypt)
    return render_template('ElGamal.html', title="Шифр ElGamal")

@app.route('/ECDSA', methods =["GET", "POST"])
def get_ECDSA():
    if request.method == "POST":
        message = int(request.form['message'])
        public_key = int(request.form['public_key'])
        cryt, k, k_inverse, public_key, n, private_key = ECDSA(public_key, message)
        cry_message = request.form["cry_message"]
        print(private_key)
        if cry_message != '':
            decrypt = ECDSA_des(cryt, k, k_inverse, public_key, n)
            cryt = ''
            return render_template('ECDSA.html', title="Шифр ECDSA", message=message, public_key=public_key, private_key=private_key,
                                cry_message=cry_message, cryt=cryt, decrypt=decrypt)
        return render_template('ECDSA.html', title="Шифр ECDSA", message=message, public_key=public_key, private_key=private_key,
                                cry_message=cry_message, cryt=cryt)
    return render_template('ECDSA.html', title="Шифр ECDSA")
#ХЕШИРОВАНИЕ

@app.route('/sha256', methods =["GET", "POST"])
def get_sha256():
    if request.method == "POST":
        mesege = request.form['password']
        cryt = SHA256(mesege)
        return render_template('sha256.html', title="sha256", cryt=cryt, mesege=mesege)
    else:
        return render_template('sha256.html', title="sha256")


@app.route('/md5', methods =["GET", "POST"])
def get_md5():
    if request.method == "POST":
        mesege = request.form['password']
        cryt = MD5(mesege)
        return render_template('md5.html', title="md5", cryt=cryt, mesege=mesege)
    else:
        return render_template('md5.html', title="md5")


@app.route('/sha1', methods =["GET", "POST"])
def get_sha1():
    if request.method == "POST":
        mesege = request.form['password']
        cryt = SHA1(mesege)
        return render_template('sha1.html', title="sha1", cryt=cryt, mesege=mesege)
    else:
        return render_template('sha1.html', title="sha1")


@app.route('/sha224', methods =["GET", "POST"])
def get_sha224():
    if request.method == "POST":
        mesege = request.form['password']
        cryt = SHA224(mesege)
        return render_template('sha224.html', title="sha224", cryt=cryt, mesege=mesege)
    else:
        return render_template('sha224.html', title="sha224")


@app.route('/sha384', methods =["GET", "POST"])
def get_sha384():
    if request.method == "POST":
        mesege = request.form['password']
        cryt = SHA384(mesege)
        return render_template('sha384.html', title="sha384", cryt=cryt, mesege=mesege)
    else:
        return render_template('sha384.html', title="sha384")


@app.route('/eds', methods =["GET", "POST"])
def get_eds():
    if request.method == "POST":
        key = request.form['key']
        mesege = request.form['mesege']
        cryt = eds(int(key), int(mesege))

        print(cryt)
        return render_template('eds.html', title="ЭЦП", cryt=cryt, mesege=mesege)
    else:
        return render_template('eds.html', title="ЭЦП")
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
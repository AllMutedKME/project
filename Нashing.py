import uuid
import hashlib
def SHA256(new_pass):
    def hash_password(password):
        # uuid используется для генерации случайного числа
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
            
    hashed_password = hash_password(new_pass)
    return hashed_password

def sha256(hashed_password, old_pass):
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
    
    if check_password(hashed_password, old_pass):
        return 'Вы ввели правильный пароль'
    else:
        return 'Извините, но пароли не совпадают'


def MD5(new_pass):
    def hash_password(password):
        # uuid используется для генерации случайного числа
        salt = uuid.uuid4().hex
        return hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt

    hashed_password = hash_password(new_pass)
    return hashed_password

def md5(hashed_password, old_pass):
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.md5(salt.encode() + user_password.encode()).hexdigest()
    
    if check_password(hashed_password, old_pass):
        return 'Вы ввели правильный пароль'
    else:
        return 'Извините, но пароли не совпадают'

def SHA1(new_pass):
    def hash_password(password):
        # uuid используется для генерации случайного числа
        salt = uuid.uuid4().hex
        return hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
      
    hashed_password = hash_password(new_pass)
    return hashed_password

def sha1( hashed_password, old_pass):
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha1(salt.encode() + user_password.encode()).hexdigest()
    
    if check_password(hashed_password, old_pass):
        return 'Вы ввели правильный пароль'
    else:
        return 'Извините, но пароли не совпадают'


def SHA224(new_pass):
    def hash_password(password):
        # uuid используется для генерации случайного числа
        salt = uuid.uuid4().hex
        return hashlib.sha224(salt.encode() + password.encode()).hexdigest() + ':' + salt
           
    hashed_password = hash_password(new_pass)
    return hashed_password
    
def sha224(hashed_password, old_pass):
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha224(salt.encode() + user_password.encode()).hexdigest()
    
    if check_password(hashed_password, old_pass):
        return 'Вы ввели правильный пароль'
    else:
        return 'Извините, но пароли не совпадают'


def SHA384(new_pass):
    def hash_password(password):
        # uuid используется для генерации случайного числа
        salt = uuid.uuid4().hex
        return hashlib.sha384(salt.encode() + password.encode()).hexdigest() + ':' + salt

    hashed_password = hash_password(new_pass)
    return hashed_password

def sha384(hashed_password, old_pass):
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha384(salt.encode() + user_password.encode()).hexdigest()
    if check_password(hashed_password, old_pass):
        return 'Вы ввели правильный пароль'
    else:
        return 'Извините, но пароли не совпадают'

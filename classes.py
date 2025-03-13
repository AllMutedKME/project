from math import gcd
import random

class DH_Endpoint(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key
    
    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c)+key)
        return encrypted_message
    
    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c)-key)
        return decrypted_message

class RSA_Endpoint(object):
    def __init__(self, public_key1, public_key2, public_e):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.public_e = public_e
        self.private_key = None
        self.full_key = None
    
    def n_mod(self, public_key1, public_key2):
        return public_key1 * public_key2
    
    def function_Euler(self, public_key1, public_key2):
        return (public_key1 - 1) * (public_key2 - 1)
    
    def private_exponent(self, public_exponent, phi):
        return pow(public_exponent, -1, phi)
    
    def encrypt_message(self, message, public_exponent, modul_n):
        return pow(message, public_exponent, modul_n)
    
    def decrypt_message(self, message, private_exponent, modul_n):
        return pow(message, private_exponent, modul_n)
    
class LG_Endpoint(object):
    def gcd(a, b):
        if a < b:
            return gcd(b, a)
        elif a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    
    # Generating large random numbers
    def gen_key(q):
        key = random.randint(pow(10, 20), q)
        while gcd(q, key) != 1:
            key = random.randint(pow(10, 20), q)
        return key
    
    # Modular exponentiation
    def power(a, b, c):
        x = 1
        y = a
        while b > 0:
            if b % 2 != 0:
                x = (x * y) % c
            y = (y * y) % c
            b = int(b / 2)
        return x % c
    
    # Asymmetric encryption
    def encrypt(msg, q, h, g):
        en_msg = []
        k = LG_Endpoint.gen_key(q)# Private key for sender
        s = LG_Endpoint.power(h, k, q)
        p = LG_Endpoint.power(g, k, q)
        for i in range(0, len(msg)):
            en_msg.append(msg[i])
        #print("g^k used : ", p)
        #print("g^ak used : ", s)
        for i in range(0, len(en_msg)):
            en_msg[i] = s * ord(en_msg[i])
        return en_msg, p

    def decrypt(en_msg, p, key, q):
        dr_msg = []
        h = LG_Endpoint.power(p, key, q)
        for i in range(0, len(en_msg)):
            dr_msg.append(chr(int(en_msg[i]/h)))
        return dr_msg

class ECDSA_Endpoint(object):
    def find_inverse(number, modulus):
        return pow(number, -1, modulus)
    
    def multiply(self, times):
            current_point = self
            current_coefficient = 1

            pervious_points = []
            while current_coefficient < times:
                # store current point as a previous point
                pervious_points.append((current_coefficient, current_point))
                # if we can multiply our current point by 2, do it
                if 2 * current_coefficient <= times:
                    current_point = current_point.add(current_point)
                    current_coefficient = 2 * current_coefficient
                # if we can't multiply our current point by 2, let's find the biggest previous point to add to our point
                else:
                    next_point = self
                    next_coefficient = 1
                    for (previous_coefficient, previous_point) in pervious_points:
                        if previous_coefficient + current_coefficient <= times:
                            if previous_point.x != current_point.x:
                                next_coefficient = previous_coefficient
                                next_point = previous_point
                    current_point = current_point.add(next_point)
                    current_coefficient = current_coefficient + next_coefficient

            return current_point
    
    
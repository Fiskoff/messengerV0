from bcrypt import gensalt, hashpw, checkpw


class PasswordManager:
    __SALT_LENGTH = 16
    __HASH_LENGTH = 60
    __COST_FACTOR = 14

    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode('utf-8')
        salt = gensalt(rounds=PasswordManager.__COST_FACTOR, prefix=b'2b')
        hash_password = hashpw(password_bytes, salt)
        return hash_password.decode("utf-8")

    @staticmethod
    def verify_password(input_password: str, hashed_password_from_db: str) -> bool:
        input_password = input_password.encode('utf-8')
        hashed_bytes = hashed_password_from_db.encode('utf-8')
        return checkpw(input_password, hashed_bytes)

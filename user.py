class User:
    def __init__(self, name: str, email: str):
        self.__name = name  # private attribute
        self.__email = email  # private attribute

    def update_name(self, new_name: str):
        self.__name = new_name

    def update_email(self, new_email: str):
        self.__email = new_email

    def get_user_info(self) -> dict:
        return {
            "name": self.__name,
            "email": self.__email
        }
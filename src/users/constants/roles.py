from enum import Enum

__all__ = ["Role"]


class Role(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

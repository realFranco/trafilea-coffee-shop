from pydantic import BaseModel


class CartModel(BaseModel):
    id: int = None
    user_id: int = None

from google import genai
from typing import Optional
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


class BaristaService:

    def __init__(self):
        self.order = []
        self.placed_order = []

    def add_to_order(self, drink: str, modifiers: Optional[list[str]] = None) -> None:
        """Adds the specified drink to the customer's order, including any modifiers."""
        if modifiers is None:  # Ensures safe handling of None
            modifiers = []
        self.order.append((drink, modifiers))

    def get_order(self) -> list[tuple[str, list[str]]]:
        """Returns the customer's order."""
        return self.order


    def remove_item(self, n: int) -> str:
        """Removes the nth (one-based) item from the order.

        Returns:
            The item that was removed.
        """
        item, _ = self.order.pop(n - 1)
        return item


    def clear_order(self) -> None:
        """Removes all items from the customer's order."""
        self.order.clear()


    def place_order(self) -> int:
        """Submit the order to the kitchen.

        Returns:
            The estimated number of minutes until the order is ready.
        """
        self.placed_order[:] = self.order.copy()
        self.clear_order()

        # TODO: Implement coffee fulfillment.
        return randint(1, 10)

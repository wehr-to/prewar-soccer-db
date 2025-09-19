# Search logic (by player, year, etc.)

from app.models import Card, CardSet
from app.utils import sanitize_string, is_valid_year
from app import db

# Search by player

def search_by_player(player_name: str):
    """
    Return all cards for a given player across years and sets.
    """
    name = sanitize_string(player_name)

    if not name:
        return []

    results = (
        Card.query.join(CardSet)
        .filter(Card.player_name.ilike(f"%{name}%"))
        .order_by(CardSet.year.asc())
        .all()
    )
    return results

# Search by year

def search_by_year(year: str):
    """
    Return all sets from a given year.
    """
    if not is_valid_year(year):
        return []

    results = (
        CardSet.query.filter(CardSet.year == int(year))
        .order_by(CardSet.producer.asc())
        .all()
    )
    return results

# Search by producer

def search_by_producer(producer: str):
    """
    Return all sets by a given producer (e.g., Panini, Ogden's).
    """
    name = sanitize_string(producer)

    if not name:
        return []

    results = (
        CardSet.query.filter(CardSet.producer.ilike(f"%{name}%"))
        .order_by(CardSet.year.asc())
        .all()
    )
    return results

from .client import ForumSession

def login(token: str = None, user_id: str | int = None, forum_url: str = "https://lgdc.flarum.cloud") -> ForumSession:
    """Initialise et retourne une session connectée (ou anonyme si pas de token)."""
    return ForumSession(api_token=token, user_id=user_id, forum_url=forum_url)

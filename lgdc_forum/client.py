import requests

class ForumSession:
    def __init__(self, api_token: str = None, user_id: str | int = None, forum_url: str = "https://lgdc.flarum.cloud"):
        self.base_url = forum_url.rstrip('/')
        self.api_url = f"{self.base_url}/api"
        self.api_token = api_token
        self.user_id = str(user_id) if user_id else None

    def _get_headers(self):
        headers = {"Content-Type": "application/vnd.api+json"}
        if self.api_token and self.user_id:
            headers["Authorization"] = f"Token {self.api_token}; userId={self.user_id}"
        return headers

    def post(self, content: str, discussion_id: str | int):
        """Envoie un message dans une discussion existante."""
        if not self.api_token or not self.user_id:
            raise ValueError("Jeton d'authentification requis pour poster.")

        payload = {
            "data": {
                "type": "posts",
                "attributes": {"content": content},
                "relationships": {
                    "discussion": {
                        "data": {"type": "discussions", "id": str(discussion_id)}
                    }
                }
            }
        }
        response = requests.post(
            f"{self.api_url}/posts",
            json=payload,
            headers=self._get_headers()
        )
        return response.status_code == 201

    def create_discussion(self, title: str, content: str, tag_ids: list[str | int] = None):
        """Crée un nouveau sujet de discussion (avec ou sans catégories/sous-catégories)."""
        if not self.api_token or not self.user_id:
            raise ValueError("Jeton d'authentification requis pour créer une discussion.")

        tags_data = [{"type": "tags", "id": str(tag_id)} for tag_id in (tag_ids or [])]

        payload = {
            "data": {
                "type": "discussions",
                "attributes": {
                    "title": title,
                    "content": content
                },
                "relationships": {
                    "tags": {
                        "data": tags_data
                    }
                }
            }
        }

        response = requests.post(
            f"{self.api_url}/discussions",
            json=payload,
            headers=self._get_headers()
        )
        return response.status_code == 201

    def get_user_data(self, target_user_id: str | int):
        """Récupère les données brutes d'un utilisateur par son ID."""
        response = requests.get(
            f"{self.api_url}/users/{target_user_id}",
            headers=self._get_headers()
        )
        if response.status_code == 200:
            return response.json()
        return None

    def get_username(self, target_user_id: str | int) -> str | None:
        """Récupère le nom d'utilisateur (username) à partir de son ID."""
        data = self.get_user_data(target_user_id)
        if data and "data" in data:
            return data["data"].get("attributes", {}).get("username")
        return None

    def get_user_groups(self, target_user_id: str | int):
        """Récupère les groupes d'un utilisateur par son ID."""
        json_data = self.get_user_data(target_user_id)
        if not json_data:
            return []

        user_rel_groups = (
            json_data.get("data", {})
            .get("relationships", {})
            .get("groups", {})
            .get("data", [])
        )
        group_ids = {group["id"] for group in user_rel_groups}

        groups = []
        for item in json_data.get("included", []):
            if item.get("type") == "groups" and item.get("id") in group_ids:
                group_info = {"id": item.get("id")}
                group_info.update(item.get("attributes", {}))
                groups.append(group_info)

        return groups

    def get_tags(self):
        """Récupère toutes les catégories (tags) du forum avec leur parenté."""
        response = requests.get(f"{self.api_url}/tags", headers=self._get_headers())
        if response.status_code != 200:
            return []

        data = response.json().get("data", [])
        tags = []
        for tag in data:
            parent_rel = tag.get("relationships", {}).get("parent", {}).get("data")
            tags.append({
                "id": tag.get("id"),
                "name": tag.get("attributes", {}).get("name"),
                "slug": tag.get("attributes", {}).get("slug"),
                "parent_id": parent_rel.get("id") if parent_rel else None
            })
        return tags

    def get_subcategories(self, parent_tag_id: str | int):
        """Récupère uniquement les sous-catégories associées à un tag parent."""
        all_tags = self.get_tags()
        return [t for t in all_tags if str(t["parent_id"]) == str(parent_tag_id)]

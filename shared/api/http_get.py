import requests

def http_get(url: str, params: dict[str, object]):
    try:
        response = requests.get(
            url=url,
            params=params,
        )
        result = response.json()
        response.raise_for_status()
        return {
            "success": True,
            "status": response.status_code,
            "data": result,
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}",
        }

import requests
class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"

        response = self.session.request(
            method=method,
            url=url,
            timeout=10,
            **kwargs
        )
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise Exception(
                f"""
                API Request Failed:Method: {method}
                URL: {url}
                Status Code: {response.status_code}
                Response: {response.text}"""
            ) from e

        return response


    def get(self, endpoint: str, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)
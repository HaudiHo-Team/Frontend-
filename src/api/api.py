import os
import requests
import streamlit as st
from typing import Any, Dict, Optional, List, Union

class Api:
    def __init__(
        self,
        base_url: Optional[str] = None,
        token: Optional[str] = None,
        use_bearer: bool = True,
        api_key_header: str = "X-API-Key",
        default_timeout: int = 30,
    ):
        self.base_url = (base_url or
                         os.getenv("PUBLIC_API_ENDPOINT") or
                         "http://213.171.4.67:8000")
        self.token = token or os.getenv("API_TOKEN") or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJpb2kifQ.aqTJGzKPtdU_8MD92unXMFCpcam_iNSl16FZgM3gZ-o"
        self.use_bearer = use_bearer
        self.api_key_header = api_key_header
        self.default_timeout = default_timeout

        if not isinstance(self.base_url, str) or not self.base_url:
            raise ValueError("base_url must be a non-empty string")

    def _auth_headers(self) -> Dict[str, str]:
        if not self.token:
            return {}
        if self.use_bearer:
            return {"Authorization": f"Bearer {self.token}"}
        return {self.api_key_header: self.token}

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        hdrs = {
            **self._auth_headers(), 
            **{"Content-Type": "application/json", "Accept": "application/json"},
            **(headers or {})
        }
        
        if os.getenv("DEBUG", "false").lower() == "true":
            print(f"Debug - Making request to: {url}")
            print(f"Debug - Headers: {hdrs}")

        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                params=params,
                json=json,
                data=data,
                headers=hdrs,
                timeout=timeout or self.default_timeout,
            )
            
            if os.getenv("DEBUG", "false").lower() == "true":
                print(f"Debug - Response status: {resp.status_code}")
                print(f"Debug - Response headers: {dict(resp.headers)}")
                print(f"Debug - Response content (first 500 chars): {resp.text[:500]}")
            
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        return self._request("GET", path, params=params, headers=headers)

    def post(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, data=None):
        return self._request("POST", path, json=json, data=data, headers=headers)

    def put(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, data=None):
        return self._request("PUT", path, json=json, data=data, headers=headers)

    def delete(self, path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        return self._request("DELETE", path, params=params, headers=headers)

    def upload_file(self, file_data: bytes, filename: str, content_type: str = None, headers: Optional[Dict[str, str]] = None):
        """Загружает файл на сервер"""
        url = f"{self.base_url}/files/"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        files = {
            'file': (filename, file_data, content_type or 'application/octet-stream')
        }
        
        try:
            resp = requests.post(
                url=url,
                files=files,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def get_file_result(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Получает результат обработки файла"""
        url = f"{self.base_url}/files/{file_id}/result"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.get(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def get_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Получает информацию о файле"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.get(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def get_files_list(self, headers: Optional[Dict[str, str]] = None):
        """Получает список файлов"""
        url = f"{self.base_url}/files/"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.get(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    def delete_file(self, file_id: str, headers: Optional[Dict[str, str]] = None):
        """Удаляет файл по ID"""
        url = f"{self.base_url}/files/{file_id}"
        hdrs = {**self._auth_headers(), **(headers or {})}
        
        try:
            resp = requests.delete(
                url=url,
                headers=hdrs,
                timeout=self.default_timeout
            )
            resp.raise_for_status()
            try:
                return resp.json()
            except ValueError:
                return resp.text
        except requests.HTTPError as e:
            body = e.response.text if e.response is not None else str(e)
            print(f"HTTP error ({e.response.status_code if e.response else 'n/a'}): {body}")
            raise
        except requests.RequestException as e:
            print(f"Network error: {str(e)}")
            raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise



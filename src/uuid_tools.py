from requests import Session

class UuidTools:
	def __init__(self) -> None:
		self.api = "https://www.uuidtools.com/api"
		self.session = Session())
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def generate_uuid_v1(self, count: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/generate/v1/count/{count}").json()

	def generate_uuid_v3(
			self,
			name: str,
			name_space: str) -> dict:
		return self.session.get(
			f"{self.api}/generate/v3/namespace/{name_space}/name/{name}").json()

	def generate_uuid_v4(self, count: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/generate/v4/count/{count}").json()

	def generate_uuid_v5(self, name: str, name_space: str) -> dict:
		return self.session.get(
			f"{self.api}/generate/v5/namespace/{name_space}/name/{name}").json()

	def generate_timestamp_first_uuid(self, count: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/generate/timestamp-first/count/{count}").json()

	def decode_uuid(self, uuid: str) -> dict:
		return self.session.get(f"{self.api}/decode/{uuid}").json()

from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    name_safe: str
    email: str
    password_bcrypt: str
    ban_ts: int
    register_ts: int
    silence_end_ts: int
    silence_reason: str
    privileges: int # TODO: Priv enum.
    donor_expire_ts: int
    ban_reason: str

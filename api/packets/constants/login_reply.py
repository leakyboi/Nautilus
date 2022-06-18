from enum import IntEnum

class LoginReply(IntEnum):
    """Enumeration for the login response IDs."""

    FAILED = -1
    OUTDATED_CLIENT = -2
    BANNED = -3 # TODO: find a way to make these 2 eq.
    BANNED_2 = -4 # They are handled by the same case statement in the client.
    BANCHO_ERROR = -5
    SUPPORTER_REQUIRED = -6
    PASSWORD_RESET = -7
    VERIFICATION_REQUIRED = -8

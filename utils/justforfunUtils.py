import hmac
import hashlib
import time
import struct

class JustForFunUtil:
    """
    Going to push more comments like these
    `print("Just for fun")`
    Todo: Implement system design concepts here-    
    """
    def flatten_the_dict(self, simple_dict):
        """
        Flatens the dict such that if a nested dict is given
        , no matter how many levels of nesting is present. It recursively
        flatens the dict all in single level.
        """
        ans_dict = {}

        def flatten_dict(parent_key, dict_val):
            for child_key, value in dict_val.items():
                if isinstance(value, dict):
                    flatten_dict(parent_key+"_"+child_key, value)
                else:
                    ans_dict[parent_key+"_"+child_key] = value
            return

        flatten_dict("", simple_dict)

        return ans_dict

    def HOTP(self, K, C, digits=10):
        """HTOP:
        K is the shared key
        C is the counter value
        digits control the response length
        """
        K_bytes = K.encode()
        C_bytes = struct.pack(">Q", C)
        hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
        return self.Truncate(hmac_sha512)[-digits:]
    
    def Truncate(self, hmac_sha512):
        """truncate sha512 value"""
        offset = int(hmac_sha512[-1], 16)
        binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
        return str(binary)

    def generate_totp(self, secret, digits=10, timeref=0, timestep = 30):
        """TOTP, time-based variant of HOTP
        digits control the response length
        the C in HOTP is replaced by ( (currentTime - timeref) / timestep )
        """
        C = int (time.time() - timeref ) // timestep
        return self.HOTP(secret, C, digits = digits)
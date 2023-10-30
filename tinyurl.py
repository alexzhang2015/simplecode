import hashlib
import time
import random

def generate_hash_string(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()[:6]

global_dict = {
    "abcdef": "https://github.com/viatsko/awesome-vscode/tree/master"
}

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        if longUrl in global_dict.values():
            return
        hash_value = generate_hash_string(longUrl.join(str(time.time()).join(str(random.randint(1, 100))
)))
        while hash_value in global_dict:
            hash_value = generate_hash_string(longUrl.join(str(time.time()).join(str(random.randint(1, 100))
)))
        global_dict[hash_value] = longUrl
        return 'http://tinyurl.com/'.join(hash_value)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return global_dict[shortUrl.replace("http://tinyurl.com/", "")]

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))


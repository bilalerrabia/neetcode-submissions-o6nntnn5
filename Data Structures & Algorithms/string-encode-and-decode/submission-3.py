class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "raknkhawer"
        return "bilal1337".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "raknkhawer":
            return []
        return s.split("bilal1337")
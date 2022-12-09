class Database:
    
    def __init__(self, long_to_short={}, short_to_long={}, base_URL= "http://short.ner/")-> None:
        self.long_to_short= long_to_short
        self.short_to_long= short_to_long
        self.base_URL= base_URL

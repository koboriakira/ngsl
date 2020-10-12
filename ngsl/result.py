class Result:
    def __init__(self, ngsl_words, not_ngsl_words) -> None:
        self.ngsl_words = sorted(ngsl_words)
        self.not_ngsl_words = sorted(not_ngsl_words)

from pysad.core.base_model import BaseModel


class NullModel(BaseModel):

    def __init__(self):
        super().__init__()

        self.labels = []

    def fit_partial(self, x, y=None):

        return self

    def score_partial(self, x):

        return 0.5

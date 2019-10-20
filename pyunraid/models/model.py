class Model():

    def __init__(self):
        pass

    def to_dict(self):
        """Convert Model to dictionary"""
        dict = {}

        for k, v in vars(self).items():
            if not k.startswith('_') or callable(v):
                dict[k] = v

        return dict

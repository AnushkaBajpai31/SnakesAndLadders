class BoardUtility:
    def __init__(self, reference_dict):
        reference_dict.update({'distanceDict': {tuple(v): k for k, v in reference_dict['boardDict'].items()}})
        self.refDict = reference_dict

    def getBoardDict(self):
        return self.refDict['boardDict']

    def getDistanceDict(self):
        return self.refDict['distanceDict']
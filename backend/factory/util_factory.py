class UtilFactory:

    @staticmethod
    def getBoardUtility(reference_dict):
        from utility.board import BoardUtility
        return BoardUtility(reference_dict)

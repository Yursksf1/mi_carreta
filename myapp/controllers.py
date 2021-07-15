from myapp.models import HistoryWeather, SheepBreed


class SheepController(object):
    """
    contain methods related to Sheeps
    """

    @staticmethod
    def get_id_pure():
        """
        Return id pures
        return list ids. Ie, [12,13,14,25]
        """

        pure = 80
        sheep_breeds = SheepBreed.objects.filter(percent__gte=pure).all()
        ids_pure = [sheep_breed.sheep.id for sheep_breed in sheep_breeds]
        return ids_pure

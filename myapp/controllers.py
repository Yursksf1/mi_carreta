from myapp.models import HistoryWeather, SheepBreed, HistoryWeight


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

    @staticmethod
    def get_id_range_weight(weight_range_min, weight_range_max):
        # todo check
        weight = HistoryWeight.objects.order_by('-create_at')

        ids_weight = []
        for w in weight:
            if weight_range_min and w.weight < weight_range_min:
                continue

            if weight_range_max and w.weight > weight_range_max:
                continue

            ids_weight.append(w.sheep.id)

        return ids_weight
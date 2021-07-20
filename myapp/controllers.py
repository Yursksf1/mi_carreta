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
        sheep_current_height = {}
        weights = HistoryWeight.objects.order_by('create_at').all()
        ids_weight = []
        for i in weights:
            if i.sheep not in sheep_current_height:
                sheep_current_height[i.sheep] = i
            else:
                if sheep_current_height[i.sheep].create_at < i.create_at:
                    sheep_current_height[i.sheep] = i

        for key, value in sheep_current_height.items():
            if weight_range_min and value.weight < weight_range_min:
                continue

            if weight_range_max and value.weight > weight_range_max:
                continue

            ids_weight.append(str(value.sheep.id))


        return ids_weight
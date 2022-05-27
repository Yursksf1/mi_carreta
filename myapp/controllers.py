from myapp.models import Sheep, Group, SheepGroup, HistoryWeather, SheepBreed, HistoryWeight, HistoryFamacha, HistoryBodyCondition, Observations


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
    def get_id_in_group(group_name):
        """
        Return id sheep in group
        :param: group_name, name gropu Ie, "service"
        return list ids. Ie, [12,13,14,25]
        """
        group = Group.objects.filter(slug=group_name).first()

        sheep_groups = SheepGroup.objects.filter(group=group).all()
        ids_sheep = [sheep_group.sheep.id for sheep_group in sheep_groups]
        return ids_sheep

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

    @staticmethod
    def update_weight(pk, data):
        """
        Update values weight
        :param pk: UUID, unique sheep identifier Ie, 'ce24c41c-1660-42db-ab47-78e5380ec0ac'
        :param data: dict, values update Ie:
            data = {
                'date': data_request.get('date')[0],
                'weight': data_request.get('weight')[0],
                'famacha': data_request.get('famacha')[0],
                'corporal': data_request.get('corporal')[0],
                'evaluation-reproductive': data_request.get('evaluation-reproductive')[0],
                'observacion': data_request.get('observacion')[0],
            }
        """
        sheep = Sheep.objects.filter(id=pk).first()
        if sheep:
            date = data.get('date')
            weight = data.get('weight')
            famacha = data.get('famacha')
            corporal = data.get('corporal')
            evaluation_reproductive = data.get('evaluation_reproductive')
            observacion = data.get('observacion')

            if weight:
                hw = HistoryWeight()
                hw.sheep = sheep
                hw.weight = data.get('weight')
                hw.save()

            if famacha:
                hw = HistoryFamacha()
                hw.sheep = sheep
                hw.famacha = famacha
                hw.save()

            if corporal:
                hw = HistoryBodyCondition()
                hw.sheep = sheep
                hw.body_condition = corporal
                hw.save()

            if observacion:
                hw = Observations()
                hw.sheep = sheep
                hw.description = observacion
                hw.active = True
                hw.save()
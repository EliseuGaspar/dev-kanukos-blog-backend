





class Convertor:

    @classmethod
    def convert_queryset_to_dict(cls, queryset: any, instance: any, Serializer: any = None) -> dict:
        if Serializer:
            serializer = Serializer(queryset, many = True)
            return serializer.data[0]
        serializer = instance.get_serializer(queryset, many = True)
        return serializer.data[0]


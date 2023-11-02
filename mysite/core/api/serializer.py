from rest_framework.fields import Field
from wagtail.query import PageQuerySet


class CommonImageSerializer(Field):

    def to_representation(self, value):
        return value.get_rendition('original').url



class ImageAndThumbSerializer(Field):

    def to_representation(self, value):
        data = []
        images = value.all()
        for image in images:
            _meta = {}
            _meta['src'] = image.src.get_rendition('original').url
            _meta['thumb'] = image.src.get_rendition('fill-200x200').url 
            data.append(_meta)
        return data



class CommonForeignKeyNameSerializer(Field):

    def to_representation(self, value):
        if value:
            return value.name


class CommonPageSerializer(Field):
    def _get_value(self, val, field):
        field_name = field.name
        val = getattr(val, field_name)
        try:
            if field.serializer:
                if callable(field.serializer):
                    return field.serializer().to_representation(val)
                else:
                    return field.serializer.to_representation(val)
            else:
                return val
        except:
            return ''

    def to_representation(self, value):
        api_fields = value.specific.api_fields
        final_data = {}
        for field in api_fields:
            val = self._get_value(value.specific, field)
            final_data[field.name] = val
        return final_data
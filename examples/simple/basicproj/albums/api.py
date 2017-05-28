from rest_framework import routers, serializers, viewsets

from rest_framework_yaml.parsers import YAMLParser
from rest_framework_yaml.renderers import YAMLRenderer

from albums.models import Album, Track


# via http://www.django-rest-framework.org/api-guide/relations/


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')



class AlbumSerializer(serializers.ModelSerializer):
    #tracks = serializers.StringRelatedField(many=True)
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')

# see also http://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    parser_classes = (YAMLParser,)
    renderer_classes = (YAMLRenderer,)



from rest_framework.renderers import CoreJSONRenderer
from rest_framework.schemas import SchemaGenerator
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
@renderer_classes([CoreJSONRenderer])
def schema_view(request):
    generator = SchemaGenerator(title='Koldunov API')
    return Response(generator.get_schema())

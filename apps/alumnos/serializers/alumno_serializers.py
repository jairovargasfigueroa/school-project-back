
from rest_framework import serializers
from apps.alumnos.models import Alumno


#Clase para definir las validaciones y la estructura de los datos del modelo Alumno
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'  # Serialize all fields of the Alumno model

    def validate(self, data):
        """
        Validates the data for the Alumno model.
        :param data: Dictionary containing the data to validate.
        :return: Validated data.
        """
        # Example validation: Ensure 'nombre' is not empty
        if len(data.get('telefono')) < 5:
            raise serializers.ValidationError("El campo 'telefono' debe tener al menos 8 caracteres.")
            # raise serializers.ValidationError("El campo 'nombre' es obligatorio.")
        
        # Add more validations as needed
        return data
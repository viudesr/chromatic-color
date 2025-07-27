class ChromaticColor:
    """
    Class used to define chromatic colors as well as operate actions on here-defined colors.
    """


    def __init__(self, red, green, blue):

        self._rgb = (0, 0, 0)
        self.set_rgb(red, green, blue)

    def check_rgb_component_value(self, value):
        """
        Assert that the provided RGB component value is correct, that is to say:
        - It is an integer
        - Its value is between 0 and 255
        If an issue is found, raises an error
        """

        if not isinstance(value, int):
            raise TypeError(f"Invalid component type: {type(value)} instead of int")

        if value < 0 or value > 255:
            raise ValueError(f"Invalid value: {value}. RGB component should be between 0 and 255.")

        return True

    def set_rgb(self, red, green, blue):
        """
        Set internal RGB components if provided values are correct.
        Each component consists of an integer between 0 and 255
        representing the intensity of the color.
        """
        for component in [red, green, blue]:
            self.check_rgb_component_value(component)

        self._rgb = (red, green, blue)

    def get_rgb(self):
        """
        Returns the RGB (red, green, blue) triplet for this color.
        """
        return self._rgb
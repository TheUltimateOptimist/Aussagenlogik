class Variables:
    names = []
    values = []

    @classmethod
    def add(cls, name, value):
        if cls.contains(name):
            for i, variable in enumerate(cls.names):
                if variable == name:
                    cls.values[i] = value
        else:            
            cls.names.append(name)
            cls.values.append(value)

    @classmethod
    def remove(cls, name):
        for i, variable in enumerate(cls.names):
            if variable == name:
                del cls.names[i]
                del cls.values[i]
                break

    @classmethod
    def contains(cls, name):
        for variable in cls.names:
            if variable == name:
                return True
        return False

    @classmethod
    def getValue(cls, name):
        for i, variable in enumerate(cls.names):
            if variable == name:
                return cls.values[i]
        return None 
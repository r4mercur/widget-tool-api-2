from datetime import date, datetime

class AutoSerialize(object):
    """Mixin for retrieving public fields of model in json-compatible format"""
    __public__ = None

    def get_public(self, exclude=(), extra=()):
        """Returns model's PUBLIC data for jsonify"""
        data = {}
        keys = self._sa_instance_state.attrs.items()
        public = self.__public__ + extra if self.__public__ else extra
        for k, field in  keys:
            if public and k not in public: continue
            if k in exclude: continue
            value = self._serialize(field.value)
            data[k] = value
        return data

    @classmethod
    def _serialize(cls, value, follow_fk=False):
        if type(value) is date:
            if value < date(1900,1,1):
                ret = None
            else:
                ret = value.isoformat()
        elif type(value) is datetime:
            if value < datetime(1900,1,1):
                ret = None
            else:
                ret = value.isoformat()
        elif hasattr(value, '__iter__'):
            ret = []
            for v in value:
                ret.append(cls._serialize(v))
        elif AutoSerialize in value.__class__.__bases__:
            ret = value.get_public()
        else:
            ret = value

        return ret

__author__ = 'marco'

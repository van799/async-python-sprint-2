import json
from core.job import JobDescriptor


class JobDescriptorEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JobDescriptor):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

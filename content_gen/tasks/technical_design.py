from content_gen.tasks import Task
from content_gen.config import CONFIG

class TechnicalDesign(Task):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_environment(self, environment, rsp):
        doc=CONFIG.artifacts["docs"]["backlog"]
        environment.backlog.append(doc)


from content_gen.tasks import Task
from content_gen.config import CONFIG

class SolutionDesign(Task):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_environment(self, environment, rsp):
        doc=CONFIG.artifacts["docs"]["sdd"]
        environment.design.append(doc)

  


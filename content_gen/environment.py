from pathlib import Path
import pprint
import json
from content_gen.utils import logger
from content_gen.config import CONFIG
from content_gen.utils.write_utils import save_document, save_code

'''
    The Environment class manages and maintain the context of a software development lifecycle. 
'''
class Environment:

    def __init__(
            self,
            request_prompt: str = None,
            content: dict = None,
            team: dict = None,
            directory: Path = None,
            **kwargs
        ):
        
        self.request_prompt = request_prompt
        self.content = content
        self.team = team
        self.directory = directory

    """ 

    def create_task_list(self):
        self.task_list = cl.TaskList()

    async def _display_task(self, title) -> cl.Task:
        task = cl.Task(title=title, status=cl.TaskStatus.RUNNING)
        await self.task_list.add_task(task)
        await self.task_list.send()
        return task
    
    async def _finish_task(self, task):
        task.status = cl.TaskStatus.DONE
        await self.task_list.send()

    async def _update_tasks_status(self, status):
        self.task_list.status = status
        await self.task_list.send()
    """

    def _save_artifacts(self):
        logger.info(f"Saving artifacts: {CONFIG.artifacts}")
        

        if "content" in CONFIG.artifacts:
            code = CONFIG.artifacts["code"]
            for filename, code in code.items():
                logger.debug("Filename:{}. Code:{}".format(filename, code))
                save_code(code, filename, self.directory)
            logger.debug("Code artifact saved.")


      
    
    def get_role(self, role_name: str):
        role = self.team.get(role_name, None)
        if not role:
            raise ValueError(f"Role '{role_name}' not found in the team. You must hire this role.")
        return role
    

    def dict(self):
        return {
            "request_prompt": self.request_prompt,
            "content": self.content,
            "team": self.team,
            "directory": self.directory
        }
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"request_prompt:{pprint.pformat(self.request_prompt)}\content:{pprint.pformat(self.content)}\nteam:{pprint.pformat(self.team)}\ndirectory:{pprint.pformat(self.directory)}"
 
    def log(self, msg):
        logger.debug(f"**After the execution of the task: {msg}**\n\n{self.__str__()}\n\n")



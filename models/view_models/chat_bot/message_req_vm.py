from pydantic import BaseModel


class Configuration(BaseModel):
    maxtokens: int
    temperature: float
    tools: str
    tool_choice: str


class MessageReqVM(BaseModel):
    message: str
    configuration: Configuration

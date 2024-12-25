from typing import Optional

from pydantic import BaseModel, Field


class UserIntent(BaseModel):
    """
    UserIntent
    A Pydantic model representing the Intent identified for the user.

    Attributes:
        intent (str):
            Supported intents are "open_website", "play_music", "time", "open_camera", "quit", "conversation":if no specific intent.
        website_url: Optional(str) = Link to the website in case of open_website intent
        website_name: Optional(str) = Website name in case of open_website intent
        music_name: Optional(str) = music name in case of play_music intent
        reason_for_intent: str = Reason for identified intent
    """
    intent: str = Field(description="Intent of User")
    website_url: Optional[str] = Field(description="Link to the website", default="")
    website_name: Optional[str] = Field(description="Name of the website", default="")
    music_name: Optional[str] = Field(description="music name", default="")
    reason_for_intent: str = Field(description="Reason for intent")